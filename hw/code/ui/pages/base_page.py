import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.base_page_locators import BasePageLocators


BASIC_TIMEOUT = 10


class PageNotOpenedException(Exception):
    pass


class BasePage:
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

    def wait(self, timeout=BASIC_TIMEOUT) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout=timeout)

    def find(
        self, locator, timeout=BASIC_TIMEOUT, until=EC.presence_of_element_located
    ) -> WebElement:
        return self.wait(timeout).until(until(locator))

    def find_visibility(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        return self.find(locator, timeout, until=EC.visibility_of_element_located)

    def find_all(self, locator, timeout=BASIC_TIMEOUT) -> list[WebElement]:
        return self.wait(timeout).until(EC.visibility_of_all_elements_located(locator))

    def find_all_presence(self, locator, timeout=BASIC_TIMEOUT) -> list[WebElement]:
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def find_presence(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_interactable(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    def find_invisible(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_child(
        self,
        parent,
        child_locator,
        timeout=BASIC_TIMEOUT,
        until=EC.presence_of_element_located,
    ):
        return WebDriverWait(parent, timeout).until(until(child_locator))

    def clear(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        elem = self.find(locator, timeout)
        value = elem.get_attribute("value")
        if value:
            elem.send_keys(len(value) * Keys.BACKSPACE)
        return elem

    def fill(self, locator, keys, timeout=BASIC_TIMEOUT):
        self.find(locator, timeout).send_keys(keys)

    def fill_in(self, locator, text: str, timeout=BASIC_TIMEOUT) -> WebElement:
        elem = self.clear(locator, timeout)
        elem.send_keys(text)
        return elem

    def fill_field(self, field, value):
        elem = self.find(field)
        elem.clear()
        elem.send_keys(value)

    def click(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
        return elem

    def hover(self, locator, timeout=BASIC_TIMEOUT):
        elem = self.find(locator, timeout)
        ActionChains(self.driver).move_to_element(elem).perform()

    def hover_to_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()
        return element

    def check_url(self, expected_url, timeout=BASIC_TIMEOUT):
        return self.wait(timeout).until(EC.url_matches(expected_url))

    def is_visible(self, locator, timeout=BASIC_TIMEOUT):
        try:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def became_visible(self, locator, timeout=BASIC_TIMEOUT):
        try:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def became_invisible(self, locator, timeout=BASIC_TIMEOUT):
        try:
            self.wait(timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def close_alert_if_shown(self, timeout=BASIC_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception:
            pass

    def go_to_new_tab(self):
        handles = self.driver.window_handles
        if len(handles) > 1:
            self.driver.switch_to.window(handles[1])
        else:
            raise Exception("No second tab found")

    def modal_active(self):
        return len(self.find_all(self.locators.CURRENT_MODAL)) > 0

    def get_value_from_elem(self, element):
        return element.get_attribute("value")

    def get_value(self, locator, timeout=BASIC_TIMEOUT):
        element = self.find(locator, timeout)
        return self.get_value_from_elem(element)

    def write_input_to_element(self, element, message):
        element.clear()
        element.send_keys(message)
        return element

    def write_input(self, locator, message, timeout=BASIC_TIMEOUT):
        input_element = self.find_visibility(locator, timeout)
        input_element = self.write_input_to_element(input_element, message)
        self.wait().until(EC.text_to_be_present_in_element_value(locator, message))
        return input_element

    def write_input_without_clearing(self, locator, message, timeout=BASIC_TIMEOUT):
        input_element = self.find_visibility(locator, timeout)
        input_element.send_keys(message)
        self.wait().until(EC.text_to_be_present_in_element_value(locator, message))
        return input_element
