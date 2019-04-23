from socket import *
serverAddress = ("192.168.1.112",12000) # a tuple containing the IP Address of the Server and Socket ID (Port)
clientSocket = socket(AF_INET,SOCK_DGRAM)# Datagram because we're using UDP
message = input("Input command: ")
clientSocket.sendto(message.encode(),serverAddress)
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()