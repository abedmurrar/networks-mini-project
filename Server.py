from socket import *
from os import listdir
from os.path import isfile, join

serverAddress = ("192.168.1.112",12000) # a tuple containing the IP Address of the Server and Socket ID (Port)
serverSocket = socket(AF_INET,SOCK_DGRAM) # Datagram because we're using UDP
serverSocket.bind(serverAddress)
print('starting up on %s port %s' % serverAddress) # debug
while True:
    message, clientAddress = serverSocket.recvfrom(2048)     
    modifiedMessasge = message.decode()
    if modifiedMessasge is 'ls':
        print(modifiedMessasge+" from %s port %s"%clientAddress) # debug
        onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]
        serverSocket.sendto(str(onlyfiles),clientAddress)
    else:
        serverSocket.sendto("Incorrect command",clientAddress)

