from pathlib import Path

from client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.93"
PORT = 8080

c = Client(IP, PORT)
print(f"Connection to SERVER at {IP}, PORT: {PORT}")

# Create NULL sequence
s = Seq()

# Files
U5_FILE = "../S04/sequences/U5.txt"
FRAT1_FILE = "../S04/sequences/FRAT1.txt"
ADA_FILE = "../S04/sequences/ADA.txt"

genes = {
    "U5": U5_FILE,
    "FRAT1": FRAT1_FILE,
    "ADA": ADA_FILE
}

for gene_name, filepath in genes.items():

    # Load gene using Seq class
    gene = Seq()
    gene.read_fasta(filepath)

    # 1️⃣ Send message
    message = f"Sending {gene_name} Gene to the server..."
    print("To Server:", message)
    response = c.talk(message)
    print("From Server:")
    print(response)

    # 2️⃣ Send sequence
    sequence = str(gene)
    print("To Server:", sequence)
    response = c.talk(sequence)
    print("From Server:")
    print(response)

c.close()