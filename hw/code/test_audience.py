from base import BaseCase
from ui.pages.audience_page import AudiencePage, AudienceSource


class TestAudience(BaseCase):
    def setup_method(self, method):
        if method.__name__ == 'test_audience_from_existing_audience':
            self.audience_page = AudiencePage(self.driver)

            users_list_name = "USER LIST"
            users_list_type = "Email"
            users_list_path = self.config['users_list_path']

            audience_name = 'EXISTING_AUDIENCE'
            self.audience_page.open_audience_creation()
            self.audience_page.set_audience_name(audience_name)
            self.audience_page.open_sources_list()
            self.audience_page.select_audience_source(AudienceSource.USERS_LIST)
            self.audience_page.click_upload_new_users_list()
            self.audience_page.load_new_users_list(users_list_name, users_list_type, users_list_path)
            self.audience_page.submit_audience_source()
            self.audience_page.wait_for_success_notify()
            self.audience_page.submit_audience_creation()
            self.audience_page.wait_audience_list_for_load()

    def teardown_method(self, method):
        AudiencePage(self.driver).open_users_list_list()
        AudiencePage(self.driver).clear_users_lists()
        AudiencePage(self.driver).open_audiences_list()
        AudiencePage(self.driver).clear_audiences()

    def test_create_users_list(self, audience_page: AudiencePage):
        audience_page.open_users_list_list()
        audience_page.open_users_list_creation()

        users_list_name = "USER LIST"
        users_list_type = "Email"
        users_list_path = self.config['users_list_path']

        audience_page.create_audience_from_list()
        audience_page.load_new_users_list(users_list_name, users_list_type, users_list_path)

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
        users_list_path = self.config['users_list_path']

        audience_page.load_new_users_list(users_list_name, users_list_type, users_list_path)
        audience_page.create_audience_from_list()
        audience_page.submit_users_list_creation()
        audience_page.wait_for_success_notify()

        audience_page.open_audiences_list()
        audiences = audience_page.get_audiences()
        assert len(audiences) == 1
        assert f'[auto] Список пользователей / {users_list_name}' in audiences

        audience_page.click_created_audience(users_list_name)

        assert audience_page.has_users_list_source(), "Источник 'Список пользователей' не найден в аудитории"

    def test_audience_from_keywords(self, audience_page: AudiencePage):
        audience_page.open_audience_creation()

        audience_name = 'AUDIENCE'
        audience_page.set_audience_name(audience_name)

        audience_page.open_sources_list()
        audience_page.select_audience_source(AudienceSource.KEYWORDS)

        keywords_name = 'KEYWORDS'

        with open(self.config['keywords_path'], 'r', encoding='utf-8') as keywords_file:
            keywords = keywords_file.readlines()
            audience_page.add_key_words(keywords_name, keywords)

            for keyword in keywords:
                assert keyword in audience_page.driver.page_source

        audience_page.submit_audience_source()
        assert keywords_name in audience_page.driver.page_source
        audience_page.submit_audience_creation()

        audiences = audience_page.get_audiences()
        assert len(audiences) == 1
        assert audience_name in audiences

    def test_audience_from_existing_audience(self):
        audience_name = 'AUDIENCE'

        self.audience_page.open_audience_creation()
        self.audience_page.set_audience_name(audience_name)
        self.audience_page.open_sources_list()
        self.audience_page.select_audience_source(AudienceSource.EXISTING)

        self.audience_page.add_existing_audience("EXISTING_AUDIENCE")
        assert "EXISTING_AUDIENCE" in self.audience_page.driver.page_source
        self.audience_page.submit_audience_source()
        assert "Уже созданная аудитория" in self.audience_page.driver.page_source
        self.audience_page.submit_audience_creation()

        self.audience_page.wait_audience_list_for_load()
        audiences = self.audience_page.get_audiences()
        assert len(audiences) == 2
        assert audience_name in audiences