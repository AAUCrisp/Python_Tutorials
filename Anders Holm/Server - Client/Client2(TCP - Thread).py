
import socket

# prefix 
HEADER = 128
PORT = 65432
FORMAT = 'utf-8'
SERVER_IP = "127.0.0.1"
ADDR = (SERVER_IP, PORT)

# set up
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #IPv4 and TCP
client.connect(ADDR)                    #what IP and port the client should connect too

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("Yo my man")