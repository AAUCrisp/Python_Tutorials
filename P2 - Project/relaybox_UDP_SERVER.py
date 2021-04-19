
# Imports
import threading, socket, time, platform
from djitellopy import Tello

# Variables 
PORT = 9000
HEADER = 64
FORMAT = 'utf-8'
LOCA_HOST = ''
TELLO_ADDR = ('192.168.10.1', 8889)
LOCA_CLIENT = (LOCA_HOST,PORT)
START = 'command'
TELLO_MSG = []

# UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(LOCA_CLIENT)


def start_up():
    msg = START.encode(FORMAT)
    sent = udp_socket.sendto(msg,TELLO_ADDR)


def recv():
    while True: 
        try:
            data, server = udp_socket.recvfrom(1518)
            print(data.decode(encoding=FORMAT))
        except Exception:
            print ('\nExit . . .\n')
            break

'''
def recv():
    while True: 
        try:
            data, server = udp_socket.recvfrom(1518)
            print(data.decode(encoding=FORMAT))
        except Exception:
            print ('\nExit . . .\n')
            break

'''

# not_connected = True
# while not_connected:
 #   START = START.encode(FORMAT)
  #  udp_socket.sendto(START,TELLO_ADDR)
   # if recv() == 'ok':
    #    not_connected = False


recvThread = threading.Thread(target=recv)
recvThread.start()



'''
tello = Tello()
print('[CONNECTING] connecting to the drone...')
tello.connect()

# handle data recvieved from the tello drone
def recv_tello():

    while True:
        try:
            i=0
            data, server = udp_socket.recv(HEADER)
            TELLO_MSG[i] = data.decode(FORMAT)

            if TELLO_MSG[i] == 'end':
               udp_socket.close()
                break

            print(TELLO_MSG[i])
            i+1



def start():
    print('[CONNECTING] You´re connecting to the tello drone \n Running start up now . . .')
    thread = threading.Thread(target=recv_tello)
    time.sleep(3)
    udp_socket.sendto(START,TELLO_ADDR)

    if TELLO_MSG == "ok":
        print('[CONNECTED] Successfully connected to the tello drone')


while True: 
    try:
        python_version = str(platform.python_version())
        version_init_num = int(python_version.partition('.')[0]) 
       # print (version_init_num)
        if version_init_num == 3:
            TELLO_MSG = input("")
        elif version_init_num == 2:
            TELLO_MSG2 = input("")
        
        if not TELLO_MSG:
            break  

        if 'end' in TELLO_MSG:
            print ('...')
            udp_socket.close()  
            break
        
        print('\nDrone now connected')
        # Send data
        TELLO_MSG = TELLO_MSG.encode(encoding=FORMAT) 
        sent = udp_socket.sendto(TELLO_MSG, TELLO_ADDR)
        tello.takeoff()

        tello.move_left(100)
        tello.rotate_counter_clockwise(360)
        tello.move_forward(100)

        tello.land()
    except KeyboardInterrupt:
        print ('\n . . .\n')
        udp_socket.close()  
        break
'''