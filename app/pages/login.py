import allure

from locators.login import LocatorsLoginPage


class LoginPage:
    def __init__(self, app):
        self.app = app

    @allure.step("Enter username")
    def enter_username(self, username: str or None = None):
        wd = self.app.wd
        if username is None:
            username = self.app.user_email
        wd.find_element(*LocatorsLoginPage.username_input).send_keys(username)

    @allure.step("Enter password")
    def enter_password(self, password: str or None = None):
        wd = self.app.wd
        if password is None:
            password = self.app.user_password
        wd.find_element(*LocatorsLoginPage.password_input).send_keys(password)

    @allure.step("Click submit button")
    def click_submit_btn(self):
        wd = self.app.wd
        wd.find_element(*LocatorsLoginPage.submit_button).click()
