from pathlib import Path
class Seq:
    def __init__(self, strbases = None):
        if strbases is None:
            self.strbases = "NULL"
            print("NULL sequence created!")
            return
        else:
            valid_bases = {"A", "C", "G", "T"}
            error_found = False

        for ch in strbases:
            if ch not in valid_bases:
                error_found = True

        if error_found == True:
            self.strbases = "ERROR"
            print("Invalid sequence")
        else:
            self.strbases = strbases
            print("New sequence created!")

    def __str__(self):
        return self.strbases
    def length(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return len(self.strbases)
    def count_base(self, base):
        if self.strbases in ("NULL", "ERROR"):
            return 0
        return self.strbases.count(base)

    def count(self):
        bases = {"A": 0, "C": 0, "T": 0, "G": 0}
        for i in self.strbases:
            if i in bases:
                bases[i] = bases[i] + 1
        if self.strbases in ("NULL", "ERROR"):
            return bases
        return bases

    def reverse(self):
        if self.strbases in ("NULL", "ERROR"):
            return self.strbases
        return self.strbases[::-1]

    def seq_complement(self):
        if self.strbases in ("NULL", "ERROR"):
            return self.strbases
        seq = self.strbases
        complement_seq = ""
        for base in seq:
            if base == 'A':
                complement_seq += "T"
            elif base == 'T':
                complement_seq += "A"
            elif base == 'C':
                complement_seq += "G"
            elif base == 'G':
                complement_seq += "C"
        return complement_seq

    def read_fasta(self, filename):
        content = Path(filename).read_text()
        first_newline = content.find("\n")
        seq = content[first_newline+1:]
        seq = seq.replace("\n", "")
        self.strbases = seq

    def frequency(self):
        if self.strbases in ("NULL", "ERROR"):
            return "Not valid sequence"
        bases = {"A": 0, "C": 0, "T": 0, "G": 0}
        for i in self.strbases:
            if i in bases:
                bases[i] +=  1
        return max(bases, key=bases.get)


