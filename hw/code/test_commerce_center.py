from base import BaseCase
from ui.pages.commerce_center_page import CommerceCenterPage
from ui.locators.commerce_center_locators import CommerceCenterPageLocators

class TestCommerceCenter(BaseCase):
    authorize = True

    def test_show_modal_education(self, commerce_center_page: CommerceCenterPage):
        if commerce_center_page.popup_active():  # Sometimes modal windows with the offering of training is shown. We need to close it.
            commerce_center_page.close_popup()
        commerce_center_page.click_undergo_training()
        commerce_center_page.close_popup()
        training_variants = commerce_center_page.find_all(CommerceCenterPageLocators.TRAINING_OFFER_POPUP_TRAIN_BUTTONS)
        assert 'Создать каталог с подсказками' in training_variants[0].text and 'Смотреть видеоурок от экспертов VK' in training_variants[1].text and 'Смотреть курс на обучающей платформе' in training_variants[2].text