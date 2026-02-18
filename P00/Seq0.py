from pathlib import Path
def seq_ping():
    print("OK")



def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    return file_contents
def len_seq(seq):
    return len(seq)




