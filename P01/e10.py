from Seq1 import Seq

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in genes:
    print("NULL Seq created")
    s = Seq()
    s.read_fasta(f"../S04/sequences/{gene}.txt")
    print(f"Gene {gene}: Most frequent Base: {s.frequency()}")