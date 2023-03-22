#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pytest

from service.auth.list_auth_test import data_auth_test
from service.auth.pages.auth_page import AuthPage
from service.drrp.pages.common_page import DrrpCommonPage
from settings.setting_browser import SettingsBrowser, URL
from settings.setting_sreenshots import SettingsScreenshots


class AuthMethod(SettingsBrowser, AuthPage, DrrpCommonPage, SettingsScreenshots):


    @pytest.fixture(scope="session")
    def start_session(self):
        browser = SettingsBrowser().desktop_browser(URL)
        try:
            yield browser
            browser.quit()
        except Exception:
            SettingsScreenshots().create_screenshot(browser)
            browser.quit()

    @pytest.fixture
    def start_browser(self):
        browser = SettingsBrowser().desktop_browser(URL)
        try:
            yield browser
            SettingsScreenshots().create_screenshot(browser)
            browser.quit()
        except Exception:
            SettingsScreenshots().create_screenshot(browser)
            browser.quit()

    def login(self, driver, username, passw, key_path, passw_key, cer):
        self.get_user(driver).send_keys(username)
        self.get_passw(driver).send_keys(passw)
        self.get_entry(driver).click()
        self.visible_el_popup_parent_hidden(driver)
        self.visible_v_modal(driver)
        self.click_input_type_key(driver)
        self.visible_div_is_focus(driver)
        time.sleep(2)
        self.set_attr_hover_first_element(driver, 0)
        self.set_attr_selected_first_element(driver, 0)
        self.select_type_key_list_first_element(driver, 0)
        self.insert_input_select_file(driver, key_path)
        self.insert_input_passw(driver, passw_key)
        self.check_invisible_button_is_disabled(driver)
        self.click_btn_load(driver)
        self.visible_form_select_certificate(driver)
        self.click_input_selected_acsk(driver)
        time.sleep(2)
        self.click_select_dropdown(driver)
        self.get_entry(driver, index=1).click()
        self.visible_form_select_certificate_file(driver)
        self.insert_input_select_file(driver, cer, index=1)
        self.check_invisible_button_is_disabled(driver)
        self.click_btn_load(driver)

    def login_w_o_certificate(self, driver, username, passw, key_path, passw_key):
        self.get_user(driver).send_keys(username)
        self.get_passw(driver).send_keys(passw)
        self.get_entry(driver).click()
        self.visible_el_popup_parent_hidden(driver)
        self.visible_v_modal(driver)
        self.click_input_type_key(driver)
        self.visible_div_is_focus(driver)
        time.sleep(2)
        self.set_attr_hover_first_element(driver, 0)
        self.set_attr_selected_first_element(driver, 0)
        self.select_type_key_list_first_element(driver, 0)
        self.insert_input_select_file(driver, key_path)
        self.insert_input_passw(driver, passw_key)
        self.check_invisible_button_is_disabled(driver)
        self.click_btn_load(driver)


    def logout(self, driver):
        # self.click_user_code(driver)
        self.click_u_navbar_dropdown(driver)
        self.click_user_exit(driver)
        self.check_visible_field_user(driver)

    def login_auth_first_level(self, driver, name_test):
        self.get_user(driver).send_keys(data_auth_test.get(name_test).get('username'))
        self.get_passw(driver).send_keys(data_auth_test.get(name_test).get('passw'))
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
        self.insert_input_select_file(driver, data_auth_test.get(name_test).get('key_path'))
        self.insert_input_passw(driver, data_auth_test.get(name_test).get('passw_key'))
        self.check_invisible_button_is_disabled(driver)
        self.click_btn_load(driver)
        self.visible_form_select_certificate(driver)
        self.click_input_selected_acsk(driver)
        time.sleep(2)
        self.click_select_dropdown(driver)
        self.get_entry(driver, index=1).click()
        self.visible_form_select_certificate_file(driver)
        self.insert_input_select_file(driver, data_auth_test.get(name_test).get('certificate'), index=1)
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
        self.insert_input_select_file(driver, data_auth_test.get(name_test).get('key_path'))
        self.insert_input_passw(driver, data_auth_test.get(name_test).get('passw_key'))
        self.check_invisible_button_is_disabled(driver)

    def login_auth_second_level_w_o_added_certificate(self, driver, name_test):
        self.visible_el_popup_parent_hidden(driver)
        self.visible_v_modal(driver)
        self.click_input_type_key(driver)
        self.visible_div_is_focus(driver)
        time.sleep(2)
        self.set_attr_hover_first_element(driver, 0)
        self.set_attr_selected_first_element(driver, 0)
        self.select_type_key_list_first_element(driver, 0)
        self.insert_input_select_file(driver, data_auth_test.get(name_test).get('key_path'))
        self.insert_input_passw(driver, data_auth_test.get(name_test).get('passw_key'))
        self.check_invisible_button_is_disabled(driver)
        self.click_btn_load(driver)
