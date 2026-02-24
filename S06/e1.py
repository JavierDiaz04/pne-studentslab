class Seq:
    def __init__(self, seq):
        valid_bases = ('A', 'C', 'G', 'T')
        is_valid = True
        self.seq = seq
        for base in seq:
            if base in valid_bases:
                is_valid = True
            else:
                is_valid = False
        if is_valid == True:
            self.seq = seq
            print("New sequence created !")
        else:
            self.seq = "ERROR"
            print("ERROR")

    def __str__(self):
        return self.seq



s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
