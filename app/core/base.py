import allure


class CommonActions:
    def __init__(self, app):
        self.app = app

    @allure.step("Open page: {url}")
    def open_page(self, url: str):
        wd = self.app.wd
        wd.get(f"{self.app.APP_URL}{url}")
