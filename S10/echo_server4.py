from Client0 import Client

# Server configuration (change if your server uses another IP/port)
SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080

# Create client
client = Client(SERVER_IP, SERVER_PORT)

# Connect 5 times and send messages
for i in range(5):
    message = f"Message {i}"

    print("To Server:", message)

    # send message and receive response
    response = client.talk(message)

    print("From Server:", response)
    print()