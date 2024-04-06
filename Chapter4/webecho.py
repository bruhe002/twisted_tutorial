'''
    A File to simulate an HTTP server using 
    Twisted Networking class functions
'''

from twisted.protocols import basic
from twisted.internet import protocol, reactor

class HTTPEchoProtocol(basic.LineReceiver):
    def __init__(self):
        self.lines = []

    def lineReceived(self, line):
        # Add Line to self.lines
        self.lines.append(line)
        # If no lines left, send response
        if not line:
            self.sendResponse()

    def sendResponse(self):
        self.sendLine("HTTP/1.1 200 OK")
        self.sendLine("")
        responseBody = "You said:\r\n\r\n" + "\r\n".join(self.lines)
        self.transport.write(responseBody)
        self.transport.loseConnection()
        