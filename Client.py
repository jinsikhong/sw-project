import sys, socket

IP = "127.0.0.1"
PORT = 8888

print("start client")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

saddress = (IP, PORT)
s.connect(saddress)

while True:
    msg = input()
    s.sendall(msg.encode())
    data = s.recv(1024)
    print("Data from server : %s" % data.decode())

s.close()