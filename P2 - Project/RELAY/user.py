from socket import *
import time

SERVER_IP = "192.168.10.2"
SERVER_PORT = 9400
BUFFER_SIZE = 2048

s = socket(AF_INET,SOCK_DGRAM)



s.sendto(bytes('takeoff','utf-8'),(SERVER_IP,SERVER_PORT))
print("Data sent.")

time.sleep(5000)

while True:
s.sendto(bytes('land','utf-8'),(SERVER_IP,SERVER_PORT))
