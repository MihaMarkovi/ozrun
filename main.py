#!/usr/bin/env pytho
import webapp2

from handlers.base import MainHandler, EnMainHandler, ThanksHandler
from handlers.register import PrijavaCreateHandler

app = webapp2.WSGIApplication([
    # main pages
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/en', EnMainHandler, name="en-main-page"),

    #prijava
    webapp2.Route('/prijava', PrijavaCreateHandler, name='prijava-main'),
    webapp2.Route('/zahvala', ThanksHandler, name='zahvala-page')
], debug=True)
