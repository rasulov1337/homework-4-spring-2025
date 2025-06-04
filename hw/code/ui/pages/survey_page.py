from ui.pages.base_page import BasePage
from ui.locators.survey_locators import SurveyLocators


class SurveyPage(BasePage):
    url = "https://ads.vk.com/hq/leadads/surveys"
    locators = SurveyLocators()

    def click_continue(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def click_create_survey_button(self):
        self.click(self.locators.CREATE_SURVEY_BUTTON)

    def get_last_image_name_from_media_library(self) -> str:
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        return self.find(self.locators.UPLOADED_IMAGE_NAME).text

    def fill_empty_data(self):
        name_input = self.find(self.locators.TITLE_INPUT)
        company_name_input = self.find(self.locators.COMPANY_INPUT)
        title_input = self.find(self.locators.HEADER_INPUT)
        description_input = self.find(self.locators.DESCRIPTION_INPUT)

        name_input.clear()
        company_name_input.clear()
        title_input.clear()
        description_input.clear()

    def fill_data(self, name, company, title, desc):
        name_input = self.find(self.locators.TITLE_INPUT)
        company_name_input = self.find(self.locators.COMPANY_INPUT)
        title_input = self.find(self.locators.HEADER_INPUT)
        description_input = self.find(self.locators.DESCRIPTION_INPUT)

        self.fill_empty_data()

        name_input.send_keys(name)
        company_name_input.send_keys(company)
        title_input.send_keys(title)
        description_input.send_keys(desc)

    def upload_image(self, filepath: str):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        load_image_input = self.find(self.locators.LOAD_IMAGE_INPUT)
        load_image_input.send_keys(filepath)

    def delete_all_from_media_library(self):
        self.click(self.locators.EDIT_IMAGES_BUTTON)
        self.click(self.locators.SELECT_ALL_IMAGES_BUTTON)
        self.click(self.locators.DELETE_IMAGES_BUTTON)
        self.click(self.locators.CONFIRM_DELETE_BUTTON)

    def fill_title(self, title):
        title_input = self.find(self.locators.QUESTION_TITLE_INPUT)
        title_input.send_keys(title)

    def click_add_question(self):
        self.click(self.locators.ADD_QUESTION_BUTTON)

    def fill_answer(self, answer):
        answer_input = self.find(self.locators.ANSWER_1_INPUT)
        answer_input.send_keys(answer)

    def fill_answers(self, answer1, answer2):
        answer_input = self.find(self.locators.ANSWER_1_INPUT)
        answer_input.send_keys(answer1)

        answer_input = self.find(self.locators.ANSWER_2_INPUT)
        answer_input.send_keys(answer2)

    def click_selector_many(self):
        self.click(self.locators.SELECTOR_INPUT)
        self.click(self.locators.SELECTOR_MANY)

    def click_selector_answer(self):
        self.click(self.locators.SELECTOR_INPUT)
        self.click(self.locators.SELECTOR_ANSWER)

    def click_selector_scale(self):
        self.click(self.locators.SELECTOR_INPUT)
        self.click(self.locators.SELECTOR_SCALE)

    def fill_thanks(self, thanks):
        thanks_input = self.find(self.locators.HEADER_3)
        thanks_input.clear()
        thanks_input.send_keys(thanks)

    def fill_description(self, description):
        description_input = self.find(self.locators.DESCRIPTION_3)
        description_input.clear()
        description_input.send_keys(description)

    def fill_link(self, link):
        link_input = self.find(self.locators.LINK_3)
        link_input.clear()
        link_input.send_keys(link)

    def remove_survey(self):
        self.click(self.locators.ARCHIVE_BUTTON)
        self.click(self.locators.ARCHIVE_ACCEPT_BUTTON)

    def click_last_image_name_from_media_library(self):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        self.click(self.locators.UPLOADED_IMAGE_NAME)
        self.became_invisible(self.locators.UPLOAD_IMAGE_MODAL)

    def get_form_name(self) -> str:
        name = self.find(self.locators.FIRST_LEAD_FORM_NAME)
        return name.text

    def get_error_texts(self) -> dict:
        return {
            "name": self.find(self.locators.ERROR_1_TITLE).text.strip(),
            "company": self.find(self.locators.ERROR_1_COMPANY).text.strip(),
            "title": self.find(self.locators.ERROR_1_HEADER).text.strip(),
            "description": self.find(self.locators.ERROR_1_DESCRIPTION).text.strip(),
        }
    
    def delete_all_forms(self, name: str):
        try:
            self.click(self.locators.SELECT_ALL_FORMS)
            self.click(self.locators.SELECT_ACTIONS_BUTTON)
            self.click(self.locators.DELETE_ACTION)
        except Exception as e:
            print(f"Не удалось удалить опросы: {e}")