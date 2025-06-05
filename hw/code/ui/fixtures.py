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
from ui.pages.budget_page import BudgetPage
from ui.pages.audience_page import AudiencePage, AudienceSource

from ui.pages.company_page import CompanyPage
from ui.pages.main_page import MainPage
from ui.pages.sites_page import SitesPage
from ui.pages.mobile_apps_page import MobileAppsPage
from ui.pages.leadforms_page import LeadformPage
from ui.pages.survey_page import SurveyPage


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


@pytest.fixture
def setup_existing_audience(driver, config):
    page = AudiencePage(driver)
    driver.get(page.url)

    users_list_name = "USER LIST"
    users_list_type = "Email"
    users_list_path = config["users_list_path"]

    page.open_audience_creation()
    page.set_audience_name("EXISTING_AUDIENCE")
    page.open_sources_list()
    page.select_audience_source(AudienceSource.USERS_LIST)
    page.click_upload_new_users_list()
    page.load_new_users_list(users_list_name, users_list_type, users_list_path)
    page.submit_audience_source()
    page.wait_for_success_notify()
    page.submit_audience_creation()
    page.wait_audience_list_for_load()

    yield

    page.open_users_list_list()
    page.clear_users_lists()
    page.open_audiences_list()
    page.clear_audiences()


@pytest.fixture()
def audience_page(driver):
    page = AudiencePage(driver)
    driver.get(page.url)
    yield page

    page.open_users_list_list()
    page.clear_users_lists()
    page.open_audiences_list()
    page.clear_audiences()


@pytest.fixture
def commerce_center_page(driver):
    driver.get(CommerceCenterPage.url)
    page = CommerceCenterPage(driver=driver)
    if page.popup_active():
        page.close_popup()
    yield page

    page.delete_catalog()


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


@pytest.fixture()
def budget_page(driver):
    driver.get(BudgetPage.url)
    return BudgetPage(driver)


@pytest.fixture
def leadforms_page(driver):
    driver.get(LeadformPage.url)
    return LeadformPage(driver=driver)


@pytest.fixture
def survey_page(driver):
    driver.get(SurveyPage.url)
    return SurveyPage(driver=driver)
