'''
    Usage of Site class to serve up a 
    site directory for the files in
    a local directory
'''

from twisted.internet import reactor, endpoints
from twisted.web.server import Site
from twisted.web.static import File

resource = File('./resources')
factory = Site(resource)

endpoint = endpoints.TCP4ServerEndpoint(reactor, 8000)
endpoint.listen(factory)
reactor.run()