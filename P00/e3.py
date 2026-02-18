from Seq0 import *

if __name__ == "__main__":

    genes = ["ADA", "FAT1", "U5", "FXN"]
    for gene in genes:
        filename = f"../S04/sequences/{gene}.txt"
        seq = seq_read_fasta(filename)
        length = len_seq(seq)
        print(f"Gene{gene} -> length : {length}")