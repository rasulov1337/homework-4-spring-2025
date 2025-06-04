from base import BaseCase
from ui.pages.company_page import CompanyPage, CompanyTarget


class TestCompany(BaseCase):

    SITE_URL = "https://pootnick.ru/"
    AD_HEADER = "AD"
    AD_DESC = "DESC"
    ADVERTISED_SITE_TEXT = "Рекламируемый сайт"
    def setup_method(self, method):
        self.company_page = CompanyPage(self.driver)

    def teardown_method(self, method):
        self.company_page.clear_all_companies()

    def test_create_site_company(self, company_page: CompanyPage):
        company_page.close_help_modal()
        company_page.open_company_creation()
        company_page.select_target(CompanyTarget.SITE)
        assert self.ADVERTISED_SITE_TEXT in company_page.driver.page_source

        company_page.set_site_url(self.SITE_URL)
        assert self.SITE_URL in company_page.driver.page_source
        company_page.unfocus()
        company_page.apply_target()

        company_page.click_next()
        company_page.check_not_click_next()
        company_page.set_region()
        assert "Россия" in company_page.driver.page_source
        company_page.click_next()

        company_page.set_ad_header(self.AD_HEADER)
        company_page.set_ad_short_desc(self.AD_DESC)
        assert self.AD_HEADER in company_page.driver.page_source
        assert self.AD_DESC in company_page.driver.page_source

        company_page.save_company()

        company_page.open_companies_list()
        company_page.open_companies_drafts()
        companies_drafts = company_page.get_companies_drafts()

        assert len(companies_drafts) == 1
