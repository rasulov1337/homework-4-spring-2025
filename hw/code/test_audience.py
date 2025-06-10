from base import BaseCase
from ui.pages.audience_page import AudiencePage, AudienceSource


class TestAudience(BaseCase):
    USERS_LIST_NAME = "USER LIST"
    ALREADY_CREATED_AUDITORY = f"[auto] Список пользователей / {USERS_LIST_NAME}"
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

        assert audience_page.get_users_list_name_preview() == users_list_name
        assert audience_page.get_users_list_type_preview() == users_list_type
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

        assert audience_page.are_keywords_displayed(keywords), "Не все ключевые слова отображаются в списке"

        audience_page.submit_audience_source()
        assert audience_page.is_keyword_list_named(keywords_name), "Название набора ключевых слов не отображается"
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

        audience_page.add_existing_audience(self.ALREADY_CREATED_AUDITORY)
        assert audience_page.is_existing_audience_selected(self.ALREADY_CREATED_AUDITORY), \
            f"Не отображается выбранная аудитория: {self.ALREADY_CREATED_AUDITORY}"
        audience_page.submit_audience_source()
        assert audience_page.is_existing_audience_confirmed(self.ALREADY_CREATED_AUDITORY), \
            f"Подтверждение аудитории не отображается: {self.ALREADY_CREATED_AUDITORY}"
        audience_page.submit_audience_creation()

        audience_page.wait_audience_list_for_load()
        audiences = audience_page.get_audiences()
        assert len(audiences) == 2
        assert self.AUDIENCE_NAME in audiences
