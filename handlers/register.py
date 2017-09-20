from handlers.base import BaseHandler
from models.user import User
from google.appengine.api import users


class PrijavaCreateHandler(BaseHandler):
    def get(self):
        return self.render_template("prijava.html")

    def post(self):
        name = self.request.get("ime")
        surname = self.request.get("prezime")
        sex = self.request.get("spol")
        category = self.request.get("kategorija")
        country = self.request.get("drzava")
        club = self.request.get("klub")

        User.create(ime=name, prezime=surname, spol=sex, kategorija=category, drzava=country, klub=club)

        return self.redirect_to("zahvala-page")


class UsersAllHandler(BaseHandler):
    def get(self):
        seznam_3_km = User.query(User.category == "3 km", User.deleted == False).order(User.updated).fetch()
        seznam_6_km = User.query(User.category == "6 km", User.deleted == False).order(User.updated).fetch()
        seznam_9_km = User.query(User.category == "9 km", User.deleted == False).order(User.updated).fetch()

        params = {'seznam_3_km': seznam_3_km, 'seznam_6_km': seznam_6_km, 'seznam_9_km': seznam_9_km}
        return self.render_template("all_users.html", params=params)


class UserDeleteHandler(BaseHandler):
    def get(self, user_id):
        user = User.get_by_id(int(user_id))
        params = {"user": user}

        return self.render_template("delete_user.html", params=params)

    def post(self, user_id):
        user = User.get_by_id(int(user_id))
        user.deleted = True
        user.put()
        return self.redirect_to("admin-page")


class UserEditHandler(BaseHandler):
    def get(self, user_id):
        user = User.get_by_id(int(user_id))
        params = {"user": user}

        return self.render_template("edit_user.html", params=params)

    def post(self, user_id):
        startni_broj = self.request.get("broj")
        user = User.get_by_id(int(user_id))
        user.broj = startni_broj
        user.put()

        return self.redirect_to("admin-page")


class UserReviveHandler(BaseHandler):
    def get(self, user_id):
        user = User.get_by_id(int(user_id))
        params = {"user": user}

        return self.render_template("povrni.html", params=params)

    def post(self, user_id):
        user = User.get_by_id(int(user_id))
        user.deleted = False
        user.put()

        return self.redirect_to("admin-page")


class UserFinallyDelete(BaseHandler):
    def get(self, user_id):
        user = User.get_by_id(int(user_id))
        params = {"user": user}

        return self.render_template("finally_delete_user.html", params=params)

    def post(self, user_id):
        user = User.get_by_id(int(user_id))
        user.key.delete()
        return self.redirect_to("trash-page")


class ResultHandler(BaseHandler):
    def get(self):

        admin = users.is_current_user_admin()

        if admin:
            logiran = True
            logout_url = users.create_logout_url(self.request.uri)

            params = {"logiran": logiran, "logout_url": logout_url, "admin": admin}
        else:
            logiran = False
            login_url = users.create_login_url(self.request.uri)

            params = {"logiran": logiran, "login_url": login_url, "admin": admin}

        return self.render_template("rezultati.html", params=params)

    def post(self):
        broj = self.request.get("broj_rezultat")
        vrjeme = self.request.get("vrjeme_rezultat")
        users = User.query(User.broj == broj).order(User.updated).fetch()
        for user in users:
            user.vrjeme = vrjeme
            user.put()

        return self.redirect_to("result-page")


class ResultUserHandler(BaseHandler):
    def get(self):
        seznam_3_km = User.query(User.category == "3 km", User.deleted == False).order(User.updated).fetch()
        seznam_6_km = User.query(User.category == "6 km", User.deleted == False).order(User.updated).fetch()
        seznam_6_len = len(seznam_6_km)
        seznam_9_km = User.query(User.category == "9 km", User.deleted == False).order(User.updated).fetch()

        params = {'seznam_3_km': seznam_3_km,"seznam_6_len": seznam_6_len, 'seznam_6_km': seznam_6_km, 'seznam_9_km': seznam_9_km}
        return self.render_template("rezultati_users.html", params=params)
