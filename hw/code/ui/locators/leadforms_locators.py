from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class LeadFormsPageLocators(BasePageLocators):
    CREATE_LEADFORM_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton') and text()='Создать лид-форму']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__') and text()='Удалить']")

    LOAD_IMAGE_BUTTON = (By.XPATH, "//*[contains(@data-testid, 'set-global-image')]")
    LOAD_IMAGE_INPUT = (By.XPATH, "//input[@type='file']")
    UPLOADED_IMAGE_ITEM = (By.XPATH, "//*[contains(@class, 'ItemList_item__')]")
    UPLOADED_IMAGE_NAME = (By.XPATH, "//*[contains(@class, 'ImageItem_name__')]")

    EDIT_IMAGES_BUTTON = (By.XPATH, "//button[contains(@aria-label, 'Edit')]")
    SELECT_ALL_IMAGES_BUTTON = (By.XPATH, "//*[contains(@class, 'EditControl_selection__')]//*[text()='Выбрать все']")

    DELETE_IMAGES_BUTTON = (By.XPATH, "//button[contains(@data-testid, 'delete')]")

    CONTINUE_BUTTON = (By.XPATH, "//button[contains(@data-testid, 'submit')]")

    MORE_TEXT_BUTTON = (By.XPATH, "//label[h4[div[span[contains(text(), 'Больше текста')]]]]")
    MAGNET_BUTTON = (By.XPATH, "//label[h4[div[span[contains(text(), 'Лид-магнит')]]]]")
    MAGNET_BONUS_BUTTON = (By.XPATH, "//label[div[div[div[span[contains(text(), 'Бонус')]]]]]")
    MAGNET_SALE_BUTTON = (By.XPATH, "//label[div[div[div[span[contains(text(), 'Скидка')]]]]]")
    MAGNET_SALE_PERCENT_BUTTON = (By.XPATH, "//h4[contains(text(), '%')]")

    LEADFORM_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Название лид-формы')]")
    COMPANY_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Название компании')]")
    LEADFORM_TITLE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Текст заголовка')]")
    LEADFORM_DESCRIPTION_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите описание')]")
    MORE_TEXT_INPUT = (By.XPATH, "//textarea[@placeholder='Расскажите о вашем предложении']")
    MAGNET_BONUS_INPUT = (By.XPATH, "//input[@placeholder='Бонус']")
    MAGNET_SALE_INPUT = (By.XPATH, "(//input[contains(@class, 'vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none')])[4]")

    ERROR_1_NAME = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Название лид-формы']]]")
    ERROR_1_HEADING = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Название компании']]]")
    ERROR_1_COMPANY = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Текст заголовка']]]")
    ERROR_1_DESCRIPTION = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Введите описание']]]")
    ERROR_1_LOGO = (By.XPATH, "//span[preceding-sibling::div[@class='vkuiSimpleCell vkuiSimpleCell--sizeY-none vkuiCellButton vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible']]")
    ERROR_MORE_TEXT = (By.XPATH, "//span[preceding-sibling::span[textarea[@placeholder='Расскажите о вашем предложении']]]")
    ERROR_1_MAGNET_BONUS = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Бонус']]]")
    ERROR_1_MAGNET_SALE_ZERO = (By.XPATH, "//div[contains(text(), 'Значение должно быть больше нуля')]")
    ERROR_1_MAGNET_SALE_OVER = (By.XPATH, "//div[contains(text(), 'Укажите скидку не больше 100%')]")

    ADD_CONTACT_BUTTON = (By.XPATH, "//button[contains(@class, 'Questions_addContactFieldsBtn__')]")
    BIN_NAME_BUTTON = (By.XPATH, "//button[@data-id='first_name']")
    BIN_PHONE_BUTTON = (By.XPATH, "//button[@data-id='phone']")
    ADD_SELECTED_CONTACTS_BUTTON = (By.XPATH, "//span[contains(text(), 'Добавить')]")

    

    NAME_CONTACT = (By.XPATH, "//span[contains(text(), 'Имя')]")
    PHONE_CONTACT = (By.XPATH, "//span[contains(text(), 'Номер телефона')]")
    EMAIL_CONTACT = (By.XPATH, "//span[contains(text(), 'Электронная почта')]")
    LINK_CONTACT = (By.XPATH, "//span[contains(text(), 'Cсылка на соцсеть')]")
    BIRTHDAY_CONTACT = (By.XPATH, "//span[contains(text(), 'День рождения')]")
    CITY_CONTACT = (By.XPATH, "//span[contains(text(), 'Город')]")

    SELECT_QUESTION_TYPE_BUTTON = (By.XPATH, "//div[contains(text(), 'Выбор одного ответа')]")
    MULTIPLE_ANSWERS_BUTTON = (By.XPATH, "//span[contains(text(), 'Выбор нескольких ответов')]")
    USER_ANSWER_BUTTON = (By.XPATH, "//span[contains(text(), 'Ответ в произвольной форме')]")

    ERROR_2_QUESTION = (By.XPATH, "//div[@class='Hint_hintTrigger__ixYRu Question_errorIconWrap__0UsDI']")
    ERROR_2_CONTACT = (By.XPATH, "(//p[@class='vkuiTypography vkuiTypography--normalize vkuiBanner__text vkuiText vkuiText--sizeY-none'])[2]")

    QUESTION_INPUT = (By.XPATH, "//textarea[@placeholder='Напишите вопрос']")
    ANSWER_1_INPUT = (By.XPATH, "(//input[@placeholder='Введите ответ'])[1]")
    ANSWER_2_INPUT = (By.XPATH, "(//input[@placeholder='Введите ответ'])[2]")
    ANSWER_3_INPUT = (By.XPATH, "(//input[@placeholder='Введите ответ'])[3]")

    HEADING_INPUT = (By.XPATH, "(//input[contains(@class, 'vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none')])[1]")
    INPUT_3_HEADING_ALT = (By.XPATH, "(//input[@class='vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none'])[1]")
    DESCRIPTION_3_INPUT = (By.XPATH, "(//input[contains(@class, 'vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none')])[2]")
    SITE_INPUT = (By.XPATH, "(//input[@class='vkuiTypography vkuiInput__el vkuiText vkuiText--sizeY-none'])[3]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='+7......']")
    PROMOCODE_INPUT = (By.XPATH, "//input[@placeholder='Введите промокод']")

    SITE_BUTTON = (By.XPATH, "//span[contains(text(), 'Добавить сайт')]")
    PHONE_BUTTON = (By.XPATH, "//span[contains(text(), 'Добавить телефон')]")
    PROMOCODE_BUTTON = (By.XPATH, "//span[contains(text(), 'Добавить промокод')]")

    ERROR_3_HEADING = (By.XPATH, "(//span[@class='vkuiTypography vkuiTypography--normalize vkuiFormItem__bottom vkuiFootnote'])[1]")
    ERROR_3_DESCRIPTION = (By.XPATH, "(//span[@class='vkuiTypography vkuiTypography--normalize vkuiFormItem__bottom vkuiFootnote'])[2]")
    ERROR_3_SITE = (By.XPATH, "(//span[@class='vkuiTypography vkuiTypography--normalize vkuiFormItem__bottom vkuiFootnote'])[3]")
    ERROR_3_PHONE = (By.XPATH, "(//span[@class='vkuiTypography vkuiTypography--normalize vkuiFormItem__bottom vkuiFootnote'])[4]")
    ERROR_3_PROMO = (By.XPATH, "(//span[@class='vkuiTypography vkuiTypography--normalize vkuiFormItem__bottom vkuiFootnote'])[5]")

    NOTIFY_EMAIL_BUTTON = (By.XPATH, "(//label[contains(@class, 'vkuiCheckbox vkuiCheckbox--sizeY-none vkuiTappable vkuiInternalTappable vkuiTappable--hasHover vkuiTappable--hasActive vkui-focus-visible')])[1]")

    NAME_4_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите фамилию, имя и отчество')]")
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите адрес')]")
    EMAIL_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите email')]")
    INN_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Введите ИНН')]")
    NOTIFY_EMAIL_INPUT = (By.XPATH, "//input[contains(@placeholder, 'email@example.com')]")

    ERROR_4_NAME = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Введите фамилию, имя и отчество']]]")
    ERROR_4_ADDRESS = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Введите адрес']]]")
    ERROR_4_EMAIL = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Введите email']]]")
    ERROR_4_INN = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='Введите ИНН']]]")
    ERROR_4_NOTIFY_EMAIL = (By.XPATH, "//span[preceding-sibling::span[input[@placeholder='email@example.com']]]")

    ADD_QUESTION_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__') and text()='Добавить вопрос']")
    ADD_ANSWER_BUTTON = (By.XPATH, "//*[contains(@class, 'Question_addAnswerLine__')]/button")

    CREATED_LEAD_FORM = (By.XPATH, "//div[contains(@class, 'BaseTable__body')]")
    ARCHIVE_BUTTON = (By.XPATH, "//span[contains(text(), 'Архивировать')]")
    ARCHIVE_ACCEPT_BUTTON = (By.XPATH, "//span[contains(text(), 'Архивировать')]")

    FIRST_LEAD_FORM_NAME = (By.XPATH, "(//h5[contains(@data-testid, 'lead_form_name__')])[1]")

    UPLOAD_IMAGE_MODAL = (By.XPATH, "(//div[contains(@class, 'ModalSidebarPage_control')])[2]")


