import pytest

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


# pytest-playwright provides fixtures: browser, context, page
# We just ensure base URL navigation is fast via helper if needed.
