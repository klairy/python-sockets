from socket import *
import threading
import time


# handles receiving message
def startRecv(port):
	serverAddr = "127.0.0.1"

	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.setblocking(False)
	serverSocket.bind((serverAddr, port))
	serverSocket.listen(1)

	while True:
		try:
			# receive the message, thread 1
			client, address = serverSocket.accept()
		except OSError as e:
			# print("Try connecting again...")
			time.sleep(0.5)
		except IOError as e:
			print(e)
		else:
			# receive message from server
			info = client.recv(1024)
			info = info.decode()

			# ask to stop
			if info == "stop":
				print("Client exited.")
				break

			# show your friend's message
			print(info)

	client.close()
	serverSocket.close()


# handles sending message
# now only support point-to-point message
def startSend(port, name):
	# send the message, thread 2
	serverAddr = "127.0.0.1"

	print("Welcome to the chatting room!\n "
		  "1. To send a message --> user: text\n "
		  "2. To exit --> enter stop and return\n")

	while 1:
		client = socket(AF_INET, SOCK_STREAM)
		# read message
		info = input()
		info = name + " " + info

		try:
			# send to server
			client.connect((serverAddr, port))
			client.send(info.encode())
			client.close()

			# ask to stop
			if info == 'stop':
				break

		except OSError as e:
			print(e)
		except IOError as e:
			print(e)


# interface for callers
def run(port1, port2, name):
	sender = threading.Thread(target=startSend, args=(port1, name, ))
	receiver = threading.Thread(target=startRecv, args=(port2,))

	receiver.start()
	sender.start()


