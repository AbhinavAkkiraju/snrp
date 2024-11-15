import os
import concurrent.futures
import pyfastx
from itertools import chain

def extract_kmers(seq, k):
    """
    Efficient k-mer extraction using generator expressions.
    """
    return (seq[i:i+k] for i in range(len(seq) - k + 1))

def process_fasta(fasta_file, k):
    """
    Process a single FASTA file, extracting k-mers from all sequences.
    """
    k_mers = []
    f = pyfastx.Fasta(fasta_file)
    
    # Extract k-mers for each sequence in the FASTA file
    for seq in f:
        k_mers.extend(extract_kmers(str(seq.seq), k))
        
    return k_mers

def main():
    fasta_files = [
        "/Users/abhinav/Downloads/SNRP/FASTA/glycine_max/ncbi_dataset/data/GCA_000004515.5/GCA_000004515.5_Glycine_max_v4.0_genomic.fna",
        "/Users/abhinav/Downloads/SNRP/FASTA/pisum_sativum/ncbi_dataset/data/GCA_024323335.2/GCA_024323335.2_CAAS_Psat_ZW6_1.0_genomic.fna",
        "/Users/abhinav/Downloads/SNRP/FASTA/trifolium_pratense/ncbi_dataset/data/GCA_020283565.1/GCA_020283565.1_ARS_RC_1.1_genomic.fna"
    ]
    
    k = 3  # Define the k-mer length
    
    # Use ProcessPoolExecutor for parallel processing of FASTA files
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Map each FASTA file to the process function
        kmer_results = list(executor.map(process_fasta, fasta_files, [k] * len(fasta_files)))
    
    # Flatten the list of k-mer results from all FASTA files
    all_kmers = list(chain.from_iterable(kmer_results))
    
    # Print or process the k-mers
    print(f"Extracted {len(all_kmers)} k-mers.")
    
if __name__ == '__main__':
    main()
