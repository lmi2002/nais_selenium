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
        time.sleep(2)
        self.click_input_type_key(driver)
        time.sleep(2)
        self.select_type_key_list_first_element(driver)
        self.insert_input_select_file(driver, r'D:\Project\nais_selenium\drivers\Key-6.dat')
        self.insert_input_passw(driver, '123456789')
        time.sleep(2)
        self.click_btn_load(driver)

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
