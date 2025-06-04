from base import BaseCase
from ui.pages.company_page import CompanyPage, CompanyTarget


class TestCompany(BaseCase):
    def test_create_site_company(self, company_page: CompanyPage):
        company_page.close_help_modal()
        company_page.open_company_creation()
        company_page.select_target(CompanyTarget.SITE)
        assert "Рекламируемый сайт" in company_page.driver.page_source

        site_url = 'https://pootnick.ru/'

        company_page.set_site_url(site_url)
        assert site_url in company_page.driver.page_source
        company_page.unfocus()
        company_page.apply_target()

        company_page.click_next()
        company_page.check_not_click_next()
        company_page.set_region()
        assert 'Россия' in company_page.driver.page_source
        company_page.click_next()

        ad_header = 'AD'
        ad_desc = 'DESC'

        company_page.set_ad_header(ad_header)
        company_page.set_ad_short_desc(ad_desc)
        assert ad_header in company_page.driver.page_source
        assert ad_desc in company_page.driver.page_source

        company_page.save_company()

        company_page.open_companies_list()
        company_page.open_companies_drafts()
        companies_drafts = company_page.get_companies_drafts()

        assert len(companies_drafts) == 1