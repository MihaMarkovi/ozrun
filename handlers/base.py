import os
import uuid

from google.appengine.api import memcache
from google.appengine.api import users
import jinja2
import webapp2

from models.user import User

template_dir = os.path.join(os.path.dirname(__file__), "../templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):

        if not params:
            params = {}

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

    def render_template_with_csrf(self, view_filename, params=None):
        if not params:
            params = {}

        csrf_token = str(uuid.uuid4())  # convert UUID to string
        memcache.add(key=csrf_token, value=True, time=600)
        params["csrf_token"] = csrf_token

        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("base.html")

class EnMainHandler(BaseHandler):
    def get(self):
        return self.render_template("en_base.html")


class ThanksHandler(BaseHandler):
    def get(self):
        return self.render_template("thanks.html")

class AdminHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()

        admin = users.is_current_user_admin()

        seznam_3_km = User.query(User.category == "3 km", User.deleted == False).order().fetch()
        seznam_6_km = User.query(User.category == "6 km", User.deleted == False).order().fetch()
        seznam_9_km = User.query(User.category == "9 km", User.deleted == False).order().fetch()

        if admin:
            logiran = True
            logout_url = users.create_logout_url(self.request.uri)

            params = {"seznam_3_km": seznam_3_km, "seznam_6_km": seznam_6_km, "seznam_9_km": seznam_9_km, "logiran": logiran, "logout_url": logout_url, "user": user}
        else:
            logiran = False
            login_url = users.create_login_url(self.request.uri)

            params = {"seznam_3_km": seznam_3_km, "seznam_6_km": seznam_6_km, "seznam_9_km": seznam_9_km, "logiran": logiran, "login_url": login_url, "user": user, "admin": admin}

        return self.render_template("admin.html", params=params)

class TrashHandler(BaseHandler):
    def get(self):
        seznam = User.query(User.deleted == True).order().fetch()
        params = {"seznam": seznam}
        return self.render_template("smeti.html", params=params)