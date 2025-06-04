from selenium.webdriver.common.by import By

from ui.locators.left_menu_locators import LeftMenuLocators


class AudiencePageLocators:
    left_menu = LeftMenuLocators()

    USERS_LIST_TAB_BTN = (By.ID, 'tab_audience.users_list')
    USERS_LIST_MENU_LOCATOR = (By.CSS_SELECTOR, '[data-testid=audience-item-menu]')
    USERS_LIST_MENU_ITEM_BTN = (By.CSS_SELECTOR, '[data-testid=dropdown-item]')
    USERS_LIST_UPLOAD_NEW_UBTN = (By.ID, 'tab-create-from-user-list-new')
    USERS_LIST_POPUP_ITEM_BTN = (By.XPATH, '//div[contains(@class, "DeleteUsersListConfirm")]//button')
    CREATE_USERS_LIST_BTN = (By.CSS_SELECTOR, '[data-testid=download-list]')
    CREATE_AUDIENCE_FROM_LIST_CHECK = (By.XPATH, "//div[contains(text(), 'Создать новую аудиторию после сохранения этого списка')]")
    CREATE_AUDIENCE_BTN = (By.CSS_SELECTOR, '[data-testid=create-audience]')
    AUDIENCE_NAME_INPUT = (By.CSS_SELECTOR, 'span.vkuiFormField > input')
    AUDIENCE_NAME_LOCATOR = (By.CSS_SELECTOR, '.NameCell_wrapper__hxqrL > h5')
    ADD_AUDIENCE_SRC_BTN = (By.CSS_SELECTOR, '.vkuiInternalGroup > div > div > button')
    NEW_USERS_LIST_NAME_INPUT = (By.CSS_SELECTOR, '[placeholder="Введите название списка"]')
    NEW_USERS_LIST_TYPE_SELECT = (By.CSS_SELECTOR, '.vkuiCustomSelect')
    NEW_USERS_LIST_FILE_INPUT = (By.CSS_SELECTOR, 'input[type=file]')
    SUBMIT_BTN = (By.CSS_SELECTOR, '[data-testid=submit]')
    SUCCESS_NOTIFY = (By.CSS_SELECTOR, '.vkuiSnackbar')
    USERS_LIST_NAME = (By.CSS_SELECTOR, '.EditableName_name__qWWXi > div')
    AUDIENCE_SRC = (By.CSS_SELECTOR, 'div.ModalSidebarPage_content__2mBu8 > section > div[role=button]')
    KEYWORDS_NAME_INPUT = (By.CSS_SELECTOR, '.SelectSourceModal_groupSourceWrapper__wAURc > div > span > input')
    KEYWORDS_TEXTAREA = (By.CSS_SELECTOR, '.KeyPhrases_textarea__wzycT > textarea')
    EXISTING_AUDIENCE_SELECT = (By.CSS_SELECTOR, '.vkuiCustomSelect')
    EXISTING_USERS_LIST_SELECT = (By.CSS_SELECTOR, '.vkuiCustomSelect')
    AUDIENCE_MENU_LOCATOR = (By.CSS_SELECTOR, '[data-testid=audience-item-menu]')
    AUDIENCE_MENU_ITEM_BTN = (By.CSS_SELECTOR, '[data-testid=dropdown-item]')
    AUDIENCE_LIST_POPUP_ITEM_BTN = (By.XPATH, '//div[contains(@class, "ModalConfirm_buttons")]//button')
    CREATE_AUDIENCE_SOURCE_MODAL = (By.XPATH, '//div[contains(@class, "ModalRoot_overlay__")]')


    @staticmethod
    def EXISTING_AUDIENCE_SELECT_ITEM(audience_name):
        return (By.XPATH, f"//*[contains(@class, 'Segment_option__79RaG')][text()='{audience_name}']")

    @staticmethod
    def NEW_USERS_LIST_TYPE_SELECT_ITEM(list_type):
        return By.CSS_SELECTOR, f'[role=option][title={list_type}]'

    @staticmethod
    def EXISTING_USERS_LIST_SELECT_ITEM(users_list_name):
        return (By.XPATH, f"//*[contains(@class, 'UsersListSelect_option__gUna1')][text()='{users_list_name}']")