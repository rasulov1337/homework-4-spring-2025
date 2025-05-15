import json
from os import environ

import pytest
from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

from ui.pages.commerce_center_page import CommerceCenterPage
from ui.pages.auth_page import AuthPage

# from ui.pages.budget_page import BudgetPage
from ui.pages.company_page import CompanyPage
from ui.pages.audience_page import AudiencePage
from ui.pages.main_page import MainPage
from ui.pages.sites_page import SitesPage
from ui.pages.mobile_apps_page import MobileAppsPage
# from ui.pages.settings_page import SettingsPage
# from ui.pages.commerce_page import CommercePage
# from ui.pages.leadforms_page import LeadFormsPage
# from ui.pages.survey_page import SurveyPage
# from ui.pages.sites_page import SitePage


SESSION_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "session_data.json"
)


@pytest.fixture
def load_session_data(driver):
    with open(SESSION_FILE, "r") as f:
        data = json.load(f)

    # Устанавливаем localStorage
    for key, value in data.get("localStorage", {}).items():
        driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

    # Устанавливаем cookies
    for cookie in data.get("cookies", []):
        driver.add_cookie(cookie)

    # Перезагружаем страницу, чтобы сессия вступила в силу
    driver.refresh()

    return driver


@pytest.fixture()
def driver(config):
    url = config["url"]
    opts = Options()
    service = Service(environ.get("CHROMEDRIVER_PATH"))
    driver = webdriver.Chrome(options=opts, service=service)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def credentials():
    load_dotenv(find_dotenv())
    return environ.get("LOGIN"), environ.get("PASSWORD")


@pytest.fixture()
def main_page(driver):
    driver.get(MainPage.url)
    return MainPage(driver)


@pytest.fixture()
def audience_page(driver):
    driver.get(AudiencePage.url)
    return AudiencePage(driver)


@pytest.fixture
def commerce_center_page(driver):
    driver.get(CommerceCenterPage.url)
    page = CommerceCenterPage(driver=driver)
    if page.popup_active():
        page.close_popup()
    return page


@pytest.fixture
def sites_page(driver):
    driver.get(SitesPage.url)
    return SitesPage(driver=driver)


@pytest.fixture
def mobile_apps_page(driver):
    driver.get(MobileAppsPage.url)
    return MobileAppsPage(driver=driver)


@pytest.fixture()
def company_page(driver):
    driver.get(CompanyPage.url)
    return CompanyPage(driver)


@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)


@pytest.fixture
def site_page(driver):
    driver.get(SitePage.url)
    return SitePage(driver=driver)


@pytest.fixture
def leadforms_page(driver):
    driver.get(LeadFormsPage.url)
    return LeadFormsPage(driver=driver)


@pytest.fixture
def survey_page(driver):
    driver.get(SurveyPage.url)
    return SurveyPage(driver=driver)
