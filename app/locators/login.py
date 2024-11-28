from selenium.webdriver.common.by import By

class LocatorsLoginPage:
    username_input = (By.XPATH, "//input[@id='username']")
    password_input = (By.XPATH, "//input[@id='password']")
    submit_button = (By.XPATH, "//button[@id='submit']")