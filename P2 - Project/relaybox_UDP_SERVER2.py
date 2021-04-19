import socket, time, platform
from threading import Thread

# Tello constans
TELLO_IP = '192.168.10.1'  # Tello IP address
CONTROL_UDP_PORT = 8889 # send and receive commands


# Local variables
HEADER = 1024

# Video stream
VS_UDP_IP = '0.0.0.0'
VS_UDP_PORT = 11111
VS_SERVER_ADDR = (VS_UDP_IP,VS_UDP_PORT)

# State stream
STATE_UDP_IP = '0.0.0.0'
STATE_UDP_PORT = 8890 # receive drone info
SS_UDP_ADDR = (STATE_UDP_IP, STATE_UDP_PORT)

# Create a UDP object
UDP_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_server.bind(SS_UDP_ADDR)
print('[LISTENING] Server is listen for incoming stats')

# UDP server
while True:
    data, addr = UDP_server.recvfrom(HEADER)
    print('Client IP Address:{}'.format(addr))
    print('State:{}'.format(data))