import socket


# The first link in the project. 
# The main purpose is to send and recvieve over a TCP connection to a server.

HEADER = 2048
FORMAT = 'utf-8'
PORT = 9000
SERVER = ''
ADDR = (SERVER, PORT)

TCP_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    TCP_client.send(send_length)
    TCP_client.send(message)
    print(TCP_client.recv(2048).decode(FORMAT))

while True:
    msg = input()
    send(msg)


