import subprocess

def run_jellyfish(fasta_file, k): # Using Jellyfish each FASTA file to extract all unique k-mers and their counts
    jellyfish_output = fasta_file + f".{k}.jf"  # Jellyfish output file
    # Run Jellyfish command: count k-mers in the FASTA file
    command = [
        "jellyfish", "count",
        "-m", str(k),  # k-mer length
        "-s", "100M",  # Hash table size, adjust based on memory
        "-t", "4",     # Use 4 threads for parallelism
        "-o", jellyfish_output,  # Output file
        fasta_file      # Input FASTA file
    ]
    subprocess.run(command, check=True)  # Run the command

    # Jellyfish dump: Get the k-mers and their counts
    dump_command = [
        "jellyfish", "dump", jellyfish_output
    ]
    result = subprocess.run(dump_command, capture_output=True, text=True, check=True)
    
    # Dictionary to store k-mers and their counts
    kmer_counts = {}

    # Split the stdout into lines and parse the output
    lines = result.stdout.splitlines()
    for i in range(1, len(lines), 2):  # Skip the count lines
        count, kmer = lines[i - 1].strip('>'), lines[i].strip()  # Get count and k-mer
        kmer_counts[kmer] = int(count)  # Store the count as an integer

    return kmer_counts  # Return the dictionary of k-mer counts

def main():
    fasta_files = [
        # Glycine_max GCA Fasta file
        "/Users/abhinav/Downloads/SNRP/FASTA/glycine_max/ncbi_dataset/data/GCA_000004515.5/GCA_000004515.5_Glycine_max_v4.0_genomic.fna",
        # Pisum_saticum GCA Fasta file
        "/Users/abhinav/Downloads/SNRP/FASTA/pisum_sativum/ncbi_dataset/data/GCA_024323335.2/GCA_024323335.2_CAAS_Psat_ZW6_1.0_genomic.fna",
        # Trifolium_pratense GCA Fasta file
        "/Users/abhinav/Downloads/SNRP/FASTA/trifolium_pratense/ncbi_dataset/data/GCA_020283565.1/GCA_020283565.1_ARS_RC_1.1_genomic.fna"
    ]
    
    k = 3  # k-mer length
    all_kmers_counts = {}  # Dictionary to store k-mer counts globally
    
    for fasta_file in fasta_files:
        # Run Jellyfish on each file and get k-mer counts
        kmer_counts = run_jellyfish(fasta_file, k)
        
        # Merge the k-mer counts from the current file into the global dictionary
        for kmer, count in kmer_counts.items():
            if kmer in all_kmers_counts:
                all_kmers_counts[kmer] += count  # Add the counts together if k-mer exists
            else:
                all_kmers_counts[kmer] = count  # Initialize count for new k-mer
    
    # Print the total number of unique k-mers and their counts
    print(f"Total unique k-mers: {len(all_kmers_counts)}")
    for kmer, count in list(all_kmers_counts.items()):  # Print k-mers and their counts
        print(f"{kmer}: {count}")
    
    # Print the total number of k-mers (including duplicates)
    total_kmers = sum(all_kmers_counts.values())
    print(f"Total k-mers (including duplicates): {total_kmers}")

if __name__ == "__main__":
    main()
