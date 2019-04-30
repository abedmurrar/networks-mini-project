from socket import *
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('./files') if isfile(join('./files', f))]

serverAddress = ("127.0.0.1",12000) # a tuple containing the IP Address of the Server and Socket ID (Port)
serverSocket = socket(AF_INET,SOCK_DGRAM) # Datagram because we're using UDP
serverSocket.bind(serverAddress)
print('starting up on %s port %s' % serverAddress) # debug
while True:
    message, clientAddress = serverSocket.recvfrom(2048) 
    modifiedMessasge = message.decode()
    print(modifiedMessasge+" from %s port %s"%clientAddress) # debug
    if modifiedMessasge == 'ls':
        serverSocket.sendto("\n".join(onlyfiles).encode(),clientAddress)
    elif modifiedMessasge in onlyfiles:
        data=''
        with open('./files/'+modifiedMessasge, 'r') as file:
            data = file.read()
        serverSocket.sendto(data.encode(),clientAddress)
    else:
        serverSocket.sendto("File not found".encode(),clientAddress)

    modifiedMessasge = message