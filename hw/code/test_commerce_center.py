from base import BaseCase
from ui.pages.commerce_center_page import CommerceCenterPage
from selenium.webdriver.support import expected_conditions as EC


class TestCommerceCenter(BaseCase):
    authorize = True

    CREATE_CATALOG_TEXT = "Создать каталог с подсказками"
    WATCH_VIDEO_TEXT = "Смотреть видеоурок от экспертов VK"
    WATCH_COURSE_TEXT = "Смотреть курс на обучающей платформе"
    NEW_CATALOG_TEXT = "Новый каталог"
    NEEDS_FILLING_TEXT = "Нужно заполнить"
    OZON_SELLER_LINK = "https://www.ozon.ru/seller/g-point-806219/"
    OZON_CLIENT_ID = "806219"
    VK_COMMUNITY_WITH_GOODS_LINK = "https://vk.com/club230422504"
    VK_COMMUNITY_WITHOUT_GOODS_LINK = "https://vk.com/vkeducation"
    NOT_ENOUGH_GOODS_TEXT = "В этом сообществе недостаточно товаров или услуг"
    INVALID_HTTP_INPUT_VALUE = "not a http"
    NOT_HTTP_LINK_TEXT = "Необходимо указать протокол http(s)"
    CATALOG_NAME_TEXT = "Some Name"
    WRONG_API_KEY_TEXT = "Указан неверный ключ"
    WRONG_CLIENT_ID_VALUE = "123"
    WRONG_API_KEY_VALUE = "123"

    def test_show_modal_education(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.click_undergo_training()
        commerce_center_page.close_popup()
        training_variants = commerce_center_page.find_all(
            commerce_center_page.locators.TRAINING_OFFER_POPUP_TRAIN_BUTTONS
        )
        assert self.CREATE_CATALOG_TEXT in training_variants[0].text
        assert self.WATCH_VIDEO_TEXT in training_variants[1].text
        assert self.WATCH_COURSE_TEXT in training_variants[2].text

    def test_close_modal_education(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.click_undergo_training()
        commerce_center_page.close_popup()
        popup = commerce_center_page.find(commerce_center_page.locators.CURRENT_POPUP)
        assert popup

    def test_catalog_sidebar_form(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.open_catalog_creation_form()

        sidebar_form_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert self.NEW_CATALOG_TEXT in sidebar_form_text

    def test_close_catalog_sidebar_form(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.close_catalog_creation_form()
        assert commerce_center_page.became_invisible(
            commerce_center_page.locators.SIDEBAR_FORM, timeout=2
        )

    def test_catalog_form_name_empty(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.clear_catalogue_name()
        commerce_center_page.click(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.NAME_INPUT
        )
        commerce_center_page.click(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.CREATE_BUTTON
        )
        assert commerce_center_page.became_visible(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.MANDATORY_TO_FILL_TEXT,
            10,
        )
        assert commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.MANDATORY_TO_FILL_TEXT
        )

    def test_catalog_feed_or_community(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_feed_or_community()

        assert commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.LINK_TO_FEED_OR_COMMUNITY_INPUT
        )
        assert commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.UPDATE_PERIOD_SELECT
        )
        assert commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.AUTOMATICALLY_DELETE_UTM_LABELS_TEXT
        )

    def test_catalog_marketplace(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_marketplace()
        assert commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.SELLER_LINK_INPUT
        )

    def test_catalog_manual(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_manually()

        assert commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.FEED_CATEGORY_SELECT
        )
        assert commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.DOWNLOAD_TEMPLATE_OF_FEED_BUTTON
        )
        assert commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.FILE_FEED_SELECT
        )
        assert commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.AUTO_DELETE_UTM_LABELS_CHECKBOX_LABEL
        )

    def test_catalog_marketplace_link_empty(
        self, commerce_center_page: CommerceCenterPage
    ):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_marketplace()
        commerce_center_page.click_sidebar_form_create_catalog()

        need_to_fill_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert self.NEEDS_FILLING_TEXT in need_to_fill_text

    def test_catalog_marketplace_not_link(
        self, commerce_center_page: CommerceCenterPage
    ):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_marketplace()

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.SELLER_LINK_INPUT,
            self.INVALID_HTTP_INPUT_VALUE,
        )
        commerce_center_page.click_sidebar_form_create_catalog()

        need_to_fill_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert self.NOT_HTTP_LINK_TEXT in need_to_fill_text

    def test_catalog_marketplace_valid_link(
        self, commerce_center_page: CommerceCenterPage
    ):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_marketplace()

        commerce_center_page.click(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.SELLER_LINK_INPUT
        )
        commerce_center_page.fill(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.SELLER_LINK_INPUT,
            self.OZON_SELLER_LINK,
        )

        assert commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.CLIENT_ID_INPUT
        )
        assert commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.API_KEY_INPUT
        )
        assert commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.UPDATE_PERIOD_SELECT
        )

    def test_catalog_marketplace_empty_api_key(
        self, commerce_center_page: CommerceCenterPage
    ):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_marketplace()

        commerce_center_page.click(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.SELLER_LINK_INPUT
        )
        commerce_center_page.fill(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.SELLER_LINK_INPUT,
            self.OZON_SELLER_LINK,
        )

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.CLIENT_ID_INPUT,
            self.OZON_CLIENT_ID,
        )

        commerce_center_page.click_sidebar_form_create_catalog()

        need_to_fill_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert self.NEEDS_FILLING_TEXT in need_to_fill_text

    def test_catalog_marketplace_invalid_api_key(
        self, commerce_center_page: CommerceCenterPage
    ):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_marketplace()

        commerce_center_page.click(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.SELLER_LINK_INPUT
        )
        commerce_center_page.fill(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.SELLER_LINK_INPUT,
            self.OZON_SELLER_LINK,
        )

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.CLIENT_ID_INPUT,
            self.WRONG_CLIENT_ID_VALUE,
        )

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.API_KEY_INPUT,
            self.WRONG_API_KEY_TEXT,
        )

        commerce_center_page.click_sidebar_form_create_catalog()

        commerce_center_page.wait().until(
            EC.visibility_of_element_located(
                commerce_center_page.locators.CommerceCenterSidebarFormLocators.ERROR_TEXT_SPAN
            )
        )

        need_to_fill_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert self.WRONG_API_KEY_TEXT in need_to_fill_text

    def test_catalog_manually_empty_file(
        self, commerce_center_page: CommerceCenterPage
    ):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_manually()

        commerce_center_page.click_sidebar_form_create_catalog()

        need_to_fill_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert self.NEEDS_FILLING_TEXT in need_to_fill_text

    def test_catalog_feed_empty_link(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_feed_or_community()

        commerce_center_page.clear(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.LINK_TO_FEED_OR_COMMUNITY_INPUT
        )
        commerce_center_page.click_sidebar_form_create_catalog()

        need_to_fill_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert self.NEEDS_FILLING_TEXT in need_to_fill_text

    def test_catalog_feed_not_link(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_feed_or_community()

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.LINK_TO_FEED_OR_COMMUNITY_INPUT,
            self.INVALID_HTTP_INPUT_VALUE,
        )
        commerce_center_page.click_sidebar_form_create_catalog()

        need_to_fill_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert self.NOT_HTTP_LINK_TEXT in need_to_fill_text

    def test_catalog_feed_community_without_services(
        self, commerce_center_page: CommerceCenterPage
    ):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_feed_or_community()

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.LINK_TO_FEED_OR_COMMUNITY_INPUT,
            self.VK_COMMUNITY_WITHOUT_GOODS_LINK,
        )
        commerce_center_page.click_sidebar_form_create_catalog()

        commerce_center_page.wait().until(
            EC.visibility_of_element_located(
                commerce_center_page.locators.CommerceCenterSidebarFormLocators.FEED_OR_COMMUNITY_ERROR_DIV
            )
        )

        need_to_fill_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert self.NOT_ENOUGH_GOODS_TEXT in need_to_fill_text

    def test_catalog_feed_page_redirect(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_feed_or_community()

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.NAME_INPUT,
            self.CATALOG_NAME_TEXT,
        )

        commerce_center_page.click_sidebar_form_create_catalog()

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.LINK_TO_FEED_OR_COMMUNITY_INPUT,
            self.VK_COMMUNITY_WITH_GOODS_LINK,
        )

        commerce_center_page.wait().until(
            EC.invisibility_of_element_located(
                commerce_center_page.locators.CommerceCenterSidebarFormLocators.AUTO_DELETE_UTM_LABELS_CHECKBOX_LABEL
            )
        )

        commerce_center_page.click_sidebar_form_create_catalog()

        commerce_center_page.wait().until(EC.url_changes(commerce_center_page.url))

        sidebar_form_text = commerce_center_page.find(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.CURRENT_CATALOG_DIV
        ).text
        assert self.CATALOG_NAME_TEXT in sidebar_form_text
