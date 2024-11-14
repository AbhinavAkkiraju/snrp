from Bio import SeqIO # Importing Sequence Input/Output interface from Biopython

fasta_files = [
    # Glycine_max GCA Fasta file
    "/Users/abhinav/Downloads/SNRP/FASTA/glycine_max/ncbi_dataset/data/GCA_000004515.5/GCA_000004515.5_Glycine_max_v4.0_genomic.fna",
    # Pisum_saticum GCA Fasta file
    "/Users/abhinav/Downloads/SNRP/FASTA/pisum_sativum/ncbi_dataset/data/GCA_024323335.2/GCA_024323335.2_CAAS_Psat_ZW6_1.0_genomic.fna",
    # Trifolium_pratense GCA Fasta file
    "/Users/abhinav/Downloads/SNRP/FASTA/trifolium_pratense/ncbi_dataset/data/GCA_020283565.1/GCA_020283565.1_ARS_RC_1.1_genomic.fna"
]

sequences = [] # List of sequences

for fasta_file in fasta_files: # Looping through each file to extract the sequences
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequences.append(str(record.seq)) # Adding DNA sequences from all crops to sequences list