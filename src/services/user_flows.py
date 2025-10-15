from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def login_flow(page: Page, username: str, password: str) -> InventoryPage:
    lp = LoginPage(page)
    lp.open()
    lp.login_as(username, password)
    inv = InventoryPage(page)
    inv.assert_loaded()
    return inv
