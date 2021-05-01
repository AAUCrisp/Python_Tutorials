import socket

bufferSize = 2048
y_Port = 9999
y_Server = 'localhost' 
y_Addr = (y_Server, y_Port)
forMat = 'utf-8'

z_Port = 9400
z_Server = 'localhost'#socket.gethostbyname(socket.gethostname())
z_Addr = (z_Server, z_Port)

y_ServerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
z_ClientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
y_ServerSock.bind(y_Addr)

print("Server Y up and running...")
print("Listening for messages from X-client in port"+str(y_Port))

def receiveRelayFromX():
    while True:
        bytesAddressPair = y_ServerSock.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        #address = bytesAddressPair[1]
        clientMsg = "{}".format(message)
        #clientIP  = "Client IP Address:{}".format(address)
        print(clientMsg)
        #print(clientIP)
        bytesToSend = str.encode(clientMsg)
        z_ClientSock.sendto(bytesToSend, z_Addr)
        print("The message "+clientMsg +"has been relayed to the Z-server!")


receiveRelayFromX()