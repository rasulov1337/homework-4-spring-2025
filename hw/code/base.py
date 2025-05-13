import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.main_page import MainPage
from ui.pages.base_page import PageNotOpenedException


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        if self.authorize:
            credentials = request.getfixturevalue("credentials")
            driver.get(MainPage.url)
            MainPage(driver).login(*credentials)


class NoAuthCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

    def is_opened(self, url, timeout=None):
        if timeout is None:
            timeout = 7

        try:
            WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
            return True
        except:
            raise PageNotOpenedException(
                f"{url} did not open in {timeout} sec, current url {self.driver.current_url}"
            )