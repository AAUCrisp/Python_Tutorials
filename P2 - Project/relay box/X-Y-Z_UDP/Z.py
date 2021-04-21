import socket 
import threading

HEADER = 2048
PORT = 9400
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[+] Y user {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        print(f"[{addr}] {msg}")
        conn.send("Z received message".encode(FORMAT))       

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server listen for Z")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 6}")

SERVER_IP = socket.gethostbyname(socket.gethostname())
print('Your IP address: ' + SERVER_IP + '\n\n')

print("[STARTING] Z is starting...")
start()