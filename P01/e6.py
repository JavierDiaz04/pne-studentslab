from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 1: {s1} (Length: {s1.length()}) ")
print(f"Bases:, {s1.count()}")

print(f"Sequence 1: {s2} (Length: {s2.length()}) ")
print(f"Bases:, {s2.count()}")

print(f"Sequence 1: {s3} (Length: {s3.length()}) ")
print(f"Bases:, {s3.count()}")
