from client0 import Client
from Seq1 import Seq
FRAT1 = "../S04/sequences/FRAT1.txt"
s = Seq()

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.92" #This is the IP from the Pc i was working 3rd row, closest to the hallway on the left side from professors' POV
PORT = 8080
PORT2 = 8081
c1 = Client(IP, PORT)
c2 = Client(IP, PORT2)

def cut(string):
    fragments = []
    for i in range(10):
        start_index = i * 10
        end_index = start_index + 10
        fragment = string[start_index:end_index]
        fragments.append(fragment)
    return fragments

print(c1)
print(c2)
print(f"Sending the FRAT1 Gene to the server...")

s.read_fasta(FRAT1)
gene = s.strbases
print(f"Gene FRAT1: {gene}")

fragments = cut(gene)

for index in range(len(fragments)):
    i = index + 1
    ch = fragments[index]

    print(f"Fragment {i}: {ch}")
    if i % 2 != 0:
        response = c1.talk(ch)
    else:
        response = c2.talk(ch)