from ..locators.main_page import MainPageLocators
from ..pages.base_page import BasePage


class MainPage(BasePage):
    url = "https://ads.vk.com/"
    locators = MainPageLocators()

    def click_vk_ads_logo(self):
        self.click(self.locators.VK_ADS_LOGO)

    def click_nav_item(self, item_name: str):
        self.click(self.locators.NAV_ITEM(self.locators.MAIN_PAGE_LINKS[item_name]))

    def click_dropdown_item(self, item_name: str):
        self.click(
            self.locators.NAV_DROPDOWN_MENU_ITEM(
                self.locators.MAIN_PAGE_LINKS[item_name]
            )
        )
