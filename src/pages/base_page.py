from playwright.sync_api import Page

from config.settings import settings


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = settings.base_url
        self.timeout = settings.default_timeout_ms

    def goto(self, path: str = "/"):
        self.page.goto(self.base_url + path)
