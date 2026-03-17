from P03.client0 import Client
from Seq1 import Seq

print("-----| Practice 2, Exercise 6 |------")

IP = "212.128.255.93"
PORT = 8080

c = Client(IP, PORT)
print(f"Connection to SERVER at {IP}, PORT: {PORT}")

# Create NULL sequence
s = Seq()

# Read FRAT1 from file using your method
frat1 = Seq()
frat1.read_fasta("../S04/sequences/FRAT1.txt")

print("Gene FRAT1:", frat1)

# Take 5 fragments of 10 bases
for i in range(5):
    start = i * 10
    end = (i + 1) * 10
    fragment = frat1.strbases[start:end]
    print(f"Fragment {i+1}: {fragment}")

# Send to server
c.talk("Sending FRAT1 Gene to the server, in fragments of 10 bases...")

for i in range(5):
    start = i * 10
    end = (i + 1) * 10
    fragment = frat1.strbases[start:end]
    c.talk(f"Fragment {i+1}: {fragment}")