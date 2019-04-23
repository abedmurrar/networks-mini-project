# from socket import *
# serverAddress = ("25.66.140.253",12000) # a tuple containing the IP Address of the Server and Socket ID (Port)
# serverSocket = socket(AF_INET,SOCK_DGRAM) # Datagram because we're using UDP
# serverSocket.bind(serverAddress)
# print('starting up on %s port %s' % serverAddress)
# while True:
#     message, clientAddress = serverSocket.recvfrom(2048)
#     modifiedMessasge = message.decode().upper()
#     if modifiedMessasge:
#         print(modifiedMessasge+" from %s port %s"%clientAddress)
#     serverSocket.sendto(modifiedMessasge.encode(),clientAddress)

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]
