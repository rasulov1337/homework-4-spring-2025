from selenium.webdriver.common.by import By
from .left_menu_locators import LeftMenuLocators


class CompanyPageLocators:
    left_menu = LeftMenuLocators()

    LOGO = (By.CSS_SELECTOR, '[data-route=root]')

    CLOSE_HELP_MODAL_BTN_LOCATOR = (By.CSS_SELECTOR, '[role=button][aria-label=Закрыть]')

    COMPANIES_TYPES_DROPDOWN = (By.CSS_SELECTOR, '[data-testid="tags-selector"]')
    COMPANIES_DRAFTS = (By.XPATH, '//div[contains(@class, "TagSelector_menuList__")]/div[3]')
    COMPANY_DRAFT_NAME = (By.CSS_SELECTOR, '.nameCellContent_content__TyfEC > button')
    SAVE_DRAFT_COMPANY_MODAL = (By.XPATH, '//div[contains(@class, "ModalRoot_overlay__")]')
    SAVE_DRAFT_COMPANY_MODAL_CLOSE_BTN = (By.XPATH, '//div[contains(@class, "vkuiModalDismissButton")]')

    CREATE_COMPANY_BTN = (By.CSS_SELECTOR, '[data-testid="create-button"]')
    COMPANY_BUDGET_INPUT = (By.CSS_SELECTOR, '[data-testid="targeting-not-set"]')
    NEXT_BTN = (By.XPATH, "//*[contains(@class, 'CreateFooter_footerContentGroup__Hm+Yd')]/div/button")
    NEXT_BTN_WITH_ERROR = (By.XPATH, "//*[contains(@class, 'CreateFooter_footerContentGroup__Hm+Yd')]/div[2]/button")
    SAVE_COMPANY_BTN = (By.XPATH, "//span[contains(text(), 'Сохранить черновик')]")
    SAVE_DRAFT_COMPANY_BTN = (By.XPATH, "//button[contains(@class, 'ConfirmUsnavedChanges_button')]")
    ERROR_LOCATOR = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="1 ошибка"]')

    SITE_COMPANY_TARGET = (By.CSS_SELECTOR, '[data-id="site_conversions"]')
    SITE_URL_INPUT = (By.CSS_SELECTOR, '[placeholder="Вставьте ссылку или выберите из списка"]')

    NO_REGION_ERROR_LOCATOR = (By.XPATH, '//*[@id="react-collapsed-panel-1"]/fieldset/div/div/section')
    REGION_RUSSIA_BTN_LOCATOR = (By.XPATH, '//span[contains(@class, "vkuiButton__content") and text()="Россия"]')
    TARGET_LABEL_LOCATOR = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/div[2]/section/div/div/div/div/div/div[1]/div[1]')

    AD_HEADER_INPUT = (By.CSS_SELECTOR, '[data-testid="заголовок, макс. 40 символов"]')
    AD_SHORT_DECS_TEXTAREA = (By.CSS_SELECTOR, '[data-testid="описание, макс. 90 символов"]')

    CATALOG_SELECT_LOCATOR = (By.CSS_SELECTOR, '[data-testid="catalog-select"]')
    AD_CAROUSEL_TEXTAREA = (By.CSS_SELECTOR, '[data-testid="Дескрипшен для карусели, общий"]')
    AD_CARD_TEXTAREA = (By.CSS_SELECTOR, '[data-testid="Заголовок слайда динрем карусели"]')
    PUBLIC_LOCATOR = (By.XPATH, f'//span[text()="Опубликовать"]')
    COMPANY_SELECT_PUBLIC_BTN = (By.CSS_SELECTOR, '[data-testid="vk-owner-selector"]')
    ANOTHER_PUBLIC_BTN = (By.CSS_SELECTOR, '[data-testid="priced-goal"]')
    ADD_PUBLIC_INPUT = (By.XPATH, '//*[contains(@class, "AddGroupModal_input")]')
    ADD_PUBLIC_BTN = (By.XPATH, '//*[contains(@class, "vkuiModalCardBase")]')
    PRICE_DROPDOWN = (By.CSS_SELECTOR, '[data-testid="autobidding-mode"]')
    DELETE_COMPANY_BTN = (By.CSS_SELECTOR, '[data-testid="delete-button"]')
    SELECT_ALL_CHECKBOX = (By.ID, 'checkbox-all')


    @staticmethod
    def VK_UI_SELECT_ELEM(text):
        return (By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption')][text()='{text}']")
