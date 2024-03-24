from twisted.internet.protocol import Factory
from twisted.internet import reactor, protocol

class QuoteProtocol(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numConnections += 1

    def dataReceived(self, data):
        print("Number of connections: %d" % (self.factory.numConnections))
        print("> Received: \"%s\"\n> Sending: \"%s\"" % (data, self.getQuote()))
        self.transport.write(self.getQuote())
        self.updateQuote(data)