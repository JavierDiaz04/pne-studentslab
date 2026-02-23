from pathlib import Path
def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    return file_contents

def len_seq(seq):
    return len(seq)
def seq_count_base(seq):
    bases = ['A', 'C', 'G', 'T']
    count = [0, 0, 0, 0]
    for gene in seq:
        if gene in bases:
            count[bases.index(gene)] += 1
    return count

def seq_printer_4(counts):
    bases = ['A', 'C', 'G', 'T']
    for i in range(len(bases)):
        print(f"  {bases[i]}: {counts[i]}")



