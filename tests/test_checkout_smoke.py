def test_homepage_loads(page):
    page.goto("https://www.saucedemo.com")
    assert page.title().lower().find("swag") >= 0
