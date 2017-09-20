from google.appengine.ext import ndb

class User(ndb.Model):
    name = ndb.StringProperty()
    surname = ndb.StringProperty()
    sex = ndb.StringProperty()
    category = ndb.StringProperty()
    country = ndb.StringProperty()
    club = ndb.StringProperty()
    created = ndb.DateProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)
    broj = ndb.StringProperty()
    vrjeme = ndb.StringProperty()

    @classmethod
    def create(cls, ime, prezime, spol, kategorija, drzava, klub):
        new_user = User(name=ime, surname=prezime, sex=spol, category=kategorija, country=drzava, club=klub)
        new_user.put()

        return new_user