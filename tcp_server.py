import socket 

# Define the srevre address and port

HOST = '0.0.0.0' # Listen on all network interfaces
PORT = 8080

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET: Address Family, SOCK_STREAM: TCP

# socket.AF_INET: Uses IPv4.
# socket.SOCK_STREAM: Establishes a TCP connection

server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"[*] Listening on {HOST}:{PORT}")
# In Python, placing an f before a string allows you to embed expressions directly within the string using curly braces {}.

while True:
    client_socket, client_address = server_socket.accept()
    print(f"[+] Connection from {client_address}")

    # Recieve data from the client
    data = client_socket.recv(1024).decode() #recv(1024): It is the buffer size, Receives up to 1024 bytes from the client.

    print(f"[+] Received: {data}")

    # Send a response back to the client
    response = "Hello, Client!"
    client_socket.send(response.encode()) #send(): Sends a response back to the client.

    # Close the client socket
    client_socket.close()
    

    #f is for formatted strings in Python.
    # [] are used for log tagging.
    # + is simply part of the tag format.
    # [+] for positive events (e.g., connection received).
    # [-] for errors or disconnections.
    # [*] for informational messages (e.g., server started).