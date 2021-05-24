import time

import pytest

from service.drrp.pages.auth_page import DrrpAuthPage
from service.drrp.pages.common_page import DrrpCommonPage
from settings.setting_browser import SettingsBrowser
from settings.setting_project import *


class DrrpAuthMethod(SettingsBrowser, DrrpAuthPage, DrrpCommonPage):

    def login(self, driver):
        self.get_user(driver).send_keys(project_rule[PROJECT][RULE]['login'])
        self.get_passw(driver).send_keys(project_rule[PROJECT][RULE]['passw'])
        self.get_entry(driver).click()
        time.sleep(30)

    def logout(self, driver):
        self.click_user_code(driver)
        self.click_user_exit(driver)
        self.visible_client_login_form(driver)

    @pytest.fixture(scope="session")
    def start_session(self):
        browser = self.desktop_browser()
        self.login(browser)
        yield browser
        # self.logout(browser)
        # browser.quit()

