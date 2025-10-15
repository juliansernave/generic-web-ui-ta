from playwright.sync_api import Page, expect


def wait_visible(page: Page, selector: str, timeout: int = 5000):
    el = page.locator(selector)
    expect(el).to_be_visible(timeout=timeout)
    return el
