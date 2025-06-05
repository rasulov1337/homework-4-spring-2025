from base import BaseCase
from ui.pages.company_page import CompanyPage, CompanyTarget


class TestCompany(BaseCase):

    SITE_URL = "https://pootnick.ru/"
    AD_HEADER = "AD"
    AD_DESC = "DESC"
    ADVERTISED_SITE_TEXT = "Рекламируемый сайт"
    COUNTRY = "Россия"

    def teardown_method(self, method):
        try:
            self.company_page = CompanyPage(self.driver)

            self.company_page.clear_all_companies()
        except Exception as e:
            print("Exception occured: ", e)

    def test_create_site_company(self, company_page: CompanyPage):
        company_page.close_help_modal()
        company_page.open_company_creation()
        company_page.select_target(CompanyTarget.SITE)
        assert company_page.is_site_section_opened(), "Раздел 'Рекламируемый сайт' не открылся"

        company_page.set_site_url(self.SITE_URL)
        actual_url = company_page.get_site_url_value()
        assert actual_url == self.SITE_URL, f"URL не совпадает: ожидалось {self.SITE_URL}, получено {actual_url}"
        company_page.apply_target("1000")

        company_page.click_next()
        company_page.check_not_click_next()
        company_page.set_region()
        assert company_page.is_region_selected(self.COUNTRY), f"Страна '{self.COUNTRY}' не выбрана"
        company_page.click_next()

        company_page.set_ad_header(self.AD_HEADER)
        company_page.set_ad_short_desc(self.AD_DESC)
        assert company_page.get_ad_header_value() == self.AD_HEADER, "Заголовок не совпадает"
        assert company_page.get_ad_short_desc_value() == self.AD_DESC, "Описание не совпадает"

        company_page.save_company()

        company_page.open_companies_list()
        company_page.open_companies_drafts()
        companies_drafts = company_page.get_companies_drafts()

        assert len(companies_drafts) == 1, "Ожидался 1 черновик кампании"
