
import socket
import threading

# The second link in this project
# The main purpose is to recvieve data from a client with the TCP protocol 
# and send that data to a new server with the UDP protocol

FORMAT = 'utf-8'
HEADER = 2048
DISCONNECT_MESSAGE = '!disconnect'
SERVER_IP = ''
LOCAL_PORT = 9000
CLIENT_PORT = 9400
CLIENT_IP = ''
LOCAL_ADDR = (SERVER_IP, LOCAL_PORT)
CLIENT_ADDR = (CLIENT_IP, CLIENT_PORT)
msg = ''

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(LOCAL_ADDR)

def connect_z():
    try:
        server.connect(CLIENT_ADDR)
        print('\n[+] Connected to Z')
    finally:
        print('[-] Failed to connect to Z')

def handle_x(conn, addr):
    print('\n[+] Connected to X')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"X = [{addr}] {msg}")
            conn.send("Y received message".encode(FORMAT))
            send(msg)
    conn.close()

def send(msg_z):
    server.send(msg_z)
    print('Message send to Z')

def start():
    connect_z()
    server.listen()
    print('[LISTENING] Server starts listening for X')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_x, args=(conn, addr))
        thread.start()
    

start()