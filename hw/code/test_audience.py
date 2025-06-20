from base import BaseCase
from ui.pages.audience_page import AudiencePage, AudienceSource


class TestAudience(BaseCase):
    USERS_LIST_NAME = "USER LIST"
    USERS_LIST_TYPE = "Email"
    ALREADY_CREATED_AUDITORY_TEXT = f"[auto] Список пользователей / {USERS_LIST_NAME}"
    AUDIENCE_NAME = "AUDIENCE"
    EXISTING_AUDIENCE = "EXISTING_AUDIENCE"

    def test_create_users_list(self, audience_page: AudiencePage):
        audience_page.open_users_list_list()
        audience_page.open_users_list_creation()

        users_list_path = self.config["users_list_path"]

        audience_page.create_audience_from_list()
        audience_page.load_new_users_list(
            self.USERS_LIST_NAME, self.USERS_LIST_TYPE, users_list_path
        )

        assert audience_page.get_users_list_name_preview() == self.USERS_LIST_NAME
        assert audience_page.get_users_list_type_preview() == self.USERS_LIST_TYPE
        audience_page.submit_users_list_creation()
        audience_page.wait_for_success_notify()

        users_lists = audience_page.get_users_lists()
        assert len(users_lists) == 1
        assert self.USERS_LIST_NAME in users_lists

    def test_audience_from_uploading_users_list(self, audience_page: AudiencePage):
        audience_page.open_users_list_list()
        audience_page.open_users_list_creation()

        users_list_path = self.config["users_list_path"]

        audience_page.load_new_users_list(
            self.USERS_LIST_NAME, self.USERS_LIST_TYPE, users_list_path
        )
        audience_page.submit_users_list_creation()
        audience_page.wait_for_success_notify()

        audience_page.open_audiences_list()
        audiences = audience_page.get_audiences()
        assert len(audiences) == 1
        assert f"[auto] Список пользователей / {self.USERS_LIST_NAME}" in audiences

        audience_page.click_created_audience(self.USERS_LIST_NAME)

        users_list_name = audience_page.get_users_list_name()
        assert users_list_name == self.USERS_LIST_NAME

    def test_audience_from_keywords(self, audience_page: AudiencePage):
        audience_page.open_audience_creation()

        audience_page.set_audience_name(self.AUDIENCE_NAME)

        audience_page.open_sources_list()
        audience_page.select_audience_source(AudienceSource.KEYWORDS)

        keywords_name = "KEYWORDS"

        with open(self.config["keywords_path"], "r", encoding="utf-8") as keywords_file:
            keywords = set([kw.strip().lower() for kw in keywords_file.readlines()])
            audience_page.add_key_words(keywords_name, keywords)

        texts = audience_page.get_keywords_displayed()
        assert set(texts) == keywords, "Не все ключевые слова отображаются в списке"

        audience_page.submit_audience_source()
        parsed_keywords_set = audience_page.get_parsed_keywords_set()
        assert parsed_keywords_set.issubset(keywords)
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

        audience_page.add_existing_audience(self.ALREADY_CREATED_AUDITORY_TEXT)
        existing_auditory_selected = audience_page.get_existing_audience_selected(
            self.ALREADY_CREATED_AUDITORY_TEXT
        )
        assert existing_auditory_selected == self.ALREADY_CREATED_AUDITORY_TEXT
        audience_page.submit_audience_source()

        existing_audience_confirmed = audience_page.get_existing_audience_confirmed(
            self.ALREADY_CREATED_AUDITORY_TEXT
        )
        assert existing_audience_confirmed == self.ALREADY_CREATED_AUDITORY_TEXT
        audience_page.submit_audience_creation()

        audience_page.wait_audience_list_for_load()
        audiences = audience_page.get_audiences()
        assert len(audiences) == 2
        assert self.AUDIENCE_NAME in audiences
