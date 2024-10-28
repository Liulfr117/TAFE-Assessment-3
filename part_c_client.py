'''
Program Description: This program creates a cient that can connect to a server at address 127.0.0.1 via port 1234. Once connected, it revceives
a text message which it then decodes and displays. Once it has received the message, it closes the connection with the server.
'''

# Name: Dylan Bailey
# Student ID: 20114978

# Date                   Version                    Reason for Change
# 30/10/2024             1                          Creation of program
# 31/10/2024             2                          Added additional print statements to provide the user withmore information, making for a better user experience



import socket

def start_client():
    # Creates a socket object and specifies IPv4 and TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connects to the server on localhost and port 1234
    host = '127.0.0.1'
    port = 1234
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    # Receives data from the server. Buffer size is 1024 bytes
    message = client_socket.recv(1024)
    # The received text data is decoded and displayed in a string
    print("Message from server:", message.decode())

    # Closes the connection
    client_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    start_client()
