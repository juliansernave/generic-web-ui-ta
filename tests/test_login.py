from services.user_flows import login_flow


def test_valid_login(page):
    inv = login_flow(page, "standard_user", "secret_sauce")
    assert inv.item_count() > 0
