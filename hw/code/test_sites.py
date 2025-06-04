from base import BaseCase
from ui.pages.sites_page import SitesPage
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker()


class TestSitesPage(BaseCase):
    WRONG_SITE_LINK_TEXT = "Введите корректный адрес сайта (вида: example.ru)"
    WRONG_DOMAIN_VALUE = "вронг"

    def test_empty_site_link(self, sites_page: SitesPage):
        sites_page.click_add_pixel()
        sites_page.fill_in(
            sites_page.locators.SITE_DOMAIN_INPUT, self.WRONG_DOMAIN_VALUE
        )
        sites_page.clear(sites_page.locators.SITE_DOMAIN_INPUT)

        add_pixel_button = sites_page.find(sites_page.locators.MODAL_ADD_PIXEL_BUTTON)

        assert add_pixel_button.is_enabled is False

    def test_wrong_site_link(self, sites_page: SitesPage):
        sites_page.click_add_pixel()
        sites_page.fill_in(
            sites_page.locators.SITE_DOMAIN_INPUT, self.WRONG_DOMAIN_VALUE
        )
        sites_page.click_create_pixel()
        sites_page.wait().until(
            EC.visibility_of_element_located(sites_page.locators.ALERT_SPAN)
        )

        current_modal_text = sites_page.find(sites_page.locators.CURRENT_MODAL).text
        assert self.WRONG_SITE_LINK_TEXT in current_modal_text

    def test_valid_site_link(self, sites_page: SitesPage):
        random_site = fake.url()

        sites_page.click_add_pixel()
        sites_page.fill_in(sites_page.locators.SITE_DOMAIN_INPUT, random_site)
        sites_page.click_create_pixel()

        sites_page.wait(timeout=60).until(
            EC.visibility_of_element_located(sites_page.locators.PIXEL_CREATED_TEXT),
        )

        sites_page.click(sites_page.locators.GET_CODE_BUTTON)

        sites_page.wait(10).until(
            lambda d: len(d.window_handles) > 1
        )  # Wait for new tab to open
        self.driver.switch_to.window(self.driver.window_handles[1])
        site_url_text = self.driver.find_element(
            sites_page.locators.PIXEL_URL_ANCHOR
        ).text
        assert random_site in site_url_text

    def teardown_method(self, method):
        try:
            sites_page = SitesPage(self.driver)

            buttons = sites_page.find_all(sites_page.locators.PIXEL_MORE_BUTTON)
            for button in buttons:
                button.click()
                sites_page.click_delete_pixel()
                sites_page.confirm_pixel_delition()
                sites_page.wait(30).until(
                    EC.invisibility_of_element_located(
                        sites_page.locators.CONFIRM_DELITION_OVERLAY
                    )
                )

            sites_page.page.delete_catalog_by_name(self.CATALOG_NAME_TEXT)
        except Exception:
            pass
