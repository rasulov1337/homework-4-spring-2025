from ui.pages.base_page import BasePage
from ui.locators.leadforms_locators import LeadFormsPageLocators


class LeadformPage(BasePage):
    url = "https://ads.vk.com/hq/leadads/leadforms"
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

    def is_leadform_page_opened(self) -> bool:
        return self.is_visible(LeadFormsPageLocators.CONTINUE_BUTTON)

    def fill_leadform_name_field(self, name: str):
        self.fill_field(LeadFormsPageLocators.INPUT_NAME_LEAD_FORM, name)

    def fill_company_name_field(self, name: str):
        self.fill_field(LeadFormsPageLocators.INPUT_NAME_COMPANY, name)

    def fill_leadform_title_field(self, title: str):
        self.fill_field(LeadFormsPageLocators.INPUT_TITLE, title)

    def fill_leadform_description_field(self, description: str):
        self.fill_field(LeadFormsPageLocators.INPUT_DESCRIPTION, description)

    def click_download_and_choose_logo_button(self):
        self.click(LeadFormsPageLocators.DOWNLOAD_LOGO)
        self.click(LeadFormsPageLocators.CHOOSE_LOGO)
        self.became_invisible(LeadFormsPageLocators.CHOOSE_LOGO, 5)

    def click_save_button(self):
        self.click(LeadFormsPageLocators.CONTINUE_BUTTON)

    def is_question_leadform_page_opened(self) -> bool:
        return self.is_visible(LeadFormsPageLocators.ADD_CONTACTS_BUTTON)

    def is_result_leadform_page_opened(self) -> bool:
        return self.is_visible(LeadFormsPageLocators.ADD_SITE_BUTTON)

    def is_settings_leadform_page_opened(self) -> bool:
        return self.is_visible(LeadFormsPageLocators.CONTACTS)

    def fill_leadform_contacts_field(self, name: str):
        self.fill_field(LeadFormsPageLocators.CONTACTS, name)

    def fill_leadform_legal_adress_field(self, adress: str):
        self.fill_field(LeadFormsPageLocators.INPUT_LEGAL_ADRESS_COMPANY, adress)

    def is_leadform_in_list_exists(self, name: str) -> bool:
        return self.is_visible(LeadFormsPageLocators.SELECT_FROM_LEADFORM_LIST(name))

    def fill_find_leadform_field(self, name: str):
        self.fill_field(LeadFormsPageLocators.INPUT_FIND_LEADFORM, name)

    def delete_all_leadforms(self):
        try:
            self.click(self.locators.SELECT_ALL_FORMS)
            self.click(self.locators.SELECT_ACTIONS_BUTTON)
            self.click(self.locators.DELETE_ACTION)
        except Exception as e:
            print(f"Не удалось удалить лид-формы: {e}")
