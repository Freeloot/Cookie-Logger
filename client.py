import socket
import requests
  
r = requests.get('http://google.com')
  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostname()
PORT = 1234

s.bind((IP, PORT))
s.listen(5)

while True:
	clientsocket, addr = s.accept()
	print(f"Connection from {addr} has been established!")
	for c in r.cookies:
		clientsocket.send(bytes(f"{c.value}", "utf-8"))
	clientsocket.close()
