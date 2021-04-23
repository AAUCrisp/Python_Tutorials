
import socket
import threading

# prefix 
SERVER_IP = "127.0.0.1"
PORT = 65432                                                                    #Server port
FORMAT = 'utf-8'
ADDR = (SERVER_IP, PORT)
HEADER = 128  
DISCONNECT_MSG = "!DISCONNECT"

# set up
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                      #IPv4 and TCP
server.bind(ADDR)                                                               #the server binds a connection to the server IP and port

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    while True:
        conn, addr = server.accept()                                            #saves the address of the connection(addr) and the connection as an obejct (conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))      #start a new thread and sends the thread to a function with two arguments 
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")              #tell us how many threads has been made


print("[STARTING SERVER]")
start()