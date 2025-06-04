from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class SitesPageLocators(BasePageLocators):
    ADD_PIXEL_BUTTON = (By.XPATH, '//button[span[span[text()="Добавить пиксель"]]]')
    SITE_DOMAIN_INPUT = (By.XPATH, '//Input[@placeholder="Домен сайта"]')
    MODAL_ADD_PIXEL_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "ModalRoot")]//button[span[span[text()="Добавить пиксель"]]]',
    )
    ALERT_SPAN = (By.XPATH, '//span[@role="alert"]')
    CLOSE_MODAL_BUTTON = (By.XPATH, '//div[@aria-label="Закрыть"]')
    PIXEL_CREATED_TEXT = (By.XPATH, '//span[contains(text(), "Создан ID пикселя")]')
    GET_CODE_BUTTON = (By.XPATH, '//a[span[span[text()="Получить код"]]]')
    COPY_CODE_BUTTON = (By.XPATH, '//button[span[span[text()="Скопировать код"]]]')
    PIXEL_MORE_BUTTON = (By.XPATH, '//button[@aria-label="More"]')
    DELETE_PIXEL_BUTTON = (By.XPATH, '//div[span[text()="Удалить пиксель"]]')
    CONFIRM_DELETE_PIXEL_BUTTON = (By.XPATH, '//button[span[span[text()="Удалить"]]]')
    CONFIRM_DELITION_OVERLAY = (
        By.XPATH,
        '//div[contains(@class, "ModalRoot_overlay")]',
    )
    PIXEL_URL_ANCHOR = (
        By.XPATH,
        '//a[contains(@class, "vkuiLink vkuiTappable") and @target="_blank"]',
    )
