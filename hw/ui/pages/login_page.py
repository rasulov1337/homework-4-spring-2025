from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginPageLocators
from selenium.common.exceptions import ElementClickInterceptedException

class LoginPage(BasePage):
    url = 'https://education.vk.company/'
    authorize = False
    locators = LoginPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.is_opened()
        self.driver.set_page_load_timeout(15)


    def login(self, email, password):
        try:
            self.click(LoginPageLocators.LOGIN_BUTTON)
        except ElementClickInterceptedException:  # Some kind of bug. The only way to fix that is use this construction
            pass

        self.click(self.locators.CONTINUE_WITH_PASSWORD_BUTTON)
        self.find(self.locators.EMAIL_INPUT).send_keys(email)
        self.find(self.locators.PASSWORD_INPUT).send_keys(password)
        self.click(self.locators.SEND_CREDENTIALS_BUTTON)
