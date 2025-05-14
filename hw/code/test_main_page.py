from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base import NoAuthCase


class TestMainPage(NoAuthCase):
    def test_main_go_to_main_page_nav(self, main_page):
        main_page.click_vk_ads_logo()
        assert self.is_opened("https://ads.vk.com/")

    def test_main_go_to_news_page_nav(self, main_page):
        main_page.click_nav_item("Новости")
        assert self.is_opened("https://ads.vk.com/news")

    def test_main_go_to_insights_nav(self, main_page):
        main_page.open_education_dropdown()
        main_page.click_dropdown_item("Полезные материалы")
        assert self.is_opened("https://ads.vk.com/insights")

    def test_main_go_to_events_nav(self, main_page):
        main_page.open_education_dropdown()
        main_page.click_dropdown_item("Мероприятия")
        assert self.is_opened("https://ads.vk.com/events")

    def test_main_go_to_cases_nav(self, main_page):
        main_page.click_nav_item("Кейсы")
        assert self.is_opened("https://ads.vk.com/cases")

    def test_main_go_to_upvote_nav(self, main_page):
        main_page.click_nav_item("Форум идей")
        assert self.is_opened("https://ads.vk.com/upvote")

    def test_main_go_to_partner_nav(self, main_page):
        main_page.click_nav_item("Монетизация")
        assert self.is_opened("https://ads.vk.com/partner", check_new_tab=True)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_main_go_to_help_nav(self, main_page):
        main_page.click_nav_item("Справка")
        assert self.is_opened("https://ads.vk.com/help")

    def test_main_go_to_video_courses_nav(self, main_page):
        main_page.open_education_dropdown()
        main_page.click_dropdown_item("Видеокурсы")
        assert self.is_opened("https://expert.vk.com/catalog/courses/", check_new_tab=True)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_main_go_to_certification_nav(self, main_page):
        main_page.open_education_dropdown()
        main_page.click_dropdown_item("Сертификация")
        assert self.is_opened("https://expert.vk.com/certification/", check_new_tab=True)

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    #def test_main_click_promo_button_in_carousel(self, main_page): //TODO
    #def test_main_click_case_button_in_carousel(self, main_page): //TODO

    # def test_main_view_all_news_button(self, main_page):
    #     current_url = main_page.driver.current_url
    #     main_page.click_view_all_cases()
    #
    #     WebDriverWait(self.driver, 10).until(
    #         lambda d: d.current_url != current_url
    #     )
    #
    #     assert "ads.vk.com/cases" in self.driver.current_url.lower()
    #     assert "кейсы" in self.driver.title.lower()

    def test_main_view_all_cases_button(self, main_page):
        main_page.page_find_and_click_button("Смотреть все", button_index=1)
        assert self.is_opened("https://ads.vk.com/cases")

    def test_events_details_button(self, main_page):
        main_page.page_find_and_click_button("Подробнее", button_index=1)
        assert self.is_opened("https://ads.vk.com/events")

    def test_news_details_button(self, main_page):
        main_page.page_find_and_click_button("Подробнее", button_index=2)
        assert self.is_opened("https://ads.vk.com/news")

    def test_news_details_button_click(self, main_page):
        main_page.click_nav_item("Новости")
        main_page.page_find_and_click_button("Подробнее", button_index=1)
        assert self.is_opened("https://ads.vk.com/news/novyj-format-kollazh-sozdavajte-obyavleniya-s-raznymi-mediafajlami")

    def test_insights_details_button_click(self, main_page):
        main_page.open_education_dropdown()
        main_page.click_dropdown_item("Полезные материалы")

        main_page.page_find_and_click_button("Подробнее", button_index=1)
        assert self.is_opened("https://ads.vk.com/insights/reklama-kafe-i-restoranov")

    def test_events_details_button_click(self, main_page):
        main_page.open_education_dropdown()
        main_page.click_dropdown_item("Мероприятия")

        main_page.page_find_and_click_button("Под", button_index=1)
        assert self.is_opened("https://ads.vk.com/events/vybor-formata-obyavleniya-v-vk-reklame-vebinar-1505")

    def test_cases_details_button_click(self, main_page):
        main_page.click_nav_item("Кейсы")
        main_page.page_find_and_click_button("Подробнее", button_index=1)

        assert self.is_opened("https://ads.vk.com/cases/kak-prodavat-tury-s-pomoshchyu-kontenta-i-reklam-kejs-sogrin")

    #def test_upvote_search(self, main_page): //TODO

    def test_partner_help_button_click(self, main_page):
        original_window = self.driver.current_window_handle
        main_page.click_nav_item("Монетизация")

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body')))

        main_page.page_find_and_click_button("Справка", button_index=1)

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(3))

        new_windows = [w for w in self.driver.window_handles if w != original_window]
        self.driver.switch_to.window(new_windows[-1])  # Берем последнюю открытую

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("help/categories/partner"))

        assert "https://ads.vk.com/help/categories/partner" in self.driver.current_url

    #def test_partner_feedback_form(self, main_page): //TODO
    #def test_help_search_field(self, main_page): //TODO