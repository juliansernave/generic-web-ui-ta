import allure

from services.user_flows import login_flow


@allure.epic("Authentication")
@allure.feature("Login")
@allure.story("Valid User Login")
@allure.title("Test successful login with valid credentials")
@allure.description(
    """
This test verifies that a user can successfully log in with valid credentials.
Steps:
1. Navigate to login page
2. Enter valid username and password
3. Click login button
4. Verify user is redirected to inventory page
5. Verify products are displayed
"""
)
@allure.severity(allure.severity_level.BLOCKER)
@allure.tag("smoke", "authentication", "critical-path")
def test_valid_login(page):
    """Test that a user can login successfully with valid credentials"""

    with allure.step("Login with valid credentials"):
        inv = login_flow(page, "standard_user", "secret_sauce")

    with allure.step("Verify products are displayed on inventory page"):
        product_count = inv.item_count()
        allure.attach(
            str(product_count), name="Product Count", attachment_type=allure.attachment_type.TEXT
        )
        assert product_count > 0, f"Expected products to be displayed, but found {product_count}"
