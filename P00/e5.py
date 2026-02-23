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

    gene_name = ["U5", "ADA", "FRAT1", "FXN"]
    gene_sequence = [gene1, gene2, gene3, gene4]
    print("EX 5:")
    for i in range(len(gene_name)):
        count = seq_count(gene_sequence[i])
        print(f"Gene {gene_name[i]}: {count}")
