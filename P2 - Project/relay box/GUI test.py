from tkinter import *  
from djitellopy import tello
import cv2
import threading
import socket
import time
from PIL import ImageTk, Image
import imageio

FORMAT = 'utf-8'
HOST = ''
PORT = 9000
UDP_RELAY = (HOST,PORT)
TELLO_ADDR = ('192.168.10.1', 8889)

dataStats = []

UDP_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_client_socket.bind(UDP_RELAY)

tello = tello.Tello()
root = Tk()
tello.connect()
root.title('Videostream')

def video_streamGUI():
    tello.streamon()
    while True:
        img = tello.get_frame_read().frame # get the 
        #img = cv2.resize(img, (360,240))
        cv2.imshow("Live Stream", img)
        cv2.waitKey(1)
        
        
video_streamGUI()
root.mainloop()

def control_drone():
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

def recv_state():
    while True: 
        try:
            data, server = UDP_client_socket.recvfrom(1518)
            dataStats.append(data.decode(encoding=FORMAT))
        except Exception:
            print ('\nExit . . .\n')
            break


def state_print():
    time.sleep(5)
    print(dataStats[-1])

thread_video = threading.Thread(target=video_stream)
thread_video.start()
thread_control = threading.Thread(target=control_drone)
thread_control.start()