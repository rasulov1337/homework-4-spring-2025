from selenium.webdriver.common.by import By


class BudgetPageLocators:
    REPLENISH_BUDGET_BUTTON = (By.XPATH, "//span[contains(@class, 'vkuiButton__content') and text()='Пополнить баланс']")
    REPLENISHMENT_MODAL = (By.CLASS_NAME, "vkuiModalPage")

    CLOSE_MODAL_PAGE_BUTTON = (By.XPATH, "//*[@aria-label='Закрыть']")

    AMOUNT_INPUT = (By.NAME, "amount")
    AMOUNT_WITHOUT_VAT_INPUT = (By.NAME, "amountWithoutVat")

    ERROR_MESSAGE = (By.XPATH, "//*[@role='alert']")

    SUBMIT_BUTTON = (By.XPATH, "//*[contains(@class, 'CreateInvoiceModal_button__')]")

    VKPAY_IFRAME = (By.XPATH, "//iframe[contains(@class, 'CreateInvoiceModal_iframe')]")

    @staticmethod
    def REPLENISHMENT_MODAL_FIELD(label):
        return (By.XPATH, f"//div[contains(@class, 'CreateInvoiceModal_top') and contains(span, '{label}')]")
