from __future__ import annotations

from .base_page import BasePage


class CartPage(BasePage):
    _checkout_btn = "[data-test='checkout']"

    def proceed_to_checkout(self) -> None:
        self.page.click(self._checkout_btn)
