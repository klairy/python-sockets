from socket import *
import time


def startSend(port):
    # send the message, thread 2
    try:
        serverAddr = "127.0.0.1"
        client = socket(AF_INET, SOCK_STREAM)
        print("Welcome to the chatting room!")


        while 1:
            client.connect((serverAddr, port))
            info = input()
            info = 'Your friend: ' + info

            client.send(info.encode())

            if info == 'stop':
                break

            time.sleep(0.5)
            client.close()

    except IOError as e:
        print(e)

startSend(4444)