
# Imported liberaies
import threading, socket, time, cv2, platform
from djitellopy import Tello


# Varialbes
FORMAT = 'utf-8'
HEADER = 2048
PORT = 9000
DISCONNECT_MSG = '!disconnect'
TELLO_ADDR = ('192.168.10.1', 8889)
SERVER_IP = ''  # socket.gethostbyname(socket.gethostname()) # gets IP address of this device
ADDR = (SERVER_IP, PORT)

# Video stream
VS_UDP_IP = '0.0.0.0'
VS_UDP_PORT = 11111
VS_SERVER_ADDR = (VS_UDP_IP,VS_UDP_PORT)

# State stream
STATE_UDP_IP = '0.0.0.0'
STATE_UDP_PORT = 8890 # receive drone info
SS_UDP_ADDR = (STATE_UDP_IP, STATE_UDP_PORT)


# UDP and TCP socket objects
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(ADDR)
udp_socket.bind(VS_SERVER_ADDR)

# Create Tello object
tello = Tello()

# handle UDP client
def udp_video(data, addr):
    video.streamon()
    data_stream = True
    while data_stream:
        img = tello.get_frame_read().frame # get the 
        #img = cv2.resize(img, (360,240))
        cv2.imshow("Live Stream", img)
        cv2.waitKey(1)

def recv():
    while True: 
        try:
            data, addr = udp_socket.recvfrom(HEADER)
            print('Command: '+ data.decode(encoding=FORMAT) + '\n')
        except Exception:
            print ('\nExit . . .\n')
            break

# handle TCP client
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
            conn.send("OK".encode(FORMAT))

    conn.close()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


def start():
    tcp_socket.listen()
    tello.connect()
    
    tello.takeoff()
    conn, addr = tcp_socket.accept()
    data, addr = udp_socket.recvfrom(HEADER)
    control_thread = threading.Thread(target=recv)
    thread_video = threading.Thread(target=udp_video, args=(data, addr))
    thread_user = threading.Thread(target=tcp_client, args=(conn, addr))
    control_thread.start()
    thread_video.start()
    thread_user.start()
    while True:
             
        try:
            msg = input('')
            if 'end' in msg:
                print ('...')
                udp_socket.close()  
                break
            msg = msg.encode(encoding=FORMAT) 
            sent = udp_socket.sendto(msg, TELLO_ADDR)
        except KeyboardInterrupt:
            print ('\n . . .\n')
            udp_socket.close()  
            break
        
        #print(f'\n[CONNECTED] User {addr} has connected to the server')
        #print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


# Here the relay box are being initialized
print('[STARTING] server is starting')
time.sleep(3)
start()
