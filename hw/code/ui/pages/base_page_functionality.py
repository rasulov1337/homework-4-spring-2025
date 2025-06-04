import time
from functools import wraps


from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

BASIC_TIMEOUT = 10

class PageNotOpenedException(Exception):
    pass


class BasePageFunctionality(object):
    def is_opened(self, timeout=BASIC_TIMEOUT):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url.find(self.url) >= 0:
                return True
        raise PageNotOpenedException(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=BASIC_TIMEOUT) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=BASIC_TIMEOUT, until_EC=EC.presence_of_element_located) -> WebElement:
        return self.wait(timeout).until(until_EC(locator))

    def find_with_check_visibility(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        return self.find(locator, timeout, until_EC=EC.visibility_of_element_located)

    def click(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        elem = self.find(locator, timeout=timeout, until_EC=EC.element_to_be_clickable)
        elem.click()

        return elem

    def hover_to_element(self, element):
        AC(self.driver).move_to_element(element).perform()

        return element

    def hover_wrapper(self, locator, timeout=BASIC_TIMEOUT) -> WebElement:
        elem = self.find(locator, timeout=timeout)

        return self.hover_to_element(elem)

    def write_input_to_element(self, element, message) -> WebElement:
        element.clear()
        element.send_keys(message)

        return element

    def write_input(self, locator, message, timeout=BASIC_TIMEOUT) -> WebElement:
        input_element = self.find_with_check_visibility(locator, timeout)
        input_element = self.write_input_to_element(input_element, message)
        self.wait().until(EC.text_to_be_present_in_element_value(locator, message))

        return input_element

    def write_input_without_clearing(self, locator, message, timeout=BASIC_TIMEOUT):
        input_element = self.find_with_check_visibility(locator, timeout)
        input_element.send_keys(message)
        self.wait().until(EC.text_to_be_present_in_element_value(locator, message))

        return input_element

    @staticmethod
    def get_value_from_elem(element):
        return element.get_attribute('value')

    def get_value(self, locator, timeout=BASIC_TIMEOUT):
        element = self.find(locator, timeout)

        return self.get_value_from_elem(element)

    def check_url(self, expected_url, timeout=BASIC_TIMEOUT):
        return self.wait(timeout).until(EC.url_matches(expected_url))

    def find_child(self, parent, child_locator, timeout=BASIC_TIMEOUT, until_EC=EC.presence_of_element_located):
        return WebDriverWait(parent, timeout).until(
            until_EC(child_locator)
        )

    def close_alert_if_shown(self, timeout=BASIC_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception:
            pass


# add_write add method write() to input field
def add_write(input_field_getter):
    @wraps(input_field_getter)
    def functionality(self, *args, **kwargs):
        input_field_result = input_field_getter(self, *args, **kwargs)

        def write(message):
            return self.write_input_to_element(input_field_result, message=message)

        input_field_result.write = write

        return input_field_result

    return functionality


# add_hover add method hover() to element
def add_hover(elem_getter):
    @wraps(elem_getter)
    def functionality(self, *args, **kwargs):
        hoverable_elem_result = elem_getter(self, *args, **kwargs)

        def hover():
            return self.hover_to_element(hoverable_elem_result)

        hoverable_elem_result.hover = hover

        return hoverable_elem_result

    return functionality


def add_get_value(elem_getter):
    @wraps(elem_getter)
    def functionality(self, timeout=BASIC_TIMEOUT, *args, **kwargs):
        value_elem_result = elem_getter(self, *args, **kwargs)

        def get_value():
            return self.get_value_from_elem(value_elem_result)

        value_elem_result.get_value = get_value

        return value_elem_result

    return functionality


def add_clicks(button_getter):
    """Adds clicks method to button"""

    def decorator(self, *args, **kwargs):
        button = button_getter(self, *args, **kwargs)

        def __click():
            """Clicks button"""
            self.click(button)

        button.clicks = __click
        return button

    return decorator