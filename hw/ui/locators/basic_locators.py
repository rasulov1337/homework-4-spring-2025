from selenium.webdriver.common.by import By


class BasePageLocators:
    BODY = (By.TAG_NAME, 'body')
    PAGE_HEADER = (By.XPATH, '//h2[@class="page-header"]')


class EventsPageLocators(BasePageLocators):
    pass
