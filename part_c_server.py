'''
Program Description: This program creates a server that a client can connect to via port 1234. It listens for incoming requests to the host IPv4 address.
Once it receives a request it accepts it, sends teh client a message, and then closes the request. Once the request is closed, the server will shutdown.
'''

# Name: Dylan Bailey
# Student ID: 20114978

# Date                   Version                    Reason for Change
# 30/10/2024             1                          Creation of program
# 30/10/2024             2                          Added a break statement at the end of the first iteration of the while loop to shutdown the server
#                                                   once one request has been served

import socket

def start_server():

    # Creates a socket object while specifying IPv4 and TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the server using the bind() mehtod to the specified IP address and port
    host = '127.0.0.1'
    port = 1234
    server_socket.bind((host, port))
    print(f"Server started on {host}:{port}")

    # Puts the server into listening mode. The argument '5' is the maximum number of pending connections allowed
    server_socket.listen(5)
    print("Server is listening for incoming connections...")

    # Accepts an incoming connection. The method accept() waits for incoming connections, then returns a new socket object for the client and their address once they connect
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client at {client_address}")

        # Send a welcome message to the client
        client_socket.send("Hello, client! You are connected to Dylan's server.".encode())

        # Close the connection with the client
        client_socket.close()
        print(f"Connection with {client_address} closed.")

        # Breaks the loop after one request has been served. This can easily be modified to serve a specific number of requests or to keep listening until the user intervenes
        break


    # Close the server socket when the above loop is broken
    server_socket.close()
    print("Server shutdown.")

if __name__ == "__main__":
    start_server()
