from socket import *
import threading

def startRecv(port):
    serverAddr = "127.0.0.1"

    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind((serverAddr, port))

    serverSocket.listen(1)

    # receive the message, thread 1
    client, address = serverSocket.accept()
    while 1:

        info = client.recv(1024)
        info = info.decode()

        if info == "stop":
            print("Client exited.")
            break

        print(info)

    client.close()
    serverSocket.close()


startRecv(8888)