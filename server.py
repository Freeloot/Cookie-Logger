import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = socket.gethostname()
PORT = 1234

s.connect((IP, PORT))

full_msg = ''

while True:
	msg = s.recv(8)
	if len(msg) <= 0:
		break
	full_msg += msg.decode("utf-8")

f = open("cookies.txt", "a")
f.write(f"{full_msg}\n")
f.close()

print(full_msg)
