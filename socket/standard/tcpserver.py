from socket import *
from time import ctime

host = ''
port = 12022
buffer_size = 1024
addr = (host, port)

server = socket(AF_INET, SOCK_STREAM)
server.bind(addr)
server.listen(5)

while True:
    print('Waiting for connection...')

    client, client_addr = server.accept()
    print('...connected from :', client_addr)

    while True:
        data = client.recv(buffer_size)
        if not data:
            break
        print(data)
        client.send('[%s] %s' % (ctime(), data))

    client.close()

server.close()

print('All things done')