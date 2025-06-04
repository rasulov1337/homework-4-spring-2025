import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page_functionality import BasePageFunctionality
from ui.locators.base_page_locators import BasePageLocators

from functools import wraps


class PageNotOpenedException(Exception):
    pass


class BasePage(BasePageFunctionality):
    url = "https://ads.vk.com/"
    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedException(
            f"{self.url} did not open in {timeout} sec, current url {self.driver.current_url}"
        )

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_visibility(self, locator, timeout=None):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    def find_all(self, locator, timeout=None) -> list[WebElement]:
        return self.wait(timeout).until(EC.visibility_of_all_elements_located(locator))

    def find_all_presence(self, locator, timeout=None) -> list[WebElement]:
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def find_interactable(self, locator, timeout=None):
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def clear(self, locator, timeout: float | None = None) -> WebElement:
        elem = self.find(locator, timeout)
        # elem.clear()

        if elem.get_attribute("value") != "":
            size = len(elem.get_attribute("value"))
            elem.send_keys(size * Keys.BACKSPACE)

        return elem

    def fill(self, locator, keys):
        self.find(locator).send_keys(keys)

    def fill_in(self, locator, query: str, timeout: float | None = None) -> WebElement:
        elem = self.clear(locator, timeout)
        elem.send_keys(query)
        return elem

    def find_invisible(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def is_visible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def scroll_click(self, locator, timeout=5) -> WebElement:
        self.find(locator, timeout=timeout)
        self.wait(timeout).until(EC.visibility_of_element_located(locator))
        elem: WebElement = self.wait(timeout).until(EC.element_to_be_clickable(locator))

        self.wait(timeout).until(element_in_viewport(locator))

        elem.click()

        return elem

    def unfocus(self):
        self.driver.execute_script("document.activeElement.blur()")

    def go_to_new_tab(self):
        handles = self.driver.window_handles
        assert len(handles) > 1
        self.driver.switch_to.window(handles[1])

    def scroll_and_click(self, locator, timeout=None) -> WebElement:
        elem = self.wait(timeout).until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        return elem

    def became_visible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def became_invisible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def hover(self, locator, timeout=5):
        elem = self.wait(timeout).until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(elem).perform()

    def fill_field(self, field, value):
        elem = self.find(field)
        elem.clear()
        elem.send_keys(value)

    def modal_active(self):
        return len(self.find_all(self.locators.CURRENT_MODAL)) > 0


class PageWithView(BasePageFunctionality):
    url = ""

    def open_view(self, button_open_locator, sign_opening_locator):
        self.click(button_open_locator)
        self.find_with_check_visibility(sign_opening_locator)

    def close_view(self, button_close_locator, sign_opening_locator):
        self.click(button_close_locator)
        self.find(sign_opening_locator, until_EC=EC.invisibility_of_element_located)


# add_open_view add method open_view() to button by locator
def add_open_view(sign_opening_locator):
    def add_open_view_decorator(elem_getter):
        @wraps(elem_getter)
        def functionality(self, *args, **kwargs):
            openable_elem_result = elem_getter(self, *args, **kwargs)

            def open_view():
                return self.open_view(
                    openable_elem_result, sign_opening_locator=sign_opening_locator
                )

            openable_elem_result.open_view = open_view

            return openable_elem_result

        return functionality

    return add_open_view_decorator


class element_in_viewport(object):
    def __init__(self, locator: tuple[str, str]):
        self.locator = locator

    def __call__(self, driver):
        script = """
                    var elem = arguments[0],
                    box = elem.getBoundingClientRect(),
                    cx = box.left + box.width / 2,
                    cy = box.top + box.height / 2,
                    e = document.elementFromPoint(cx, cy);
                    for (; e; e = e.parentElement) {
                    if (e === elem)
                      return true;
                    }
                    return false;
                """

        elem = driver.find_element(*self.locator)
        return driver.execute_script(script, elem)
