import socket 
import threading

HEADER = 2048
Y_PORT = 9000
Y_SERVER = socket.gethostbyname(socket.gethostname())
Y_ADDR = (Y_SERVER, Y_PORT)
FORMAT = 'utf-8'

Z_PORT = 9400
Z_SERVER = '192.168.56.1'
Z_ADDR = (Z_SERVER, Z_PORT)

y_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
z_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
y_server.bind(Y_ADDR)


def handle_client(conn, addr):
    print(f"[+] X user {addr} connected.\n")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            print(f"\nX [{addr}] sends: {msg}")
            conn.send("Y received message".encode(FORMAT))
            send(msg)
            print('[TRANSMIT] Msg from X to Z sent')
    conn.close()

def send(message):
    z_server.send(message.encode(FORMAT))

def start():
    z_server.connect(Z_ADDR)
    print('[+] Connected to Z')
    y_server.listen()
    print("[LISTENING] Server is listening for X")
    while True:
        conn, addr = y_server.accept()
        x = threading.Thread(target=handle_client, args=(conn, addr))
        x.start()
        print(f"[ACTIVE CONNECTIONS] X = {threading.activeCount() - 7}")


print("[STARTING] server is starting...")
start()