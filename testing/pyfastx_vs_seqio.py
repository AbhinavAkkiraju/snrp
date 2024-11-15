import time
from Bio import SeqIO
import pyfastx

# List of FASTA file paths
fasta_files = [
    "/Users/abhinav/Downloads/SNRP/FASTA/glycine_max/ncbi_dataset/data/GCA_000004515.5/GCA_000004515.5_Glycine_max_v4.0_genomic.fna",
    "/Users/abhinav/Downloads/SNRP/FASTA/pisum_sativum/ncbi_dataset/data/GCA_024323335.2/GCA_024323335.2_CAAS_Psat_ZW6_1.0_genomic.fna",
    "/Users/abhinav/Downloads/SNRP/FASTA/trifolium_pratense/ncbi_dataset/data/GCA_020283565.1/GCA_020283565.1_ARS_RC_1.1_genomic.fna"
]

# Function to read sequences using Bio.SeqIO
def read_with_seqio():
    sequences = []
    for fasta_file in fasta_files:
        for record in SeqIO.parse(fasta_file, "fasta"):
            sequences.append(str(record.seq))
    return sequences

# Function to read sequences using pyfastx
def read_with_pyfastx():
    sequences = []
    for fasta_file in fasta_files:
        f = pyfastx.Fasta(fasta_file)
        for seq in f:
            sequences.append(str(seq.seq))
    return sequences

# Measure time for SeqIO approach
start_time = time.time()
read_with_seqio()
seqio_time = time.time() - start_time
print(f"Time taken with Bio.SeqIO: {seqio_time:.4f} seconds")

# Measure time for pyfastx approach
start_time = time.time()
read_with_pyfastx()
pyfastx_time = time.time() - start_time
print(f"Time taken with pyfastx: {pyfastx_time:.4f} seconds")

# Making sure sequences are the same
print(read_with_seqio() == read_with_pyfastx())

# Compare the times
if seqio_time < pyfastx_time:
    print(f"Bio.SeqIO is faster by {pyfastx_time - seqio_time:.4f} seconds")
else:
    print(f"pyfastx is faster by {seqio_time - pyfastx_time:.4f} seconds")
