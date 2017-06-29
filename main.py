#!/usr/bin/env python
import webapp2

from handlers.base import MainHandler, EnMainHandler, ThanksHandler, AdminHandler, TrashHandler
from handlers.register import PrijavaCreateHandler, UsersAllHandler, UserDeleteHandler, UserEditHandler, \
    UserReviveHandler, UserFinallyDelete

app = webapp2.WSGIApplication([
    # main pages
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/en', EnMainHandler, name="en-main-page"),

    # prijava
    webapp2.Route('/prijava', PrijavaCreateHandler, name='prijava-main'),
    webapp2.Route('/zahvala', ThanksHandler, name='zahvala-page'),
    webapp2.Route('/svi_trkaci', UsersAllHandler, name='svi-trkaci'),

    # admin pages
    webapp2.Route('/admin', AdminHandler, name='admin-page'),
    webapp2.Route('/admin/user/<user_id:(\d+)>/delete', UserDeleteHandler, name="user-delete"),
    webapp2.Route('/admin/user/<user_id:(\d+)>/edit', UserEditHandler, name="user-edit"),
    webapp2.Route('/admin/user/<user_id:(\d+)>/revive', UserReviveHandler, name="user-revive"),
    webapp2.Route('/admin/user/<user_id:(\d+)>/finally_delete', UserFinallyDelete, name="user-finally-delete"),
    webapp2.Route('/admin/091256387/smece', TrashHandler, name="trash-page"),
], debug=True)
