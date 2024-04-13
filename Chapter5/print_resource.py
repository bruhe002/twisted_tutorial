'''
    Shows the advantages of getPage*

    *Deprecated in newer versions of Twisted
'''
from twisted.internet import reactor
from twisted.web.client import downloadPage
import sys

# callbacks for the deferred object
def printPage(result):
    print(result)

def printError(failure):
    print(sys.stderr, failure)

def stop(result):
    reactor.stop()

if len(sys.argv) != 2:
    print(sys.stderr, "Usage: python print_resource.py <URL>")
    exit(1)

# Get page returns a deferred object
d = getPage(sys.argv[1])
d.addCallbacks(printPage, printError)
d.addBoth(stop)

reactor.run()