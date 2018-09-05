from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

host = ''
port = 21567
addr = (host, port)


class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

server = TCP(addr, MyRequestHandler)

print('waiting for connection...')
server.serve_forever()