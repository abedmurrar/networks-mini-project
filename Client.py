# from socket import *
# serverAddress = ("82.205.79.78",12000) # a tuple containing the IP Address of the Server and Socket ID (Port)
# clientSocket = socket(AF_INET,SOCK_DGRAM)# Datagram because we're using UDP
# message = input("input lower case sentence: ")
# clientSocket.sendto(message.encode(),serverAddress)
# modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
# print(modifiedMessage.decode())
# clientSocket.close()