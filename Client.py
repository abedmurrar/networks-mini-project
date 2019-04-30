from socket import *
serverAddress = ("127.0.0.1",12000) # a tuple containing the IP Address of the Server and Socket ID (Port)
clientSocket = socket(AF_INET,SOCK_DGRAM)# Datagram because we're using UDP
choice = input("1) Get list of files\n2) Get file content\n")
if choice == '1':
    # command = input("Input command: ")
    clientSocket.sendto("ls".encode(),serverAddress)
    modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
elif choice == '2':
    file_name = input("Which file do you want? ")
    clientSocket.sendto(file_name.encode(),serverAddress)
    file_content, s= clientSocket.recvfrom(2048)
    modifiedContent = file_content.decode()
    print(modifiedContent)
else:
    print("Wrong entry!")
clientSocket.close()