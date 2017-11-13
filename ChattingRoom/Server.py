from socket import *

userlist = {'user1': '6666', 'user2': '7777', 'user3': '5555'}

serverAddr = "127.0.0.1"
serverPort = 4444

server = socket(AF_INET, SOCK_STREAM)
server.bind((serverAddr, serverPort))
server.listen(4)
print("Ready to server......")

while 1:
	try:
		# receive from sender (user2)
		client, addr = server.accept()
		info = client.recv(1024).decode()
		print("From " + str(addr) + ": " + info)

		# parse received test
		info = info.split(':')
		text = info.pop()
		sender, receiver = info[0].split()

		# reformat message
		text = sender + ': ' + text

		# TODO : could be extend for specific transmit
		# sender gives port, dest and message
		# which could be parsed on the server,
		# but this could cause flooding if client number is huge
		# for multiple users, use publisher-subscriber pattern to manage

		# send message to destination (user1)
		destAddr = "127.0.0.1"
		dest = socket(AF_INET, SOCK_STREAM)
		dest.connect((destAddr, int(userlist[receiver])))
		dest.send(text.encode())
		dest.close()

		client.close()

	except OSError as e:
		print(e)
	except IOError as e:
		print(e)