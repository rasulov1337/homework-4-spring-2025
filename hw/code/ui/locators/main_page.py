from selenium.webdriver.common.by import By
from ..locators.base_page_locators import BasePageLocators


class MainPageLocators(BasePageLocators):
    NAVBAR_LOGIN_BTN_LOCATOR = (By.CSS_SELECTOR, '[class*="ButtonCabinet_primary"]')
    OAUTH_MAIL_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id="oAuthService_mail_ru"]')
    USERNAME_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[name="username"]')
    NEXT_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id="next-button"]')
    AUTH_PROBLEMS_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id="auth-problems"]')
    AUTH_BY_PASSWORD_BTN_LOCATOR = (By.CSS_SELECTOR, 'li[data-test-id="auth-by-password"] .fast-auth-item-text')
    PASSWORD_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input[name="password"]')
    SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-test-id="submit-button"]')

    # VIEW_ALL_CASES_BUTTON = (By.XPATH, "//a[contains(text(), 'Смотреть все') and @href]")

    # button names for this page

    VK_NEWS_BUTTON = "Новости"

    CASES_BUTTON = "Кейсы"

    IDEAS_FORUM_BUTTON = "Форум идей"

    MONETIZATION_BUTTON = "Монетизация"

    INFORMATION_BUTTON = "Справка"

    HELP_BUTTON = "Помощь"

    INSIGHTS_BUTTON = "Полезные материалы"

    EVENTS_BUTTON = "Мероприятия"

    VIDEO_COURSES_BUTTON = "Видеокурсы"

    CERTIFICATION_BUTTON = "Сертификация"

    DOCUMENTS_BUTTON = "Документы"

    EDUCATION_FOR_BUSINESS = "Обучение для бизнеса"

    EVENTS_BUTTON_SITE = "Подробнее"

    # main page links dict

    MAIN_PAGE_LINKS = {
        VK_NEWS_BUTTON: "/news",
        CASES_BUTTON: "/cases",
        IDEAS_FORUM_BUTTON: "/upvote",
        MONETIZATION_BUTTON: "/partner",
        INSIGHTS_BUTTON: "/insights",
        EVENTS_BUTTON: "/events",
        VIDEO_COURSES_BUTTON: "https://expert.vk.com/catalog/courses/",
        CERTIFICATION_BUTTON: "https://expert.vk.com/certification/",
        DOCUMENTS_BUTTON: "/documents",
        EDUCATION_FOR_BUSINESS: "https://expert.vk.com/",
        INFORMATION_BUTTON: "/help",
        HELP_BUTTON: "/help",
        EVENTS_BUTTON_SITE: "/events",
    }

    # unique buttons in header

    VK_ADS_LOGO = (By.XPATH, "//*[contains(@class, 'content_logo__')]")

    NAV_CABINET_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'NavigationVKAds_right__')]//*[contains(@class, 'ButtonCabinet_primary__')]",
    )

    @staticmethod
    def NAV_ITEM(href):
        return (
            By.XPATH,
            f"//*[contains(@class, 'item_link__') and contains(@href, '{href}')]",
        )

    # dropdown menu button

    NAV_EDUCATION_DROPDOWN_MENU_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'item_item__') and text()='Обучение']",
    )

    @staticmethod
    def NAV_DROPDOWN_MENU_ITEM(href):
        return (
            By.XPATH,
            f"//*[contains(@class, 'list_content__') and contains(@href, '{href}')]",
        )

    # company cases

    GET_ALL_CASES_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'styles_all__') and contains(@href, '/cases')]",
    )

    CASE_LINK = (
        By.XPATH,
        "//*[contains(@class, 'Case_link__')]",
    )

    CASE_TITLE = (
        By.XPATH,
        "//*[contains(@class, 'Case_title__')]",
    )

    CASE_NEW_TITLE = (
        By.XPATH,
        "//*[contains(@class, 'Summary_title__')]",
    )

    # webinars

    WEBINARS_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'GetStarted_button__')]",
    )

    # news

    NEWS_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'News_button__')]",
    )

    # footer buttons

    FOOTER_CABINET_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'Footer_leftContent__')]//*[contains(@class, 'ButtonCabinet_primary__')]",
    )

    @staticmethod
    def FOOTER_SECTIONS_ITEM(href):
        return (
            By.XPATH,
            f"//*[contains(@class, 'Footer_item__')]//*[contains(@href, '{href}')]",
        )