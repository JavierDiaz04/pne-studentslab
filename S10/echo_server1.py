import socket

HOST = "212.128.255.96"   # Listen on all interfaces
PORT = 8080

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to address and port
server_socket.bind((HOST, PORT))

# Listen for connections
server_socket.listen(5)

print("The server is configured!")
print("Waiting for Clients to connect")

while True:
    client_socket, addr = server_socket.accept()
    print("A client has connected to the server!")

    # Receive message
    data = client_socket.recv(1024)

    if data:
        message = data.decode().strip()
        print(f"Message received: {message}")

        # Echo response
        response = "ECHO: " + message
        client_socket.send(response.encode())

    client_socket.close()