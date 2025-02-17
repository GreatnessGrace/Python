import socket

# Server address and port

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

# Send a message to the server
message = "Hello, Server!"
client_socket.send(message.encode())

# Receive a response from the server
response = client_socket.recv(1024).decode()
print(f"[+] Received from server: {response}")

# Close the connection
client_socket.close() 