import time
from base import BaseCase
from ui.pages.commerce_center_page import CommerceCenterPage
from selenium.webdriver.support import expected_conditions as EC


class TestCommerceCenter(BaseCase):
    authorize = True

    def test_show_modal_education(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.click_undergo_training()
        commerce_center_page.close_popup()
        training_variants = commerce_center_page.find_all(
            commerce_center_page.locators.TRAINING_OFFER_POPUP_TRAIN_BUTTONS
        )
        assert "Создать каталог с подсказками" in training_variants[0].text
        assert "Смотреть видеоурок от экспертов VK" in training_variants[1].text
        assert "Смотреть курс на обучающей платформе" in training_variants[2].text

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
        assert "Новый каталог" in sidebar_form_text

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
        assert "Нужно заполнить" in need_to_fill_text

    def test_catalog_marketplace_not_link(
        self, commerce_center_page: CommerceCenterPage
    ):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_marketplace()

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.SELLER_LINK_INPUT,
            "not a http",
        )
        commerce_center_page.click_sidebar_form_create_catalog()

        need_to_fill_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert "Необходимо указать протокол http(s)" in need_to_fill_text

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
            "https://www.ozon.ru/seller/g-point-806219/",  # todo: move into const?
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
            "https://www.ozon.ru/seller/g-point-806219/",  # todo: move into const?
        )

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.CLIENT_ID_INPUT,
            "806219",
        )

        commerce_center_page.click_sidebar_form_create_catalog()

        need_to_fill_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert "Нужно заполнить" in need_to_fill_text

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
            "https://www.ozon.ru/seller/g-point-806219/",  # todo: move into const?
        )

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.CLIENT_ID_INPUT,
            "123",
        )

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.API_KEY_INPUT,
            "123",
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
        assert "Указан неверный ключ" in need_to_fill_text

    def test_catalog_manually_empty_file(
        self, commerce_center_page: CommerceCenterPage
    ):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_manually()

        commerce_center_page.click_sidebar_form_create_catalog()

        need_to_fill_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert "Нужно заполнить" in need_to_fill_text

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
        assert "Нужно заполнить" in need_to_fill_text

    def test_catalog_feed_not_link(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_feed_or_community()

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.LINK_TO_FEED_OR_COMMUNITY_INPUT,
            "testing",
        )
        commerce_center_page.click_sidebar_form_create_catalog()

        need_to_fill_text = commerce_center_page.find(
            commerce_center_page.locators.SIDEBAR_FORM
        ).text
        assert "Необходимо указать протокол http(s)" in need_to_fill_text

    def test_catalog_feed_community_without_services(
        self, commerce_center_page: CommerceCenterPage
    ):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_feed_or_community()

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.LINK_TO_FEED_OR_COMMUNITY_INPUT,
            "https://vk.com/vkeducation",
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
        assert "В этом сообществе недостаточно товаров или услуг" in need_to_fill_text

    def test_catalog_feed_page_redirect(self, commerce_center_page: CommerceCenterPage):
        commerce_center_page.open_catalog_creation_form()
        commerce_center_page.select_position_feed_or_community()

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.NAME_INPUT,
            "Some Name",
        )

        commerce_center_page.click_sidebar_form_create_catalog()

        commerce_center_page.fill_in(
            commerce_center_page.locators.CommerceCenterSidebarFormLocators.LINK_TO_FEED_OR_COMMUNITY_INPUT,
            "https://vk.com/club230422504",
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
        assert "Some Name" in sidebar_form_text
