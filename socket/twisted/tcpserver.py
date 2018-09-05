from twisted.internet import protocol, reactor
from time import ctime

port = 21567


class TSServerProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from:', clnt)

    def dataReceived(self, data):
        print(data)
        self.transport.write('[%s] %s' % (ctime(), data))

    
factory = protocol.Factory()
factory.protocol = TSServerProtocol

print('Waiting for connection...')
reactor.listenTCP(port, factory)

reactor.run()

print('All things done')