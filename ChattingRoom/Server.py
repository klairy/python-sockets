from socket import *

serverAddr = "127.0.0.1"
serverPort = 4444

server = socket(AF_INET, SOCK_STREAM)
server.bind((serverAddr, serverPort))
server.listen(4)

while 1:
    try:
        # receive from sender (user2)
        client, addr = server.accept()
        info = client.recv(1024)

        print(info.decode())

        # TODO : could be extend for specific transmit
        # sender gives port, dest and message
        # which could be parsed on the server,
        # but this could cause flooding if client number is huge

        # send message to destination (user1)
        destAddr = "127.0.0.1"
        port = 6666
        dest = socket(AF_INET, SOCK_STREAM)
        dest.connect((serverAddr, port))
        dest.send(info)
        dest.close()

        client.close()

    except OSError as e:
        print(e)
    except IOError as e:
        print(e)