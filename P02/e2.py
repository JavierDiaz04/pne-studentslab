from client0 import Client
PRACTICE = 2
EXERCISE = 2
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.95"
PORT = 8080
c = Client(IP, PORT)
print(c)