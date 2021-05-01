import socket
import threading

host = 'localhost'
port = 9400        
addr = (host, port)
bufferSize = 2048  
forMat = 'utf-8'

serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Creating socket
serverSock.bind(addr)    # Bind socket to the address

print('Z server is up and running...')
print('Listening for relayed datagrams in port '+str(port))

def receiveMessage():
    bytesAddressPair = serverSock.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    #address = bytesAddressPair[1]
    clientMsg = "Y is relaying the following message from X: {}".format(message)
    #clientIP  = "Client IP Address:{}".format(address)
    print(clientMsg)
    #print(clientIP)
  

while True:
    receiveMessage()
   
