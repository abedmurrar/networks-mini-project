from socket import *
serverAddress = ("192.168.1.111",12000) # a tuple containing the IP Address of the Server and Socket ID (Port)
clientSocket = socket(AF_INET,SOCK_DGRAM)# Datagram because we're using UDP
command = input("Input command: ")
clientSocket.sendto(command.encode(),serverAddress)
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
file_name = input("Which file do you want? ")
clientSocket.sendto(file_name.encode(),serverAddress)
file_content, s= clientSocket.recvfrom(2048)
modifiedContent = file_content.decode()
print(modifiedContent)
clientSocket.close()