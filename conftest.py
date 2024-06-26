import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Set default viewport
    """
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


def pytest_configure():
    """
    Instantiate global variables
    """
    pytest.url = ""
