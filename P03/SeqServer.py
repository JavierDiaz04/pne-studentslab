import socket
class Client:
    def __init__(self, IP, PORT):
        self.ip = IP
        self.port = PORT

    def ping(self):
        print("OK")

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()

        return response

import socket

from P00.Seq0 import seq_complement
from Seq1 import*


# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.86"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")
# -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()
        x = msg.split(" ")
        cmd = x[0]

        response = ""

        if cmd == "PING":
            print("PING Command!")
            response = "OK\n"

        elif cmd == "GET":
            seqs = {
                "0": "AAAGGGTTTCCCAAAAA",
                "1": "AAAGGGTTTCCCAGGGG",
                "2": "AAAGGGTTTCCCAAGGG",
                "3": "AAAGGGTTTCCCAAAGG",
                "4": "AAAGGGTTTCCCAAAAG"
            }
            response = seqs.get(x[1], "ERROR")

        elif cmd == "INFO":
            seq1 = x[1]
            s = Seq(seq1)
            dict_result = s.count_bases2()

            response = f"Sequence: {seq1}\n"
            response += f"Total length: {len(seq1)}\n"
            for base in ["A", "C", "G", "T"]:
                response += f"{base}: {dict_result[base]['times']} ({dict_result[base]['percentage']}%)\n"
            elif cmd == "COMP":
            seq1 = x[1]
            print(seq1)
            s = Seq(seq1)
            response = s.seq_complement()

        elif cmd == "REV":
            seq1 = x[1]
            print(seq1)
            s = Seq(seq1)
            response = s.reverse()

        elif cmd == "GENE":
            gene = x[1]
            gene_files = {
                "U5": "../S04/sequences/U5.txt",
                "ADA": "../S04/sequences/ADA.txt",
                "FRAT1": "../S04/sequences/FRAT1.txt",
                "FXN": "../S04/sequences/FXN.txt",
                "RNU6_269P": "../S04/sequences/RNU6_269P.txt"
            }

            if gene in gene_files:
                s1 = Seq()
                response = s1.seq_read_fasta(gene_files[gene])
            else:
                response = "ERROR: Gene not found"



    cs.send(response.encode())

        # -- Close the data socket
    cs.close()

