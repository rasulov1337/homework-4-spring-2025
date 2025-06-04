from base import BaseCase
from ui.pages.budget_page import BudgetPage


class TestBudget(BaseCase):
    PAY_SUM_TEXT = "Cумма к оплате"
    MINIMAL_SUM_TEXT = "Минимальная сумма 600,00 ₽"
    SUM_TO_BALANCE = "На баланс поступит (НДС — 20%)"

    def test_open_replenishment_modal_page(self, budget_page: BudgetPage):
        budget_page.click_replenish_budget_button()
        assert budget_page.is_replenishment_modal_visible()
        assert budget_page.is_replenishment_modal_field_visible(self.PAY_SUM_TEXT)
        assert budget_page.is_replenishment_modal_field_visible(self.SUM_TO_BALANCE)

    def test_valid_amount(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount("600")
        assert "500 ₽" == budget_page.get_amount_without_vat_value()
        budget_page.click_submit_button()
        assert budget_page.is_vkpay_iframe_visible()

    def test_valid_amount_without_vat(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount_without_vat("500")
        assert "600 ₽" == budget_page.get_amount_value()
        budget_page.click_submit_button()
        assert budget_page.is_vkpay_iframe_visible()

    def test_error_too_small_amount(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount("599")
        assert budget_page.get_error_message() == self.MINIMAL_SUM_TEXT

    def test_error_too_small_amount_without_vat(self, budget_page):
        budget_page.click_replenish_budget_button()
        budget_page.enter_amount_without_vat("499")
        budget_page.click_submit_button()
        assert budget_page.get_error_message() == self.MINIMAL_SUM_TEXT
