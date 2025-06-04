from base import BaseCase
from ui.pages.sites_page import SitesPage
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


fake = Faker()


class TestSitesPage(BaseCase):
    def test_empty_site_link(self, sites_page: SitesPage):
        sites_page.click_add_pixel()
        sites_page.fill_in(sites_page.locators.SITE_DOMAIN_INPUT, "вронг")
        sites_page.clear(sites_page.locators.SITE_DOMAIN_INPUT)

        assert (
            sites_page.find(sites_page.locators.MODAL_ADD_PIXEL_BUTTON).is_enabled
            is False
        )

    def test_wrong_site_link(self, sites_page: SitesPage):
        sites_page.click_add_pixel()
        sites_page.fill_in(sites_page.locators.SITE_DOMAIN_INPUT, "вронг")
        sites_page.click_create_pixel()
        sites_page.wait().until(
            EC.visibility_of_element_located(sites_page.locators.ALERT_SPAN)
        )
        assert (
            "Введите корректный адрес сайта (вида: example.ru)"
            in sites_page.find(sites_page.locators.CURRENT_MODAL).text
        )

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
        # self.driver.switch_to.window(self.driver.window_handles[1])
        # assert random_site in self.driver.find_element(sites_page.locators.BODY).text
