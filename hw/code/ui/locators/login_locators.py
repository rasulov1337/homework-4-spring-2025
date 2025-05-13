from selenium.webdriver.common.by import By


class LoginPageLocators:
    NAVBAR_LOGIN_BTN_LOCATOR = (By.CSS_SELECTOR, '[class*="ButtonCabinet_primary"]')
    OAUTH_MAIL_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id="oAuthService_mail_ru"]')
    USERNAME_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[name="username"]')
    NEXT_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id="next-button"]')
    AUTH_PROBLEMS_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id="auth-problems"]')
    AUTH_BY_PASSWORD_BTN_LOCATOR = (By.CSS_SELECTOR, 'li[data-test-id="auth-by-password"] .fast-auth-item-text')
    PASSWORD_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[name="password"]')
    SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id="submit-button"]')

