from ui.locators.sites_page_locators import SitesPageLocators
from ui.pages.base_page import BasePage


class SitesPage(BasePage):
    url = "https://ads.vk.com/hq/pixels/"
    locators = SitesPageLocators()

    def click_add_pixel(self):
        self.click(self.locators.ADD_PIXEL_BUTTON)

    def close_modal(self):
        self.click(self.locators.CLOSE_MODAL_BUTTON)

    def click_create_pixel(self):
        self.click(self.locators.MODAL_ADD_PIXEL_BUTTON)
