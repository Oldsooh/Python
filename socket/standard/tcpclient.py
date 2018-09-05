from socket import *
from time import ctime

host = 'localhost'
port = 12022
buffer_size = 1024
addr = (host, port)

client = socket(AF_INET, SOCK_STREAM)
client.connect(addr)

while True:
    data = raw_input('> ')
    if not data:
        break
    client.send(data)

    data = client.recv(buffer_size)
    if not data:
        break
    print(data)

client.close()

print('All things done')