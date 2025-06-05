from base import BaseCase
from ui.pages.audience_page import AudiencePage, AudienceSource


class TestAudience(BaseCase):
    ALREADY_CREATED_AUDITORY = "Уже созданная аудитория"
    AUDIENCE_NAME = "AUDIENCE"
    EXISTING_AUDIENCE = "EXISTING_AUDIENCE"

    def test_create_users_list(self, audience_page: AudiencePage):
        audience_page.open_users_list_list()
        audience_page.open_users_list_creation()

        users_list_name = "USER LIST"
        users_list_type = "Email"
        users_list_path = self.config["users_list_path"]

        audience_page.create_audience_from_list()
        audience_page.load_new_users_list(
            users_list_name, users_list_type, users_list_path
        )

        assert users_list_name in audience_page.driver.page_source
        assert users_list_type in audience_page.driver.page_source
        audience_page.submit_users_list_creation()
        audience_page.wait_for_success_notify()

        users_lists = audience_page.get_users_lists()
        assert len(users_lists) == 1
        assert users_list_name in users_lists

    def test_audience_from_uploading_users_list(self, audience_page: AudiencePage):
        audience_page.open_users_list_list()
        audience_page.open_users_list_creation()

        users_list_name = "USER LIST"
        users_list_type = "Email"
        users_list_path = self.config["users_list_path"]

        audience_page.load_new_users_list(
            users_list_name, users_list_type, users_list_path
        )
        audience_page.create_audience_from_list()
        audience_page.submit_users_list_creation()
        audience_page.wait_for_success_notify()

        audience_page.open_audiences_list()
        audiences = audience_page.get_audiences()
        assert len(audiences) == 1
        assert f"[auto] Список пользователей / {users_list_name}" in audiences

        audience_page.click_created_audience(users_list_name)

        assert (
            audience_page.has_users_list_source()
        ), "Источник 'Список пользователей' не найден в аудитории"

    def test_audience_from_keywords(self, audience_page: AudiencePage):
        audience_page.open_audience_creation()

        audience_page.set_audience_name(self.AUDIENCE_NAME)

        audience_page.open_sources_list()
        audience_page.select_audience_source(AudienceSource.KEYWORDS)

        keywords_name = "KEYWORDS"

        with open(self.config["keywords_path"], "r", encoding="utf-8") as keywords_file:
            keywords = keywords_file.readlines()
            audience_page.add_key_words(keywords_name, keywords)

            for keyword in keywords:
                assert keyword in audience_page.driver.page_source

        audience_page.submit_audience_source()
        assert keywords_name in audience_page.driver.page_source
        audience_page.submit_audience_creation()

        audiences = audience_page.get_audiences()
        assert len(audiences) == 1
        assert self.AUDIENCE_NAME in audiences

    def test_audience_from_existing_audience(
        self, audience_page: AudiencePage, setup_existing_audience
    ):
        audience_page.open_audience_creation()
        audience_page.set_audience_name(self.AUDIENCE_NAME)
        audience_page.open_sources_list()
        audience_page.select_audience_source(AudienceSource.EXISTING)

        audience_page.add_existing_audience(self.EXISTING_AUDIENCE)
        assert self.EXISTING_AUDIENCE in audience_page.driver.page_source
        audience_page.submit_audience_source()
        assert self.ALREADY_CREATED_AUDITORY in audience_page.driver.page_source
        audience_page.submit_audience_creation()

        audience_page.wait_audience_list_for_load()
        audiences = audience_page.get_audiences()
        assert len(audiences) == 2
        assert self.AUDIENCE_NAME in audiences
