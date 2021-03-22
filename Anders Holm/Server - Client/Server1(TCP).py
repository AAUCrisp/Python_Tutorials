
#Generel info
#1. This server program establish a connection to a client
#2. Sends a message to the connected client.

import socket

# prefix 
SERVER_IP = socket.gethostbyname(socket.gethostname())                          #gets the IP from this PC
PORT = 1234                                                                     #Server port
FORMAT = 'utf-8'                                            

# set up
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                      #IPv4 and TCP
server.bind((SERVER_IP, PORT))                                                  #need an IP and a port in a tuple

server.listen()                                                                 #the server starts listening for incoming connects

while True:
    conn, addr = server.accept()                                        #everyone who want to connect
    print(f"Connection from {addr} has been established!")
    conn.send(bytes("Hey you connected to the server", FORMAT))         #sends a message to the connected client