from Seq0 import *

if __name__ == "__main__":
    FILENAME = "../S04/sequences/U5.txt"

    gene = Path(FILENAME).read_text()

    clean = seq_read_fasta(gene)
    final = clean[0:20]

    print("DNA File: U5.txt")
    print("The first 20 bases are:")
    print(final)