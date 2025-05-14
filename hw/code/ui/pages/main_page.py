import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..pages.overview_page import OverviewPage
from ..locators.main_page import MainPageLocators
from ..pages.base_page import BasePage


class MainPage(BasePage):
    url = 'https://ads.vk.com/'
    locators = MainPageLocators()

    def login(self, username, password):
        self.click(self.locators.NAVBAR_LOGIN_BTN_LOCATOR)
        self.click(self.locators.OAUTH_MAIL_BTN_LOCATOR)

        username_input = self.find(self.locators.USERNAME_INPUT_LOCATOR)
        username_input.send_keys(username)

        self.click(self.locators.NEXT_BTN_LOCATOR)
        self.click(self.locators.AUTH_PROBLEMS_BTN_LOCATOR)
        self.click(self.locators.AUTH_BY_PASSWORD_BTN_LOCATOR)

        password_input = self.find(self.locators.PASSWORD_INPUT_LOCATOR)
        password_input.send_keys(password)

        self.click(self.locators.SUBMIT_BTN_LOCATOR)

        return OverviewPage(self.driver)

    def click_vk_ads_logo(self):
        self.click(self.locators.VK_ADS_LOGO)

    def click_nav_item(self, item_name: str):
        self.click(self.locators.NAV_ITEM(self.locators.MAIN_PAGE_LINKS[item_name]))

    def open_education_dropdown(self):
        self.click(self.locators.NAV_EDUCATION_DROPDOWN_MENU_BUTTON, timeout=1)

    def click_dropdown_item(self, item_name: str):
        self.click(
            self.locators.NAV_DROPDOWN_MENU_ITEM(
                self.locators.MAIN_PAGE_LINKS[item_name]
            )
        )

    # def click_view_all_cases(self):
    #     for _ in range(3):
    #         try:
    #             button = WebDriverWait(self.driver, 3).until(
    #                 EC.presence_of_element_located(self.locators.VIEW_ALL_CASES_BUTTON)
    #             )
    #             self.driver.execute_script(
    #                 "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
    #                 button
    #             )
    #             time.sleep(0.5)
    #
    #             WebDriverWait(self.driver, 5).until(
    #                 EC.element_to_be_clickable(self.locators.VIEW_ALL_CASES_BUTTON)
    #             ).click()
    #             return
    #
    #         except:
    #             self.driver.execute_script("window.scrollBy(0, 500);")
    #             time.sleep(0.5)

    def page_find_and_click_button(self, button_text, button_index=1, scroll_pause=0.8, max_scroll_attempts=5,
                              scroll_step=400):
        button_locator = (By.XPATH, f"(//*[contains(text(), '{button_text}')])[{button_index}]")

        for attempt in range(1, max_scroll_attempts + 1):
            try:
                # Пытаемся найти элемент
                button = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located(button_locator)
                )

                # Прокручиваем к элементу
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
                    button
                )
                time.sleep(scroll_pause)

                # Дожидаемся кликабельности
                button = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable(button_locator)
                )

                # Кликаем через ActionChains
                ActionChains(self.driver) \
                    .move_to_element(button) \
                    .pause(0.3) \
                    .click(button) \
                    .perform()

                print(f"Успешно кликнули кнопку '{button_text}' №{button_index}")
                return True

            except Exception as e:
                print(f"Попытка {attempt}: кнопка не найдена. Прокручиваем страницу...")
                self.driver.execute_script(f"window.scrollBy(0, {scroll_step});")
                time.sleep(scroll_pause)

                if attempt == max_scroll_attempts:
                    available_buttons = len(self.driver.find_elements(
                        By.XPATH, f"//*[contains(text(), '{button_text}')]"
                    ))
                    raise Exception(
                        f"Не удалось найти кнопку '{button_text}' №{button_index}. "
                        f"Всего найдено таких кнопок: {available_buttons}. "
                        f"Ошибка: {str(e)}"
                    )