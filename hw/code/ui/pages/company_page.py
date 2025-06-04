from .base_page import BasePage
from ui.locators.company_locators import CompanyPageLocators
from enum import Enum
import time

class CompanyTarget(Enum):
    SITE = 'site'
    CATALOG = 'ecomm'
    PUBLIC = 'social'
    ODKL = 'odkl'


class CompanyPage(BasePage):
    locators = CompanyPageLocators()
    url = 'https://ads.vk.com/hq/dashboard'

    def open_companies_list(self):
        self.click(self.locators.LOGO)
        self.click(self.locators.left_menu.COMPANIES_BTN)

    def open_companies_drafts(self):
        self.click(self.locators.COMPANIES_TYPES_DROPDOWN)
        self.click(self.locators.COMPANIES_DRAFTS)

    def get_companies_drafts(self):
        return list(map(lambda company_draft_name_element: company_draft_name_element.text,
                   self.find_all(self.locators.COMPANY_DRAFT_NAME)))

    def open_company_creation(self):
        self.click(self.locators.CREATE_COMPANY_BTN)

    def clear_companies(self):
        pass

    def select_target(self, target: CompanyTarget):
        if target == CompanyTarget.SITE:
            self.click(self.locators.SITE_COMPANY_TARGET)

    def set_site_url(self, url: str):
        self.fill_in(self.locators.SITE_URL_INPUT, url)

    def close_help_modal(self):
        try:
            self.click(self.locators.CLOSE_HELP_MODAL_BTN_LOCATOR)
        except:
            pass

    def apply_target(self):
        self.fill(self.locators.COMPANY_BUDGET_INPUT, '1000')
        self.unfocus()

    def set_region(self):
        self.find(self.locators.TARGET_LABEL_LOCATOR)
        self.click(self.locators.REGION_RUSSIA_BTN_LOCATOR)

    def wait_for_region(self):
        self.find(self.locators.REGION_RUSSIA_BTN_LOCATOR)

    def is_no_region_message_visible(self):
        return self.is_visible(self.locators.NO_REGION_ERROR_LOCATOR)

    def wait_ad_header(self):
        self.find(self.locators.AD_HEADER_INPUT)

    def set_ad_header(self, header: str):
        elem = self.find(self.locators.AD_HEADER_INPUT)
        elem.send_keys(header)

    def set_ad_short_desc(self, description: str):
        elem = self.find(self.locators.AD_SHORT_DECS_TEXTAREA)
        elem.send_keys(description)

    def click_next(self):
        self.click(self.locators.NEXT_BTN)

    def click_logo(self):
        self.click(self.locators.LOGO)

    def confirm_draft_company(self):
        self.click(self.locators.SAVE_DRAFT_COMPANY_BTN)

    def save_company(self):
        self.click(self.locators.SAVE_COMPANY_BTN)

    def check_not_click_next(self):
        self.became_invisible(self.locators.ERROR_LOCATOR, 5)
        self.click(self.locators.NEXT_BTN)
        return
        
    def clear_all_companies(self):
        try:
            self.open_companies_list()
            self.open_companies_drafts()

            checkbox = self.find(self.locators.SELECT_ALL_CHECKBOX, timeout=3)
            if checkbox.is_displayed():
                checkbox.click()

            delete_btn = self.find(self.locators.DELETE_COMPANY_BTN, timeout=3)
            if delete_btn.is_enabled():
                delete_btn.click()
        except Exception:
            pass