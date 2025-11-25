import allure


@allure.epic("Smoke Tests")
@allure.feature("Application Availability")
@allure.story("Homepage Accessibility")
@allure.title("Verify homepage loads successfully")
@allure.description(
    """
This smoke test verifies that the application homepage loads correctly.
It checks:
- The page is accessible
- The page title contains expected text
"""
)
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "health-check")
def test_homepage_loads(page):
    """Smoke test to verify the homepage loads correctly"""

    with allure.step("Navigate to homepage"):
        page.goto("https://www.saucedemo.com")
        allure.attach(page.url, name="Page URL", attachment_type=allure.attachment_type.URI_LIST)

    with allure.step("Verify page title contains 'swag'"):
        title = page.title()
        allure.attach(title, name="Page Title", attachment_type=allure.attachment_type.TEXT)
        assert title.lower().find("swag") >= 0, f"Expected 'swag' in title, but got: {title}"
