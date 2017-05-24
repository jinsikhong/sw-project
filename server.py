import sys, socket

IP = "127.0.0.1"
PORT = 8888

print("start program")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = (IP, PORT)

s.bind(address)
s.listen(1)

print("start accept")
cs, caddress = s.accept()   #대기하는부분

print(caddress)

while True:
    data = cs.recv(1024)
    if not data:
        break
    cs.sendall(data)
    print("Client : %s" % data.decode())

s.close()