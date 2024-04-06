'''
    Usage of Site class to serve up a 
    site directory for the files in
    a local directory
'''

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

resource = File('/c/Users/bruhe/Documents/twisted_tutorial/Chapter4/resources')
factory = Site(resource)

reactor.listenTCP(8000, factory)
reactor.run()