import time

import pytest

from service.drrp.list_auth_test import data_auth_test
from service.auth.pages.auth_page import AuthPage
from service.drrp.pages.common_page import DrrpCommonPage
from settings.setting_browser import SettingsBrowser
from settings.setting_project import *
from settings.setting_sreenshots import SettingsScreenshots


class AuthMethod(SettingsBrowser, AuthPage, DrrpCommonPage, SettingsScreenshots):

    def login(self, driver):
        self.get_user(driver).send_keys(project_rule[PROJECT][RULE]['login'])
        self.get_passw(driver).send_keys(project_rule[PROJECT][RULE]['passw'])
        self.get_entry(driver).click()
        self.visible_el_popup_parent_hidden(driver)
        self.visible_v_modal(driver)
        self.click_input_type_key(driver)
        self.visible_div_is_focus(driver)
        time.sleep(2)
        self.set_attr_hover_first_element(driver, 0)
        self.set_attr_selected_first_element(driver, 0)
        self.select_type_key_list_first_element(driver, 0)
        self.insert_input_select_file(driver, project_rule[PROJECT][RULE]['key_path'])
        self.insert_input_passw(driver, project_rule[PROJECT][RULE]['passw_key'])
        self.check_invisible_button_is_disabled(driver)
        self.click_btn_load(driver)
        self.visible_form_select_certificate(driver)
        self.click_input_selected_acsk(driver)
        time.sleep(2)
        # self.get_attr_select_dropdown_hover(driver)
        self.click_select_dropdown(driver)
        self.get_entry(driver, index=1).click()
        self.visible_form_select_certificate_file(driver)
        self.insert_input_select_file(driver, project_rule[PROJECT][RULE]['certificate'], index=1)
        self.check_invisible_button_is_disabled(driver)
        self.click_btn_load(driver)

    def logout(self, driver):
        # self.click_user_code(driver)
        self.click_u_navbar_dropdown(driver)
        self.click_user_exit(driver)
        self.visible_client_login_form(driver)

    @pytest.fixture(scope="session")
    def start_session(self):
        browser = self.desktop_browser()
        try:
            self.login(browser)
            yield browser
        except Exception:
            browser.quit()
        else:
            browser.quit()

    @pytest.fixture
    def start_browser_with_login(self):

        browser = self.desktop_browser()
        try:
            self.login(browser)
            yield browser
        except Exception:
            self.create_screenshot(browser)
        else:
            self.create_screenshot(browser)
        finally:
            browser.quit()

    @pytest.fixture
    def start_browser(self):
        browser = self.desktop_browser()
        try:
            yield browser
            self.logout(browser)
        except Exception:
            self.create_screenshot(browser)
        else:
            self.create_screenshot(browser)
        finally:
            browser.quit()

    @pytest.fixture
    def start_browser_auth(self):
        browser = self.desktop_browser()
        try:
            yield browser
        except Exception:
            self.create_screenshot(browser)
        else:
            self.create_screenshot(browser)
        finally:
            browser.quit()

    def login_auth_first_level(self, driver, name_test):
        self.get_user(driver).send_keys(data_auth_test[name_test]['login'])
        self.get_passw(driver).send_keys(data_auth_test[name_test]['passw'])
        self.get_entry(driver).click()

    def login_auth_second_level(self, driver, name_test):
        self.visible_el_popup_parent_hidden(driver)
        self.visible_v_modal(driver)
        self.click_input_type_key(driver)
        self.visible_div_is_focus(driver)
        time.sleep(2)
        self.set_attr_hover_first_element(driver, 0)
        self.set_attr_selected_first_element(driver, 0)
        self.select_type_key_list_first_element(driver, 0)
        self.insert_input_select_file(driver, data_auth_test[name_test]['key_path'])
        self.insert_input_passw(driver, data_auth_test[name_test]['passw_key'])
        self.check_invisible_button_is_disabled(driver)
        self.click_btn_load(driver)

    def login_auth_second_level_wo_click(self, driver, name_test):
        self.visible_el_popup_parent_hidden(driver)
        self.visible_v_modal(driver)
        self.click_input_type_key(driver)
        self.visible_div_is_focus(driver)
        time.sleep(2)
        self.set_attr_hover_first_element(driver, 0)
        self.set_attr_selected_first_element(driver, 0)
        self.select_type_key_list_first_element(driver, 0)
        self.insert_input_select_file(driver, data_auth_test[name_test]['key_path'])
        self.insert_input_passw(driver, data_auth_test[name_test]['passw_key'])
        self.check_invisible_button_is_disabled(driver)
