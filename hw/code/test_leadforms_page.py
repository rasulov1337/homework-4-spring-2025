import os

from base import BaseCase
from ui.locators.leadforms_locators import LeadFormsPageLocators

FILEPATH = os.path.join(os.path.dirname(__file__), 'files/img.png')


class TestLeadFormsPage(BaseCase):
    locators = LeadFormsPageLocators()

    def test_leadforms_negative_compact_empty(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_empty_data()
        leadforms_page.click_continue()

        logo_empty = leadforms_page.find(self.locators.ERROR_1_LOGO)
        company_name_empty = leadforms_page.find(self.locators.ERROR_1_COMPANY)
        title_empty = leadforms_page.find(self.locators.ERROR_1_HEADING)
        description_empty = leadforms_page.find(self.locators.ERROR_1_DESCRIPTION)

        expected_message = 'Нужно заполнить'
        assert logo_empty.text == expected_message, f"Expected '{expected_message}', got '{logo_empty.text}'"
        assert company_name_empty.text == expected_message, f"Expected '{expected_message}', got '{company_name_empty.text}'"
        assert title_empty.text == expected_message, f"Expected '{expected_message}', got '{title_empty.text}'"
        assert description_empty.text == expected_message, f"Expected '{expected_message}', got '{description_empty.text}'"
