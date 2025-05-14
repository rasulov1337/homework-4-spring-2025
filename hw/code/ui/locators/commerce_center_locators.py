from selenium.webdriver.common.by import By


class CommerceCenterPageLocators:
    UNDERGO_TRAINING_BUTTON = (
        By.XPATH,
        '//button[@data-testid="ecomm-onboarding-start"]',
    )
    CLOSE_POPUP_BUTTON = (By.XPATH, '//div[@aria-label="Закрыть"]')
    TRAINING_OFFER_POPUP = (By.XPATH, '//h2[text()="Хотите пройти обучение?"]')
    CURRENT_POPUP = (By.XPATH, '//div[contains(@class, "ModalRoot_overlay")]')
    TRAINING_OFFER_POPUP_TRAIN_BUTTONS = (
        By.XPATH,
        '//div[contains(@class, "ModalRoot_overlay")]//div[@role="button"]',
    )
    CREATE_CATALOG = (By.XPATH, '//button[@data-testid="create-catalog"]')
    SIDEBAR_FORM = (By.XPATH, '//form[contains(@class, "ModalSidebarPage_container")]')

    class CommerceCenterSidebarFormLocators:
        CANCEL_BUTTON = (By.XPATH, '//button[@data-testid="cancel"]')
        NAME_INPUT = (By.XPATH, '//input[@data-testid="catalogName-input"]')
        CREATE_BUTTON = (By.XPATH, '//button[@data-testid="submit"]')
        MANDATORY_TO_FILL_TEXT = (By.XPATH, '//div[text()="Нужно заполнить"]')
        FEED_OR_COMMUNITY_BUTTON = (By.XPATH, '//div[@data-entityid="url"]')
        MARKETPLACE_BUTTON = (By.XPATH, '//div[@data-entityid="marketplace"]')
        MANUALLY_BUTTON = (By.XPATH, '//div[@data-entityid="file"]')
        LINK_TO_FEED_OR_COMMUNITY_INPUT = (
            By.XPATH,
            '//input[@data-testid="catalogUrl-input"]',
        )
        UPDATE_PERIOD_SELECT = (
            By.XPATH,
            '//input[@data-testid="catalogPeriod-select"]',
        )
        AUTOMATICALLY_DELETE_UTM_LABELS_TEXT = (
            By.XPATH,
            '//span[text()="Автоматически удалять UTM-метки"]',
        )
