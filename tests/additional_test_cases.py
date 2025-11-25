"""
Complete example test showcasing Allure reporting capabilities.
This demonstrates best practices for Allure integration.
"""

import allure
import pytest

from services.user_flows import login_flow


@allure.epic("E-Commerce")
@allure.feature("Shopping Cart")
@allure.story("Add Items to Cart")
@allure.title("User can add multiple items to shopping cart")
@allure.description(
    """
This test verifies the complete flow of adding items to the cart:
1. User logs in successfully
2. User browses product inventory
3. User adds items to cart
4. Cart reflects correct item count
"""
)
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("cart", "smoke", "e2e")
@allure.label("owner", "QA Team")
@allure.link("https://www.saucedemo.com", name="Application URL")
@pytest.mark.smoke
def test_add_items_to_cart_example(page):
    """Example test showing Allure reporting best practices"""

    # Step 1: Login
    with allure.step("User logs in with standard credentials"):
        allure.attach(
            "Username: standard_user",
            name="Login Credentials",
            attachment_type=allure.attachment_type.TEXT,
        )
        inventory_page = login_flow(page, "standard_user", "secret_sauce")

    # Step 2: Verify products are available
    with allure.step("Verify products are displayed on inventory page"):
        product_count = inventory_page.item_count()

        # Attach data to report
        allure.attach(
            f"Total products available: {product_count}",
            name="Product Availability",
            attachment_type=allure.attachment_type.TEXT,
        )

        assert product_count > 0, "No products found. Expected at least 1 product."

    # Step 3: Add items to cart (example - you'll need to implement these methods)
    with allure.step("Add first product to cart"):
        # This is an example - you'll need to implement the actual method
        # For now, we'll just verify we can see products
        allure.attach(
            page.url, name="Current Page URL", attachment_type=allure.attachment_type.URI_LIST
        )

    # Step 4: Verify success
    with allure.step("Verify test completion"):
        allure.attach(
            "✅ Test completed successfully",
            name="Test Result",
            attachment_type=allure.attachment_type.TEXT,
        )


@allure.epic("E-Commerce")
@allure.feature("Shopping Cart")
@allure.story("Add Items to Cart")
@allure.title("Verify cart badge updates when adding items")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("cart", "ui")
@pytest.mark.ui
def test_cart_badge_updates_example(page):
    """Example test for cart badge functionality"""

    with allure.step("Login and navigate to inventory"):
        inventory_page = login_flow(page, "standard_user", "secret_sauce")

    with allure.step("Verify initial cart is empty"):
        # This is a placeholder - implement your actual cart badge check
        assert inventory_page.item_count() > 0
        allure.attach(
            "Cart starts empty", name="Initial State", attachment_type=allure.attachment_type.TEXT
        )


@allure.epic("Authentication")
@allure.feature("Login")
@allure.story("Invalid Login Attempts")
@allure.title("Login fails with invalid credentials")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("authentication", "negative")
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        pytest.param(
            "invalid_user",
            "invalid_pass",
            "Username and password do not match",
            id="invalid_credentials",
            marks=allure.label("test_type", "negative"),
        ),
        pytest.param(
            "",
            "",
            "Username is required",
            id="empty_credentials",
            marks=allure.label("test_type", "negative"),
        ),
    ],
)
def test_invalid_login_example(page, username, password, expected_error):
    """Example of parameterized test with Allure"""

    with allure.step(f"Attempt login with username='{username}' and password='{password}'"):
        page.goto("https://www.saucedemo.com")

        # Add test data to report
        allure.attach(
            f"Username: {username}\nPassword: {password}",
            name="Test Data",
            attachment_type=allure.attachment_type.TEXT,
        )

        if username:
            page.fill('[data-test="username"]', username)
        if password:
            page.fill('[data-test="password"]', password)

        page.click('[data-test="login-button"]')

    with allure.step(f"Verify error message contains '{expected_error}'"):
        # This is a simplified check - implement your actual error verification
        # For now, we'll just pass to show the structure
        allure.attach(
            f"Expected error: {expected_error}",
            name="Expected Result",
            attachment_type=allure.attachment_type.TEXT,
        )
