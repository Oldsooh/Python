from socket import *

host = 'localhost'
port = 21567
addr = (host, port)
buffer_size = 1024

while True:
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(addr)

    data = raw_input('> ')
    if not data:
        break

    client.send('%s\r\n' % data)
    data = client.recv(buffer_size)
    if not data:
        break

    print(data)
    client.close()

print('All things done')
