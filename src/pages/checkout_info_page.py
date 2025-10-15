from __future__ import annotations

from core.builder import CheckoutInfo  # ajusta a tu ruta real

from .base_page import BasePage


class CheckoutInfoPage(BasePage):
    _first = "[data-test='firstName']"
    _last = "[data-test='lastName']"
    _zip = "[data-test='postalCode']"
    _continue = "[data-test='continue']"

    def fill_info_and_continue(self, info: CheckoutInfo) -> None:
        self.page.fill(self._first, info.first_name)
        self.page.fill(self._last, info.last_name)
        self.page.fill(self._zip, info.postal_code)
        self.page.click(self._continue)
