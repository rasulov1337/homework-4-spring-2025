from ui.locators.budget_locators import BudgetPageLocators
from ui.pages.base_page import BasePage


class BudgetPage(BasePage):
    url = 'https://ads.vk.com/hq/budget/'
    locators = BudgetPageLocators()

    def click_replenish_budget_button(self):
        self.click(self.locators.REPLENISH_BUDGET_BUTTON)

    def is_replenishment_modal_visible(self):
        return self.is_visible(self.locators.REPLENISHMENT_MODAL)

    def is_replenishment_modal_field_visible(self, label):
        return self.is_visible(self.locators.REPLENISHMENT_MODAL_FIELD(label))

    def get_replenishment_modal(self):
        return self.find(self.locators.REPLENISHMENT_MODAL)

    def enter_amount(self, amount):
        amount_input = self.find(self.locators.AMOUNT_INPUT)
        amount_input.clear()
        amount_input.send_keys(amount)

    def get_amount_value(self):
        return self.find(self.locators.AMOUNT_INPUT).get_attribute('value')

    def enter_amount_without_vat(self, amount):
        amount_without_vat_input = self.find(self.locators.AMOUNT_WITHOUT_VAT_INPUT)
        amount_without_vat_input.clear()
        amount_without_vat_input.send_keys(amount)

    def get_amount_without_vat_value(self):
        return self.find(self.locators.AMOUNT_WITHOUT_VAT_INPUT).get_attribute('value')

    def get_error_message(self):
        return self.find(self.locators.ERROR_MESSAGE).text

    def click_submit_button(self):
        self.click(self.locators.SUBMIT_BUTTON)

    def is_vkpay_iframe_visible(self):
        return self.is_visible(self.locators.VKPAY_IFRAME, timeout=10)

    def get_vkpay_iframe(self):
        return self.find(self.locators.VKPAY_IFRAME)
