from ui.pages.overview_page import OverviewPage
from ui.locators.mobile_apps_locators import MobileAppsPageLocators
from ui.pages.base_page import BasePage


class MobileAppsPage(BasePage):
    url = "https://ads.vk.com/hq/apps/"
    locators = MobileAppsPageLocators()
