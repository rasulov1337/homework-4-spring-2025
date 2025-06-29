from selenium.webdriver.common.by import By

from ui.locators.left_menu_locators import LeftMenuLocators


class AudiencePageLocators(LeftMenuLocators):

    USERS_LIST_TAB_BTN = (By.ID, "tab_audience.users_list")
    USERS_LIST_MENU_LOCATOR = (By.CSS_SELECTOR, "[data-testid=audience-item-menu]")
    USERS_LIST_MENU_ITEM_BTN = (By.CSS_SELECTOR, "[data-testid=dropdown-item]")
    USERS_LIST_UPLOAD_NEW_UBTN = (By.ID, "tab-create-from-user-list-new")
    USERS_LIST_POPUP_ITEM_BTN = (
        By.XPATH,
        '//div[contains(@class, "DeleteUsersListConfirm")]//button',
    )
    CREATE_USERS_LIST_BTN = (By.CSS_SELECTOR, "[data-testid=download-list]")
    CREATE_AUDIENCE_FROM_LIST_CHECK = (
        By.XPATH,
        "//div[contains(text(), 'Создать новую аудиторию после сохранения этого списка')]",
    )
    CREATE_AUDIENCE_BTN = (By.XPATH, '//button[@data-testid="create-audience"]')
    AUDIENCE_NAME_INPUT = (By.XPATH, '//input[@type="text"]')
    AUDIENCE_NAME_LOCATOR = (By.CSS_SELECTOR, "[data-testid=name-link] > span")
    ADD_AUDIENCE_SRC_BTN = (By.XPATH, '//button[@data-testid="add-source"]')
    CLOSE_MODAL_BUTTON = (By.XPATH, '//button[@aria-label="Close"]')
    NEW_USERS_LIST_NAME_INPUT = (
        By.CSS_SELECTOR,
        '[placeholder="Введите название списка"]',
    )
    NEW_USERS_LIST_TYPE_SELECT = (
        By.XPATH,
        '//div//input[@type="text" and @role="combobox"]',
    )
    NEW_USERS_LIST_TYPE_EMAIL = (By.XPATH, '//div[contains(text(), "Email")]')
    NEW_USERS_LIST_FILE_INPUT = (By.CSS_SELECTOR, "input[type=file]")
    SUBMIT_BTN = (By.XPATH, '//button[@data-testid="submit"]')
    SUCCESS_NOTIFY = (By.CSS_SELECTOR, ".vkuiSnackbar")
    USERS_LIST_NAME = (By.CSS_SELECTOR, "div.vkuiCustomSelectInput__container > input")
    ALREADY_EXIST = (By.XPATH, '//div[@data-testid="existsAudience"]')
    KEYWORD = (By.CSS_SELECTOR, "[data-testid=context]")
    KEYWORDS_NAME_INPUT = (By.CSS_SELECTOR, "[data-testid=name]")
    KEYWORDS_TEXTAREA = (By.CSS_SELECTOR, "[data-testid=positive-phrases]")
    KEYWORD_IN_AUDIENCE = (By.XPATH, "//span[text()='Ключевые фразы']")
    PARSED_KEYWORDS_DIV = (
        By.XPATH,
        '//*[contains(@data-testid, "positive-phrases")]//*[@data-testid="content"]',
    )
    KEYWORDS_LIST = (By.XPATH, '//div[@data-testid="content"]')
    EXISTING_AUDIENCE_SELECT = (By.CSS_SELECTOR, ".vkuiCustomSelect")
    EXISTING_USERS_LIST_SELECT = (By.CSS_SELECTOR, ".vkuiCustomSelect")
    AUDIENCE_MENU_LOCATOR = (By.CSS_SELECTOR, "[data-testid=audience-item-menu]")
    AUDIENCE_MENU_DELETE_BTN = (
        By.XPATH,
        '//*[@data-testid="dropdown-item"][.//span[contains(text(), "Удалить")]]',
    )
    AUDIENCE_LIST_POPUP_CONFIRM_DELETION_BTN = (
        By.XPATH,
        '//button[span[span[text()="Удалить"]]]',
    )
    CREATE_AUDIENCE_SOURCE_MODAL = (
        By.XPATH,
        '//div[contains(@class, "ModalRoot_overlay__")]',
    )
    USER_LIST = (By.XPATH, "//span[text()='Список пользователей']")
    USER_LIST_NAME = (
        By.XPATH,
        '//span[.//*[text()="Название"]]//*[@data-testid="content"]',
    )
    NEW_USERS_LIST_NAME_PREVIEW = (
        By.XPATH,
        '//div[contains(@class, "BaseTable__row-cell")]//div[contains(text(), "USER LIST")]',
    )
    NEW_USERS_LIST_TYPE_PREVIEW = (
        By.XPATH,
        '//div[contains(@class, "BaseTable__row-cell")]//div[contains(text(), "Email")]',
    )

    @staticmethod
    def EXISTING_AUDIENCE_SELECT_ITEM(audience_name):
        return (
            By.XPATH,
            f"//*[contains(@class, 'Segment_option')][text()='{audience_name}']",
        )

    @staticmethod
    def EXISTING_USERS_LIST_SELECT_ITEM(users_list_name):
        return (
            By.XPATH,
            f"//*[contains(@class, 'UsersListSelect_option')][text()='{users_list_name}']",
        )

    def EXISTING_AUDIENCE_SELECTED(self, name):
        return (By.XPATH, f'//span[text()="{name}"]')

    def EXISTING_AUDIENCE_CONFIRMED(self, name):
        return (
            By.XPATH,
            f'//div[@data-testid="content"][.//text()[contains(., "{name}")]]',
        )
