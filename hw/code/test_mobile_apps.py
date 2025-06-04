from base import BaseCase
from ui.pages.mobile_apps_page import MobileAppsPage
from selenium.webdriver.support import expected_conditions as EC


class TestSitesPage(BaseCase):
    APP_LINK_INPUT_VALUE = "https://vk.com/"
    WRONG_APP_LINK_TEXT = "Введите корректную ссылку на приложение"

    def test_modal_shows(self, mobile_apps_page: MobileAppsPage):
        mobile_apps_page.click(mobile_apps_page.locators.ADD_APP_BUTTON)
        assert mobile_apps_page.modal_active()

    def test_invalid_link(self, mobile_apps_page: MobileAppsPage):
        mobile_apps_page.click(mobile_apps_page.locators.ADD_APP_BUTTON)
        mobile_apps_page.fill_in(
            mobile_apps_page.locators.APP_LINK_INPUT, self.APP_LINK_INPUT_VALUE
        )

        mobile_apps_page.click(mobile_apps_page.locators.MODAL_ADD_APP_BUTTON)

        mobile_apps_page.wait(timeout=10).until(
            EC.visibility_of_element_located(mobile_apps_page.locators.ALERT_TEXT)
        )

        alert_text = mobile_apps_page.find(mobile_apps_page.locators.ALERT_TEXT).text

        assert alert_text == self.WRONG_APP_LINK_TEXT
