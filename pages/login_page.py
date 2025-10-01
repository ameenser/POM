from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")
    HEADER_LABEL = (By.CLASS_NAME, "header_label")
    def open_login(self, base_url):
        self.open(base_url)


    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_header_label(self):
        return self.get_text(self.HEADER_LABEL)

    def get_error_msg(self):
        return self.get_text(self.ERROR_MSG)