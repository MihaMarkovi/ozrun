from google.appengine.ext import ndb

class User(ndb.Model):
    name = ndb.StringProperty()
    surname = ndb.StringProperty()
    sex = ndb.StringProperty()
    category = ndb.StringProperty()
    country = ndb.StringProperty()
    club = ndb.StringProperty()
    deleted = ndb.BooleanProperty(default=False)
    broj = ndb.StringProperty()

    @classmethod
    def create(cls, ime, prezime, spol, kategorija, drzava, klub):
        new_user = User(name=ime, surname=prezime, sex=spol, category=kategorija, country=drzava, club=klub)
        new_user.put()

        return new_user