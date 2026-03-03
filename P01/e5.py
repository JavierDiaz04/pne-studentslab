from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print(f"Sequence 0: (Length: {s1.length()}) {s1}")
print(f" A: {s1.count_base('A')}, C: {s1.count_base('C')}, T: {s1.count_base('T')}, G: {s1.count_base('G')}")

print(f"Sequence 1: (Length: {s2.length()}) {s2}")
print(f" A: {s2.count_base('A')}, C: {s2.count_base('C')}, T: {s2.count_base('T')}, G: {s2.count_base('G')}")

print(f"Sequence 2: (Length: {s3.length()}) {s3}")
print(f" A: {s3.count_base('A')}, C: {s3.count_base('C')}, T: {s3.count_base('T')}, G: {s3.count_base('G')}")