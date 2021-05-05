import socket, time, threading
from djitellopy import tello

BUFFER_SIZE = 2048
FORMAT = 'utf-8'
START_ERROR = 'Tello connection error'

# Info connection between the user and the relaybox.
RELAY_IP = ''
UR_PORT = 9400 
RELAY_ADDR = (RELAY_IP, UR_PORT)

TELLO_ADDR = ('192.168.10.1', 8889)

# Socket object 
control_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # recice udp data to client
video_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # send videofeed to user
state_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # send state info to user
control_udp.bind(RELAY_ADDR)

tello = tello.Tello() # access the tello libary 


# sends the users control commands to the tello drone
def forward_control_cmd(data):
    data = data.decode(FORMAT)
    tello.send_command_without_return(data)
        #control_udp.sendto(data, TELLO_ADDR)

'''
# sends the tello drones videofeed to the user
def backward_videofeed(addr):
    tello.streamon()
    while True:
        video_data = tello.get_frame_read().frame
        video_udp.sendto(video_data, addr)
        
# sends state info from tello drone to the user
def backward_state(addr):
    state_data = tello.udp_state_receiver()
    video_udp.sendto(state_data, addr)
'''


        
        
        
def run_program():

    print('[RELAY BOX] Relay box is running')
    print(f'Listening for incoming connections on port {UR_PORT}...\n')
    
    tello.connect()

    while True:
        data, addr = control_udp.recvfrom(BUFFER_SIZE)
        print('\tIncoming text: {}'.format(data))  

        control_thread = threading.Thread(target=forward_control_cmd, args=(data, ))
        control_thread.start()

    '''
        video_thread = threading.Thread(target=backward_videofeed, args=(addr, ))
        video_thread.start()

        state_thread = threading.Thread(target=backward_state, args=(addr, ))
        state_thread.start()
    '''

run_program()