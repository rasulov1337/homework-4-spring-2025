from selenium.webdriver.common.by import By


class CommerceCenterPageLocators:
    UNDERGO_TRAINING_BUTTON = (By.XPATH, '//button[@data-testid="ecomm-onboarding-start"]')
    CLOSE_POPUP_BUTTON = (By.XPATH, '//div[@aria-label="Закрыть"]')
    TRAINING_OFFER_POPUP = (By.XPATH, '//h2[text()="Хотите пройти обучение?"]')
    CURRENT_POPUP = (By.XPATH, '//div[contains(@class, "ModalRoot_overlay")]')
    TRAINING_OFFER_POPUP_TRAIN_BUTTONS = (By.XPATH, '//div[contains(@class, "ModalRoot_overlay")]//div[@role="button"]')

