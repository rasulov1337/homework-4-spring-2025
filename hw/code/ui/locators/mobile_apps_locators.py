from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class MobileAppsPageLocators(BasePageLocators):
    ADD_APP_BUTTON = (By.XPATH, '//button[@data-testid="add-app"]')
    APP_LINK_INPUT = (By.XPATH, '//input[@data-testid="app-link"]')
    ALERT_TEXT = (
        By.XPATH,
        '//span/span[text()="Введите корректную ссылку на приложение"]',
    )
    MODAL_ADD_APP_BUTTON = (By.XPATH, '//button[@data-testid="app-add"]')
