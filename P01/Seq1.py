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
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return {"A": 0, "C": 0, "T": 0, "G": 0}
        count = {"A": 0, "C": 0, "T": 0, "G": 0}
        for ch in self.strbases:
            if ch in counts:
                count += 1
        return count

