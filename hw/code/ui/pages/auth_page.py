from ui.pages.base_page import BasePage
from ui.locators.auth_page_locators import AuthPageLocators


class AuthPage(BasePage):
    locators = AuthPageLocators()
    url = "https://ads.vk.com/"

    def login(self, login, password):
        self.click(self.locators.MAIL_RU_AUTH_BUTTON)
        login_input = self.find_interactable(self.locators.MAIL_RU_LOGIN)
        login_input.clear()
        login_input.send_keys(login)

        self.find_interactable(self.locators.MAIL_RU_LOGIN)
        print(self.locators.MAIL_RU_LOGIN)
        print(self.locators.MAIL_RU_NEXT_BUTTON)
        self.click(self.locators.MAIL_RU_NEXT_BUTTON)

        password_input = self.find_interactable(self.locators.MAIL_RU_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)

        self.click(self.locators.MAIL_RU_SUBMIT_BUTTON)