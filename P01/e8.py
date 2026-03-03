from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 0: (Length: {s1.length()}) {s1}")
print(f" Bases: {s1.count()}")
print(f" Rev: {s1.reverse()}")
print(f" Comp: {s1.seq_complement()}")

print(f"Sequence 1: (Length: {s2.length()}) {s2}")
print(f" Bases: {s2.count()}")
print(f" Rev: {s2.reverse()}")
print(f" Comp: {s2.seq_complement()}")

print(f"Sequence 2: (Length: {s3.length()}) {s3}")
print(f" Bases: {s3.count()}")
print(f" Rev: {s3.reverse()}")
print(f" Comp: {s3.seq_complement()}")