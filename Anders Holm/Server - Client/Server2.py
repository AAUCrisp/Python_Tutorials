
#Generel info
#1. This server program establish a connection to a client
#2. Sends a message to the connected client.
#3. Close the connection to the client

msg = "Hey you connected to the server!"
print(f'{len(msg):<10}')                                                         #makes a fixed length header at the size of 10
print(f'{len(msg):<10}' + msg)


'''
import socket

# prefix 
HEADER = 
SERVER_IP = socket.gethostbyname(socket.gethostname())                          #gets the IP from this PC
PORT = 1234                                                                     #Server port
FORMAT = 'utf-8'                                            

# set up
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                      #IPv4 and TCP
server.bind((SERVER_IP, PORT))                                                  #need an IP and a port in a tuple

server.listen()                                                                 #the server starts listening for incoming connects

while True:
    clientsocket, addr = server.accept()                                        #everyone who want to connect
    print(f"Connection from {addr} has been established!")
    clientsocket.send(bytes("Hey you connected to the server", FORMAT))         #sends a message to the connected client
    clientsocket.close()                                                        #close the connection

'''