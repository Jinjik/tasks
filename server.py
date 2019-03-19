import socket
scok = socket.socket()
scok.bind(('', 8080))
scok.listen(1)
c, addr = scok.accept()
print('connect', addr)
while True:
        data = c.recv(1024)
        print(data)
        if not data:
                break
        c.send(data.upper())
c.close()
                
