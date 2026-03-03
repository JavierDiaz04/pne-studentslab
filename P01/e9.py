from Seq1 import Seq

s = Seq()
s.read_fasta("../S04/sequences/U5.txt")

print(f"Sequence : (Length: {s.length()}) {s}")
print(f" Bases: {s.count()}")
print(f" Rev: {s.reverse()}")
print(f" Comp: {s.seq_complement()}")