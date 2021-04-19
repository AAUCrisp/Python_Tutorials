
# Imported liberaies
import threading, socket, time

# Varialbes
FORMAT = 'utf-8'
HEADER = 64
PORT = 9000
DISCONNECT_MSG = '!disconnect'
TELLO_ADDR = ('192.168.10.1', 8889)
SERVER_IP = socket.gethostbyname(socket.gethostname()) # gets IP address of this device
ADDR = (SERVER_IP, PORT)


# UDP and TCP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(ADDR)

# Functions
def tcp_client(conn, addr):

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


def start():
    tcp_socket.listen()
    print(f'\n[LISTENING] TCP server is listing on {SERVER_IP} and port {PORT}')

    while True:
        conn, addr = tcp_socket.accept()
        thread = threading.Thread(target=tcp_client, args=(conn, addr))
        thread.start()
        print(f'\n[CONNECTED] User {addr} has connected to the server')
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


# Here the relay box are being initialized
print('[STARTING] server is starting')
time.sleep(3)
start()
