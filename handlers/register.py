from handlers.base import BaseHandler
from models.user import User


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
        seznam_3_km = User.query(User.category == "3 km", User.deleted == False).order().fetch()
        seznam_6_km = User.query(User.category == "6 km", User.deleted == False).order().fetch()
        seznam_9_km = User.query(User.category == "9 km", User.deleted == False).order().fetch()

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
