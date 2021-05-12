from socket import *
import time

SERVER_IP = "192.168.10.2"
SERVER_PORT = 9400
BUFFER_SIZE = 2048

s = socket(AF_INET,SOCK_DGRAM)



s.sendto(bytes('takeoff','utf-8'),(SERVER_IP,SERVER_PORT))
print("Data sent.")



hey = 118613842 % 9091
print(hey)