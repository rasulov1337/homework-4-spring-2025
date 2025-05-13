from selenium.webdriver.common.keys import Keys
from ui.locators import main_locators
from ui.pages.base_page import BasePage
from consts import VK_URL


class MainPage(BasePage):
    url = VK_URL

    locators = main_locators.MainPageLocators()

    def search(self, query: str):
        self.click(self.locators.SHOW_SEARCH_INPUT_BUTTON)
        search_input = self.find(self.locators.SEARCH_INPUT)
        search_input.send_keys(query, Keys.RETURN)

    def open_info_about_lesson_at_day_of_week(self, day_of_week):
        self.click(self.locators.DAY_OF_WEEK_BUTTON(day_of_week))
        self.click(self.locators.MORE_INFO_ABOUT_CURRENT_LESSON_BUTTON)
