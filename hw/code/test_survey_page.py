import os

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

    def test_survey_fill_invalid(self, survey_page: SurveyPage):
        survey_page.click_create_survey_button()
        survey_page.fill_data("a" * 256, "a" * 31, "a" * 51, "a" * 351)
        survey_page.click_continue()

        errors = survey_page.get_error_texts()
        for field, actual in errors.items():
            assert actual == "Сократите текст", f"{field}: expected 'Сократите текст', got '{actual}'"

    def test_survey_fill_invalid(self, survey_page: SurveyPage):
        survey_page.click_create_survey_button()
        survey_page.fill_data("a" * 256, "a" * 31, "a" * 51, "a" * 351)
        survey_page.click_continue()

        errors = survey_page.get_error_texts()
        for field, actual in errors.items():
            assert actual == "Сократите текст", f"{field}: expected 'Сократите текст', got '{actual}'"

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
