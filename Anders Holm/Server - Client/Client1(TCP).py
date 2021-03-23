
#Generel info
# 1.This client program establish a connection to a server 
# 2.Print any recvieved message from that server.
# 3.Disconnect from the server

import socket

# prefix 
PORT = 65432
FORMAT = 'utf-8'
SERVER_IP = socket.gethostbyname(socket.gethostname()) #gets the IP from this PC IPv4 only
BUFFER = 1024


# set up
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 and TCP
s.connect((SERVER_IP,PORT)) #what IP and port the client should connect to

msg = s.recv(BUFFER) #recieved message what a max size of BUFFER
print(msg.decode(FORMAT)) #decodes the message to FORMAT and prints it

