from socket import *

#SERVER_IP = "127.0.0.1"
SERVER_IP = "192.168.1.208"
SERVER_PORT = 8888
BUFFER_SIZE = 1024

s = socket(AF_INET,SOCK_STREAM)
s.connect((SERVER_IP, SERVER_PORT))

s.send(bytes("Hello there. My name is ME!",'utf-8'))
print("Data sent.")
data = s.recv(BUFFER_SIZE)
print('Received data: {}'.format(data))
