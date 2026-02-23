from pathlib import Path
def seq_ping():
    print("OK")

def seq_read_fasta(seq):
    first_end = seq.find("\n")
    seq1 = seq[first_end:]
    seq1 = seq1.replace("\n","")
    return seq1


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

def seq_count(seq):
    base_count = {}
    for i in seq:
        if i in "ACGT":
            if i in base_count:
                base_count[i] += 1
            else:
                base_count[i] = 1
    return base_count

def seq_reverse(seq, n):
    sequence = seq[0:n]
    return sequence[::-1]
def seq_complement(sequence, n):
    sequence2 = sequence[0:n]
    complementary_sequence = ""

    for base in sequence2:
        if base == 'A':
            complementary_sequence = complementary_sequence + "T"
        elif base == 'T':
            complementary_sequence = complementary_sequence + "A"
        elif base == 'C':
            complementary_sequence = complementary_sequence + "G"
        elif base == 'G':
            complementary_sequence = complementary_sequence + "C"
        else:
            complementary_sequence = complementary_sequence + base

    return complementary_sequence

def base_counter(seq):
    base_counts = {}
    for base in seq:
        if base in base_counts:
            base_counts[base] = base_counts[base] + 1
        else:
            base_counts[base] = 1

    return base_counts

def counter(dic):
    max_value = None
    max_repetition = 0
    for value in dic:
        if dic[value] > max_repetition:
            max_repetition = dic[value]
            max_value = value

    return max_value

