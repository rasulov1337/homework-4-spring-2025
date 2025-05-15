from ui.fixtures import *
from os import environ
import pytest
import os


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://ads.vk.com/")
    parser.addoption("--debug_log", action="store_true")
    parser.addoption("--selenoid", action="store_true")
    parser.addoption("--vnc", action="store_true")


@pytest.fixture(scope="session")
def config(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    debug_log = request.config.getoption("--debug_log")

    base_dir = os.path.dirname(os.path.abspath(__file__))

    users_list_path = environ.get(
        "USERS_LIST_PATH", os.path.join(base_dir, "files", "email.txt")
    )

    keywords_path = environ.get(
        "KEYWORDS_PATH", os.path.join(base_dir, "files", "keywords.txt")
    )

    return {
        "browser": browser,
        "url": url,
        "debug_log": debug_log,
        "selenoid": None,
        "vnc": False,
        "users_list_path": os.path.abspath(users_list_path),
        "keywords_path": os.path.abspath(keywords_path),
    }
