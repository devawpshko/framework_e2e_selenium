from pages.login import LoginPage
from pages.main import MainPage


class Pages:

    def __init__(self, app):
        self.main = MainPage(app)
        self.login = LoginPage(app)