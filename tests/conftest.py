import os
from pathlib import Path

import allure
import pytest
from playwright.sync_api import Page

from config.settings import settings


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": settings.headless,
        "args": ["--start-maximized"],
    }


@pytest.fixture(scope="session")
def context_kwargs():
    return {"viewport": None}  # use full size


# Allure environment configuration
@pytest.fixture(scope="session", autouse=True)
def configure_allure_environment(request):
    """Write environment information to Allure report"""
    allure_results_dir = Path("allure-results")
    allure_results_dir.mkdir(exist_ok=True)

    environment_properties = {
        "Base URL": settings.base_url,
        "Browser": os.getenv("BROWSER", "chromium"),
        "Headless": str(settings.headless),
        "Python Version": f"{request.config.cache.get('cache/nodeids', [''])[0].split('::')[0]}",
        "Test Environment": os.getenv("TEST_ENV", "development"),
    }

    # Write environment.properties for Allure
    with open(allure_results_dir / "environment.properties", "w") as f:
        for key, value in environment_properties.items():
            f.write(f"{key}={value}\n")


# Allure screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach screenshot to Allure report on test failure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Check if the test has a 'page' fixture
        if "page" in item.funcargs:
            page: Page = item.funcargs["page"]
            try:
                # Take screenshot
                screenshot_bytes = page.screenshot(full_page=True)
                allure.attach(
                    screenshot_bytes,
                    name=f"screenshot_{item.name}",
                    attachment_type=allure.attachment_type.PNG,
                )

                # Attach page HTML
                html_content = page.content()
                allure.attach(
                    html_content,
                    name=f"page_html_{item.name}",
                    attachment_type=allure.attachment_type.HTML,
                )

                # Attach page URL
                allure.attach(
                    page.url,
                    name="page_url",
                    attachment_type=allure.attachment_type.TEXT,
                )
            except Exception as e:
                allure.attach(
                    str(e),
                    name="screenshot_error",
                    attachment_type=allure.attachment_type.TEXT,
                )


# pytest-playwright provides fixtures: browser, context, page
# We just ensure base URL navigation is fast via helper if needed.
