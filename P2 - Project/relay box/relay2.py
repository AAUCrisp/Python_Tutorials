
# Imports
import threading, socket, time, platform
from djitellopy import tello
import cv2

# Variables 
HEADER = 1024
FORMAT = 'utf-8'
init = 'command'

HOST = ''
PORT = 9000
UDP_SERVER = (HOST,PORT)

TELLO_ADDR = ('192.168.10.1', 8889)

# UDP server 
UDP_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_server_socket.bind(UDP_SERVER)
me = tello.Tello()


# UDP client
UDP_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def recv():
    while True: 
        try:
            data, addr = UDP_client_socket.recvfrom(HEADER)
            print('Command: '+ data.decode(encoding=FORMAT) + '\n')
        except Exception:
            print ('\nExit . . .\n')
            break

# Create vindow with videostream
def video():
    while True:
        img = me.get_frame_read().frame
        cv2.imshow("Live Stream", img)
        cv2.waitKey(1)
   
def start():
    control_thread = threading.Thread(target=recv)
    control_thread.start()

    me.streamon()
    stream_thread = threading.Thread(target=video)
    stream_thread.start()
    video()

# init = init.encode(encoding=FORMAT) 
# sent = UDP_client_socket.sendto(init, TELLO_ADDR)

    while True:
        try:
            msg = input('')

            if 'end' in msg:
                print ('...')
                UDP_client_socket.close()  
                break

            # Send data
            msg = msg.encode(encoding=FORMAT) 
            sent = UDP_client_socket.sendto(msg, TELLO_ADDR)
        except KeyboardInterrupt:
            print ('\n . . .\n')
            UDP_client_socket.close()  
            break

start()

