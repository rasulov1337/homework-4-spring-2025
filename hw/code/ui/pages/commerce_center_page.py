from .base_page import BasePage
from ui.locators.commerce_center_locators import CommerceCenterPageLocators



class CommerceCenterPage(BasePage):
    locators = CommerceCenterPageLocators()
    url = 'https://ads.vk.com/hq/ecomm/catalogs'

    def click_undergo_training(self):
        self.click(self.locators.UNDERGO_TRAINING_BUTTON)

    def close_popup(self):
        self.click(self.locators.CLOSE_POPUP_BUTTON)

    def popup_active(self):
        return self.find(self.locators.CURRENT_POPUP)
