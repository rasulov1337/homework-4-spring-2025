from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_BUTTON = (By.XPATH, "//button[contains(@class, 'CookieBanner_button__')]")
    CURRENT_MODAL = (By.XPATH, '//div[contains(@class, "ModalRoot_overlay__")]')
    BODY = (By.XPATH, "//body")
