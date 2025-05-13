from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_BUTTON = (By.XPATH, "//a[text()='вход / регистрация']")
    CONTINUE_WITH_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Продолжить с помощью почты и пароля']")
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    SEND_CREDENTIALS_BUTTON = (By.XPATH, "//button[text()='Войти с паролем']")