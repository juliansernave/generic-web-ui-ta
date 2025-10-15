from core.wait_strategies import wait_visible

from .base_page import BasePage


class LoginPage(BasePage):
    USER = "#user-name"
    PASS = "#password"
    BTN = "#login-button"

    def open(self):
        self.goto("/")

    def login_as(self, username: str, password: str):
        wait_visible(self.page, self.USER, self.timeout).fill(username)
        self.page.locator(self.PASS).fill(password)
        self.page.locator(self.BTN).click()
