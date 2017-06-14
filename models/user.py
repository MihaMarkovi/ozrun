from google.appengine.ext import ndb

class User(ndb.Model):
    name = ndb.StringProperty()
    surname = ndb.StringProperty()
    sex = ndb.StringProperty()
    country = ndb.StringProperty()
    club = ndb.StringProperty(default="individualac")

    @classmethod
    def create(cls, ime, prezime, spol, drzava, klub):
        new_user = User(name=ime, surname=prezime, sex=spol, country=drzava, club=klub)
        new_user.put()

        return new_user