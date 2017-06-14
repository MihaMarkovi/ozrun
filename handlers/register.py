from handlers.base import BaseHandler
from models.user import User
from utils.decorators import validate_csrf


class PrijavaCreateHandler(BaseHandler):
    def get(self):
        return self.render_template_with_csrf("prijava.html")

    @validate_csrf
    def post(self):
        name = self.request.get("ime")
        surname = self.request.get("prezime")
        sex = self.request.get("spol")
        country = self.request.get("drzava")
        club = self.request.get("klub")

        User.create(ime=name, prezime=surname, spol=sex, drzava=country, klub=club)

        return self.redirect_to("thanks-page")

