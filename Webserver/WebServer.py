from socket import *
import os.path


def start():
	serverPort = 2222

	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.bind(('127.0.0.1', serverPort))
	serverSocket.listen(1)

	# handling request
	runServer(serverSocket)


def runServer(ssocket):
	while True:
		print('Ready to serve...')

		try:
			client, addr = ssocket.accept()
			request = client.recv(512).decode()
			# parse to get the requested resource
			file = parseRequest(request)

			# send the requested resource to client
			sendFile(file, client)
			client.close()
		except ConnectionError:
			print('Error in server')
		except TypeError:
			print('Incorrect type used.')
		except IOError:
			print('Error in I/O')


def parseRequest(request):
	request = request.splitlines()
	for r in request:
		if r.startswith('GET'):
			file = r.split()[1][1:]
			return file


def sendFile(file, client):
	# if the file exists on server, send it
	# or return HTTP 404
	if os.path.exists(file):
		response = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n '
		with open(file, 'r', encoding='utf-8') as f:
			for line in f:
				response += line
		client.send(response.encode(encoding='utf-8'))
	else:
		client.send('HTTP/1.1 404 Not Found\nContent-Type: '
					'text/html; charset=utf-8 \n\n '
					'<!DOCTYPE html><html>'
					'<head><meta charset="UTF-8">'
					'<title>Not Found</title>'
					'</head><body>'
					'<p>The resource is not found on this server.'
					'</p></body></html>'.encode(encoding='utf-8'))

# start the server
start()

# use http://127.0.0.1:2222/Homepage.html to test my server
