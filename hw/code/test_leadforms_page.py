import os
from datetime import datetime

from base import BaseCase
from ui.locators.leadforms_locators import LeadFormsPageLocators
from ui.pages.leadforms_page import LeadformPage

FILEPATH = os.path.join(os.path.dirname(__file__), "files/img.png")

LEADFORM_NAME = "Лид-форма " + str(datetime.now().second)
EDIT_LEADFORM_NAME = "Новая Лид-форма " + str(datetime.now().second)
COMPANY_NAME = "VK"
LEADFORM_TITLE = "Заголовок 1"
LEADFORM_DESCRIPTION = "Опрос 1"
CONTACTS = "Иванов Иван Иваныч"
COMPANY_ADRESS = "Москва, улица Арбат, дом 1"


class TestLeadFormsPage(BaseCase):
    locators = LeadFormsPageLocators()
    EXPECTED_MESSAGE = "Нужно заполнить"

    def setup_method(self, method):
        if method.__name__ == "test_find_leadform":
            self.leadforms_page = LeadformPage(self.driver)

            self.leadforms_page.click_create_leadform_button()
            self.leadforms_page.fill_leadform_name_field(LEADFORM_NAME)
            self.leadforms_page.click_download_and_choose_logo_button()
            self.leadforms_page.fill_company_name_field(COMPANY_NAME)
            self.leadforms_page.fill_leadform_title_field(LEADFORM_TITLE)
            self.leadforms_page.fill_leadform_description_field(LEADFORM_DESCRIPTION)
            self.leadforms_page.click_save_button()
            self.leadforms_page.click_save_button()
            self.leadforms_page.click_save_button()
            self.leadforms_page.fill_leadform_contacts_field(CONTACTS)
            self.leadforms_page.fill_leadform_legal_adress_field(COMPANY_ADRESS)
            self.leadforms_page.click_save_button()

    def teardown_method(self, method):
        self.leadforms_page.delete_all_leadforms()

    def test_leadforms_negative_compact_empty(self, leadforms_page):
        leadforms_page.click_create_leadform_button()

        leadforms_page.fill_empty_data()
        leadforms_page.click_continue()

        logo_empty = leadforms_page.find(self.locators.ERROR_1_LOGO)
        company_name_empty = leadforms_page.find(self.locators.ERROR_1_COMPANY)
        title_empty = leadforms_page.find(self.locators.ERROR_1_HEADING)
        description_empty = leadforms_page.find(self.locators.ERROR_1_DESCRIPTION)

        assert (
            logo_empty.text == self.EXPECTED_MESSAGE
        ), f"Expected '{self.EXPECTED_MESSAGE}', got '{logo_empty.text}'"
        assert (
            company_name_empty.text == self.EXPECTED_MESSAGE
        ), f"Expected '{self.EXPECTED_MESSAGE}', got '{company_name_empty.text}'"
        assert (
            title_empty.text == self.EXPECTED_MESSAGE
        ), f"Expected '{self.EXPECTED_MESSAGE}', got '{title_empty.text}'"
        assert (
            description_empty.text == self.EXPECTED_MESSAGE
        ), f"Expected '{self.EXPECTED_MESSAGE}', got '{description_empty.text}'"

    def test_create_leadform(self, leadforms_page):
        leadforms_page.click_create_leadform_button()
        assert leadforms_page.is_leadform_page_opened()

        leadforms_page.fill_leadform_name_field(LEADFORM_NAME)
        leadforms_page.click_download_and_choose_logo_button()
        leadforms_page.fill_company_name_field(COMPANY_NAME)
        leadforms_page.fill_leadform_title_field(LEADFORM_TITLE)
        leadforms_page.fill_leadform_description_field(LEADFORM_DESCRIPTION)
        leadforms_page.click_save_button()

        assert leadforms_page.is_question_leadform_page_opened()
        leadforms_page.click_save_button()

        assert leadforms_page.is_result_leadform_page_opened()
        leadforms_page.click_save_button()

        assert leadforms_page.is_settings_leadform_page_opened()
        leadforms_page.fill_leadform_contacts_field(CONTACTS)
        leadforms_page.fill_leadform_legal_adress_field(COMPANY_ADRESS)
        leadforms_page.click_save_button()

        assert leadforms_page.is_leadform_in_list_exists(LEADFORM_NAME)

    def test_find_leadform(self, leadforms_page):
        leadforms_page.fill_find_leadform_field(LEADFORM_NAME)
        assert leadforms_page.is_leadform_in_list_exists(LEADFORM_NAME)

        unknown_leadform_name = "Неизвестная лид-форма"
        leadforms_page.fill_find_leadform_field(unknown_leadform_name)
        assert not leadforms_page.is_leadform_in_list_exists(unknown_leadform_name)
