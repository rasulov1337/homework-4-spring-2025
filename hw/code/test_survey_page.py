import os
import pytest

from base import BaseCase
from ui.pages.survey_page import SurveyPage

FILEPATH = os.path.join(os.path.dirname(__file__), "files/img.png")


class TestSurveyPage(BaseCase):
    def teardown_method(self, method):
        self.survey_page = SurveyPage(self.driver)
        self.survey_page.delete_all_forms()

    def test_survey_upload_image(self, survey_page: SurveyPage):
        survey_page.click_create_survey_button()
        survey_page.upload_image(FILEPATH)
        assert survey_page.get_last_image_name_from_media_library() == os.path.basename(
            FILEPATH
        )

    @pytest.mark.parametrize(
        "name, company_name, title, description, expected_message",
        [
            ("", "", "", "", "Нужно заполнить"),
            ("a" * 256, "a" * 31, "a" * 51, "a" * 351, "Сократите текст"),
        ],
    )
    def test_survey_validation(
        self,
        survey_page: SurveyPage,
        name,
        company_name,
        title,
        description,
        expected_message,
    ):
        survey_page.click_create_survey_button()

        if name == "":
            survey_page.fill_empty_data()
        else:
            survey_page.fill_data(name, company_name, title, description)

        survey_page.click_continue()

        name_error = survey_page.find(self.locators.ERROR_1_TITLE).text
        company_name_error = survey_page.find(self.locators.ERROR_1_COMPANY).text
        title_error = survey_page.find(self.locators.ERROR_1_HEADER).text
        description_error = survey_page.find(self.locators.ERROR_1_DESCRIPTION).text

        assert name_error == expected_message
        assert company_name_error == expected_message
        assert title_error == expected_message
        assert description_error == expected_message

    def test_survey_fill_survey(self, survey_page: SurveyPage):
        survey_page.click_create_survey_button()
        survey_page.click_last_image_name_from_media_library()

        survey_page.fill_data("1", "1", "1", "1")
        survey_page.click_continue()

        survey_page.fill_title("1")
        survey_page.fill_answers("1", "1")
        survey_page.click_continue()

        survey_page.fill_thanks("1")
        survey_page.fill_description("1")
        survey_page.click_continue()

        assert survey_page.get_form_name() == "1"
