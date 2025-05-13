from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://ads.vk.com/')
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--selenoid', action='store_true')
    parser.addoption('--vnc', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')

    users_list_path = environ.get("USERS_LIST_PATH", "D:/Github/homework-selenium-2024-autumn/hw/code/files/emails.txt")
    keywords_path = environ.get("KEYWORDS_PATH", "D:/Github/homework-selenium-2024-autumn/hw/code/files/keywords.txt")

    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
        'selenoid': None,
        'vnc': False,
        'users_list_path': users_list_path,
        'keywords_path': keywords_path
    }