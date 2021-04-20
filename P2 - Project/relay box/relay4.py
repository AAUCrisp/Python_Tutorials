import logging, socket, time
from threading import Thread
from typing import Optional, Union, Type, Dict

import cv2


class relay:

    TELLO_IP = '192.168.10.1' # Tello drone IP address
    VS_UDP_IP = '0.0.0.0' # IP address for recieving videostream
    
    VS_UDP_PORT = 11111 # Port for recieving videostream
    CONTROL_UDP_PORT = 8889 # Port for sending control commands
    STATE_UDP_PORT = 8890 # Port for recieving drone state

    stream_on = False # controlling if the stream is on
    is_flying = False # controlling if the drone is flying

    def __init__(self, host):
        super().__init__()

# 
def recv():
    while True: 
        try:
            data, addr = UDP_client_socket.recvfrom(HEADER)
            print('Command: '+ data.decode(encoding=FORMAT) + '\n')
        except Exception:
            print ('\nExit . . .\n')
            break