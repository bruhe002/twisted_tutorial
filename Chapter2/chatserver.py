from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class ChatProtocol(LineReceiver):
    def __init__(self, factory):
        self.factory = factory
        self.name = None
        self.state = "REGISTER"

    def connectionMade(self):
        self.sendLine(str.encode("What's your name?"))

    def connectionLost(self, reason):
        if self.name in self.factory.users:
            del self.factory.users[self.name]
            self.broadcastMessage("%s has left the channel. " % (self.name))

    def lineReceived(self, line):
        if self.state == "REGISTER":
            self.handle_REGISTER(line)
        else:
            self.handle_CHAT(line)

    def handle_REGISTER(self, name):
        if name in self.factory.users:
            self.sendLine("Name taken, please choose another.")
            return
        
        self.sendLine(str.encode("Welcome, %s!" % (name.decode())))
        self.broadcastMessage("%s has joined the channel. " % (name.decode()))
        self.name = name
        self.factory.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):
        message = "<%s> %s" % (self.name.decode(), message.decode())
        self.broadcastMessage(message)

    def broadcastMessage(self, message):
        for name, protocol in self.factory.users.items():
            if protocol != self:
                protocol.sendLine(str.encode(message))

class ChatFactory(Factory):
    def __init__(self):
        self.users = {}

    def buildProtocol(self, addr):
        return ChatProtocol(self)
    
reactor.listenTCP(8000, ChatFactory())
reactor.run()