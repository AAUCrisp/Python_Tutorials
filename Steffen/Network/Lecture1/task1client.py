from socket import *

# SERVER_IP = "127.0.0.1"
SERVER_IP = "192.168.1.208"
SERVER_PORT = 19999
BUFFER_SIZE = 1024

s = socket(AF_INET, SOCK_DGRAM)     # IPv4 , UDP

s.sendto(bytes('Hello there. My name is Bamse',
               'utf-8'), (SERVER_IP, SERVER_PORT))
print("Data sent.")

#Receive answer from server
data = s.recvfrom(BUFFER_SIZE)
print(format(data))
print('Done')
