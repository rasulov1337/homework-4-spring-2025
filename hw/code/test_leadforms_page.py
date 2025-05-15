import os
from datetime import datetime

from base import BaseCase
from ui.locators.leadforms_locators import LeadFormsPageLocators

FILEPATH = os.path.join(os.path.dirname(__file__), 'files/img.png')

LEADFORM_NAME = 'Лид-форма ' + str(datetime.now().second)
EDIT_LEADFORM_NAME = 'Новая Лид-форма ' + str(datetime.now().second)
COMPANY_NAME = 'VK'
LEADFORM_TITLE = 'Заголовок 1'
LEADFORM_DESCRIPTION = 'Опрос 1'
CONTACTS = 'Иванов Иван Иваныч'
COMPANY_ADRESS = 'Москва, улица Арбат, дом 1'


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
    
    def test_create_leadform(self, leadform_page):
        leadform_page.click_create_leadform_button()
        assert leadform_page.is_leadform_page_opened()

        leadform_page.fill_leadform_name_field(LEADFORM_NAME)
        leadform_page.click_download_and_choose_logo_button()
        leadform_page.fill_company_name_field(COMPANY_NAME)
        leadform_page.fill_leadform_title_field(LEADFORM_TITLE)
        leadform_page.fill_leadform_description_field(LEADFORM_DESCRIPTION)
        leadform_page.click_save_button()

        assert leadform_page.is_question_leadform_page_opened()
        leadform_page.click_save_button()

        assert leadform_page.is_result_leadform_page_opened()
        leadform_page.click_save_button()

        assert leadform_page.is_settings_leadform_page_opened()
        leadform_page.fill_leadform_contacts_field(CONTACTS)
        leadform_page.fill_leadform_legal_adress_field(COMPANY_ADRESS)
        leadform_page.click_save_button()

        assert leadform_page.is_leadform_in_list_exists(LEADFORM_NAME)

    def test_find_leadform(self, leadform_page):
        leadform_page.fill_find_leadform_field(LEADFORM_NAME)
        assert leadform_page.is_leadform_in_list_exists(LEADFORM_NAME)

        unknown_leadform_name = 'Неизвестная лид-форма'
        leadform_page.fill_find_leadform_field(unknown_leadform_name)
        assert not leadform_page.is_leadform_in_list_exists(unknown_leadform_name)

