import os

from ui.locators.survey_locators import SurveyLocators
from base import BaseCase
from ui.pages.survey_page import SurveyPage

FILEPATH = os.path.join(os.path.dirname(__file__), 'files/img.png')


class TestSurveyPage(BaseCase):
    locators = SurveyLocators()

    def test_survey_upload_image(self, survey_page:SurveyPage):
        survey_page.click_create_survey_button()
        survey_page.upload_image(FILEPATH)
        assert survey_page.get_last_image_name_from_media_library() == os.path.basename(FILEPATH)

    def test_survey_fill_empty(self, survey_page):
        survey_page.click_create_survey_button()
        survey_page.fill_empty_data()
        survey_page.click_continue()

        name_error = survey_page.find(self.locators.ERROR_1_TITLE)
        company_name_error = survey_page.find(self.locators.ERROR_1_COMPANY)
        title_error = survey_page.find(self.locators.ERROR_1_HEADER)
        description_error = survey_page.find(self.locators.ERROR_1_DESCRIPTION)

        expected_message = 'Нужно заполнить'
        assert name_error.text == expected_message, f"Expected '{expected_message}', got '{name_error.text}'"
        assert company_name_error.text == expected_message, f"Expected '{expected_message}', got '{company_name_error.text}'"
        assert title_error.text == expected_message, f"Expected '{expected_message}', got '{title_error.text}'"
        assert description_error.text == expected_message, f"Expected '{expected_message}', got '{description_error.text}'"

    def test_survey_fill_invalid(self, survey_page):
        survey_page.click_create_survey_button()
        survey_page.fill_data('a' * 256, 'a' * 31, 'a' * 51, 'a' * 351)
        survey_page.click_continue()

        name_error = survey_page.find(self.locators.ERROR_1_TITLE)
        company_name_error = survey_page.find(self.locators.ERROR_1_COMPANY)
        title_error = survey_page.find(self.locators.ERROR_1_HEADER)
        description_error = survey_page.find(self.locators.ERROR_1_DESCRIPTION)

        expected_message = 'Сократите текст'
        assert name_error.text == expected_message, f"Expected '{expected_message}', got '{name_error.text}'"
        assert company_name_error.text == expected_message, f"Expected '{expected_message}', got '{company_name_error.text}'"
        assert title_error.text == expected_message, f"Expected '{expected_message}', got '{title_error.text}'"
        assert description_error.text == expected_message, f"Expected '{expected_message}', got '{description_error.text}'"

    def test_survey_fill_survey(self, survey_page):
        survey_page.click_create_survey_button()
        survey_page.click_last_image_name_from_media_library()

        survey_page.fill_data('1', '1', '1', '1')
        survey_page.click_continue()

        survey_page.fill_title('1')
        survey_page.fill_answers('1', '1')
        survey_page.click_continue()

        survey_page.fill_thanks('1')
        survey_page.fill_description('1')
        survey_page.click_continue()

        assert survey_page.get_form_name() == '1'
