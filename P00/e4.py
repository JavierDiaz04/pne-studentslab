from pathlib import Path

from Seq0 import *

if __name__ == "__main__":
    U5 = "../S04/sequences/U5.txt"
    ADA = "../S04/sequences/ADA.txt"
    FRAT1 = "../S04/sequences/FRAT1.txt"
    FXN = "../S04/sequences/FXN.txt"

    geneU5 = Path(U5).read_text()
    geneADA = Path(ADA).read_text()
    geneFRAT1 = Path(FRAT1).read_text()
    geneFXN = Path(FXN).read_text()

    result1 = seq_count_base(geneU5)
    result2 = seq_count_base(geneADA)
    result3 = seq_count_base(geneFRAT1)
    result4 = seq_count_base(geneFXN)

    print("EX 4:")
    gene_names = ["U5", "ADA", "FRAT1", "FXN"]
    results = [result1, result2, result3, result4]

    for i in range(len(gene_names)):
        print(f"Gene {gene_names[i]}:")
        seq_printer_4(results[i])
        print()