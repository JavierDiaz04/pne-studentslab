import socket

HOST = "212.128.255.96"
PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("The server is configured!")

connections = 0   # contador de conexiones

while True:
    print("Waiting for Clients to connect")

    client_socket, addr = server_socket.accept()

    connections += 1

    print(f"CONNECTION {connections}. Client IP,PORT: {addr}")

    data = client_socket.recv(1024)

    if data:
        message = data.decode()
        print("Message received:", message)

        response = "ECHO: " + message
        client_socket.send(response.encode())

    client_socket.close()