import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .ui.pages.base_page import PageNotOpenedException

class NoAuthCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

    def is_opened(self, url, timeout=None, check_new_tab=False):
        if timeout is None:
            timeout = 7

        if check_new_tab:
            original_window = self.driver.current_window_handle

            WebDriverWait(self.driver, timeout).until(
                lambda d: len(d.window_handles) > 1
            )

            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break

        try:
            WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
            return True
        except:
            if check_new_tab:
                self.driver.switch_to.window(original_window)
            raise PageNotOpenedException(
                f"{url} did not open in {timeout} sec, current url {self.driver.current_url}"
            )