'''
    Use of resources to create a calendar website
'''

from twisted.internet import reactor
from twisted.web.resource import Resource, NoResource
from twisted.web.server import Site

from calendar import calendar

