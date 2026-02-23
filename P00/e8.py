from pathlib import Path

from Seq0 import *

if __name__ == "__main__":
    U5 = "../S04/sequences/U5.txt"
    ADA = "../S04/sequences/ADA.txt"
    FRAT1 = "../S04/sequences/FRAT1.txt"
    FXN = "../S04/sequences/FXN.txt"

    gene1 = Path(U5).read_text()
    gene2 = Path(ADA).read_text()
    gene3 = Path(FRAT1).read_text()
    gene4 = Path(FXN).read_text()

    cleanU5 = seq_read_fasta(gene1)
    cleanADA = seq_read_fasta(gene2)
    cleanFRAT1 = seq_read_fasta(gene3)
    cleanFXN = seq_read_fasta(gene4)

    gene_names = ["U5", "ADA", "FRAT1", "FXN"]
    gene_sequences = [cleanU5, cleanADA, cleanFRAT1, cleanFXN]

    print("EX 8:")
    for i in range(len(gene_names)):
        most_repeated = counter((base_counter(gene_sequences[i])))
        print(f"Gene {gene_names[i]}: Most frequent Base: {most_repeated}")