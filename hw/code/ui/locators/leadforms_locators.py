from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class LeadFormsPageLocators(BasePageLocators):
    CREATE_LEADFORM_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton') and text()='Создать лид-форму']")
    LEADFORM_TITLE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Текст заголовка')]")
    COMPANY_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Название компании')]")
    LEADFORM_DESCRIPTION_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите описание')]")
    LEADFORM_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Название лид-формы')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__') and text()='Удалить']")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(@data-testid, 'submit')]")
    BACK_BUTTON = (By.XPATH, "//button[contains(@data-testid, 'cancel')]")
    INPUT_NAME_LEAD_FORM = (By.XPATH, '//input[@placeholder="Название лид-формы"]')
    INPUT_NAME_COMPANY = (By.XPATH, '//input[@placeholder="Название компании"]')
    INPUT_TITLE = (By.XPATH, '//input[@placeholder="Текст заголовка"]')
    INPUT_DESCRIPTION = (By.XPATH, '//input[@placeholder="Введите описание"]')
    DOWNLOAD_LOGO = (By.XPATH, f"//*[@data-testid='set-global-image']")
    CHOOSE_LOGO = (By.XPATH, '//div[contains(@class, "ItemList_item__vc1Gb")]')
    ADD_CONTACTS_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiButton__content') and text()='Добавить контактные данные']")
    ADD_SITE_BUTTON = (By.XPATH, f"//*[contains(@class, 'vkuiTypography') and text()='Добавить сайт']")
    CONTACTS = (By.XPATH, '//input[@placeholder="Введите фамилию, имя и отчество"]')
    INPUT_LEGAL_ADRESS_COMPANY = (By.XPATH, '//input[@placeholder="Введите адрес"]')
    INPUT_FIND_LEADFORM = (By.XPATH, '//input[@placeholder="Поиск"]')
    SELECT_ALL_FORMS = (By.XPATH, "(//div[@data-key='checkbox']/input[contains(@class, 'simpleCheckbox_input')][0]")
    SELECT_ACTIONS_BUTTON = (By.XPATH, f'//input[@placeholder="Действия"]')
    DELETE_ACTION = (By.XPATH, "//div[contains(@class, 'vkuiCustomSelectOption__Children')]")
    
    @staticmethod
    def SELECT_FROM_LEADFORM_LIST(name: str):
        return By.CSS_SELECTOR, f'[data-testid="lead_form_name__{name}"]'






