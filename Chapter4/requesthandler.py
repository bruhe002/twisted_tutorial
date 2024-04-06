'''
    Parsing multiple HTTP requests
'''

from twisted.internet import reactor
from twisted.web import http

class MyRequestHandler(http.Request):
    resources = {
        '/':'<h1>Home</h1>Home Page',
        '/about':'<h1>About</h1>All About me'
    }

    def process(self):
        self.setHeader('Content-Type', 'text/html')
        if self.path.decode() in self.resources.keys():
            self.write(str.encode(self.resources[self.path.decode()]))
        else:
            self.setResponseCode(http.NOT_FOUND)
            self.write(str.encode("<h1>Not Found</h1>Sorry no such resource"))
        self.finish()

class MyHTTP(http.HTTPChannel):
    requestFactory = MyRequestHandler

class MyHTTPFactory(http.HTTPFactory):
    def buildProtocol(self, addr):
        return MyHTTP()
    
reactor.listenTCP(8000, MyHTTPFactory())
reactor.run()