'''
    Handling POST requests
'''

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

import html

class FormPage(Resource):
    isleaf = True
    def render_GET(self, request):
        return str.encode(" \
        <html> \
            <body> \
                <form method='POST'> \
                <input name='form-field' type='text' /> \
                <input type='submit' /> \
                </form> \
            </body> \
        </html> \
    ")

    def render_POST(self, request):
        return str.encode("""
        <html><body>You submitted %s</body></html>
        """ % (html.escape(request.args[str.encode("form-field")][0].decode()),))
root = Resource()
root.putChild(str.encode("form"), FormPage())
factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()