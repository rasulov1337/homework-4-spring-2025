from .base_page import BasePage
from ui.locators.commerce_center_locators import CommerceCenterPageLocators
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait


class CommerceCenterPage(BasePage):
    locators = CommerceCenterPageLocators()
    url = "https://ads.vk.com/hq/ecomm/catalogs"

    def click_undergo_training(self):
        self.click(self.locators.UNDERGO_TRAINING_BUTTON)

    def close_popup(self):
        self.click(self.locators.CLOSE_POPUP_BUTTON)

    def popup_active(self):
        return self.find(self.locators.CURRENT_POPUP)

    def open_catalog_creation_form(self):
        self.click(self.locators.CREATE_CATALOG)

    def close_catalog_creation_form(self):
        self.click(self.locators.CommerceCenterSidebarFormLocators.CANCEL_BUTTON)

    def clear_catalogue_name(self):
        self.click(self.locators.CommerceCenterSidebarFormLocators.NAME_INPUT)
        self.clear(self.locators.CommerceCenterSidebarFormLocators.NAME_INPUT)

    def select_position_feed_or_community(self):
        self.click(
            self.locators.CommerceCenterSidebarFormLocators.FEED_OR_COMMUNITY_BUTTON
        )

    def select_position_marketplace(self):
        self.click(self.locators.CommerceCenterSidebarFormLocators.MARKETPLACE_BUTTON)

    def select_position_manually(self):
        self.click(self.locators.CommerceCenterSidebarFormLocators.MANUALLY_BUTTON)

    def click_sidebar_form_create_catalog(self):
        self.click(
            self.locators.CommerceCenterSidebarFormLocators.CREATE_CATALOG_BUTTON
        )
