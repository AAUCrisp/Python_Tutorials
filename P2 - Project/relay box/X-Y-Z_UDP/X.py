import socket

port = 9400
bufferSize = 2048
forMat = 'utf-8'
host = '192.168.1.113'
addr = (host, port)

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


def clientSend(msgFromClient):
    bytesToSend = str(msgFromClient).encode(forMat)
    clientSocket.sendto(bytesToSend, addr)
  

while True:
    msgFromClient = input()
    clientSend(msgFromClient)
    print("The following message has been sent to Y-server: " +msgFromClient)