import socket
# mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))



mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET /romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()


mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('liucs.liu-cscs.repl.co',80))
cmd = 'GET /calendar HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://liucs.liu-cscs.repl.co/home')
for line in fhand:
    print(line.decode().strip())