
# Imports
import threading, socket, time, platform
from djitellopy import Tello
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
me.streamon()

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

control_thread = threading.Thread(target=recv)
control_thread.start()

def videoStream():
    while True:
    img = me.get_frame_read().frame # get the 
    #img = cv2.resize(img, (360,240))
    cv2.imshow("image", img)
    cv2.waitKey(1)

stream_thread = threading.Thread(target=videoStream)
stream_thread.start()

# initi
init = init.encode(encoding=FORMAT) 
sent = UDP_client_socket.sendto(init, TELLO_ADDR)

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



