from selenium.webdriver.support import expected_conditions as ec

from ui.pages.base_page import BasePage
from ui.locators.leadforms_locators import LeadFormsPageLocators


class LeadFormsPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators = LeadFormsPageLocators()

    def click_create_leadform_button(self):
        self.click(self.locators.CREATE_LEADFORM_BUTTON)

    def fill_empty_data(self):
        name_input = self.find(self.locators.LEADFORM_NAME_INPUT)
        company_name_input = self.find(self.locators.COMPANY_NAME_INPUT)
        title_input = self.find(self.locators.LEADFORM_TITLE_INPUT)
        description_input = self.find(self.locators.LEADFORM_DESCRIPTION_INPUT)
        name_input.clear()
        company_name_input.clear()
        title_input.clear()
        description_input.clear()
    
    def click_continue(self):
        self.click(self.locators.CONTINUE_BUTTON)
