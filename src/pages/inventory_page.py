from playwright.sync_api import expect

from .base_page import BasePage


class InventoryPage(BasePage):
    TITLE = ".title"
    ITEM = ".inventory_item"

    def assert_loaded(self):
        expect(self.page.locator(self.TITLE)).to_have_text("Products", timeout=self.timeout)

    def item_count(self) -> int:
        return self.page.locator(self.ITEM).count()
