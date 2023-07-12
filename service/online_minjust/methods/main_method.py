#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import time

import requests

from exception import NotDownloadNewPdfException, NotElementsDropdownListException
from helpers import base
from helpers.func import get_list_files, extract_text_from_pdf_pypdf2
from service.online_minjust.pages.main_page import OnlineMinjustMainPage
from service.payments.portmone.methods.main_method import PortmoneMainMethod
from settings.setting_allure import SettingAllure
from settings.setting_browser import SettingsBrowser


class OnlineMinjustMainMethod:
    dirname = SettingsBrowser().get_download_dir_pdf()
    pattern_dirname = '../storages/online_minjust_pattern_pdf/'

    def get_list_download_files(self):
        return set(get_list_files(self.dirname))

    def update_list_download_files(self, browser, files):
        timeout = 60
        poll = 0.5
        end_time = time.time() + timeout
        qty = len(files)
        # print('блок: 1')
        while True:
            file = self.get_first_file(self.get_list_download_files().difference(files))
            qty_new = len(self.get_list_download_files())
            if qty_new > qty and 'crdownload' not in file:
                # print('блок: 2')
                return file
            time.sleep(poll)
            if time.time() > end_time:
                # print('блок: 3')
                break
        base.ssc.create_screenshot(browser)
        raise NotDownloadNewPdfException()

    def get_abspath_file(self, name_file):
        return os.path.join(self.dirname, name_file)

    def get_abspath_pattern_file(self, name_file):
        return os.path.join(self.pattern_dirname, name_file)

    def get_first_file(self, set_files):
        for elem in set_files:
            return elem

    def auth_online_minjust(self, browser, path_key, key_passw):
        OnlineMinjustMainPage().select_csk(browser, 30)
        OnlineMinjustMainPage().insert_input_select_file(browser, path_key)
        OnlineMinjustMainPage().insert_input_pkey_password(browser, key_passw)
        OnlineMinjustMainPage().click_submit_ecp(browser)

    def pass_to_page_service(self, browser, path_key, key_passw):
        OnlineMinjustMainPage().click_btn_pass_to_rrp(browser)
        OnlineMinjustMainPage().click_btn_pass_to_info_rrp(browser)
        self.auth_online_minjust(browser, path_key, key_passw)
        OnlineMinjustMainPage().click_btn_service(browser)
        time.sleep(2)

    def check_elems_in_dropdown_list(self, browser, elems):
        timeout = 5
        poll = 0.5
        end_time = time.time() + timeout
        while True:
            elems_new = OnlineMinjustMainPage().get_elems_in_dropdown_list(browser)
            if len(elems_new) > elems:
                return False
            time.sleep(poll)
            if time.time() > end_time:
                break
        base.ssc.create_screenshot(browser)
        raise NotElementsDropdownListException()

    def validation_infospravka(self, driver, files, number, pattern_file, prop=None, owner_prop=False, all_prop=False):
        """
        :param driver: Driver browser
        :param files: {files} -> set
        :param number:
        :param pattern_file: Name pattern file
        :param prop: Property of owner. Default -> None.
        :param owner_prop: Owner with more than one property -> True. Default -> False.
        :param all_prop: All propertyes for the subject -> True. Default -> False.
        :return:
        """
        # оплата в платежной системе Portmone
        OnlineMinjustMainPage().check_visible_form_group_title(driver)
        new_number = OnlineMinjustMainPage().check_visible_new_first_number(driver, number)
        if owner_prop is True:
            if all_prop is True:
                OnlineMinjustMainPage().click_new_first_number_select_all_obj(driver, new_number)
            else:
                OnlineMinjustMainPage().click_new_first_number_select_obj(driver, new_number)
                OnlineMinjustMainPage().click_href_onm(driver, prop=prop)
        new_number = OnlineMinjustMainPage().check_visible_new_first_number(driver, number)
        OnlineMinjustMainPage().click_first_number_payment(driver, new_number)
        OnlineMinjustMainPage().switch_to_tab_portmone(driver)
        OnlineMinjustMainPage().click_btn_payment_type_portmone(driver)
        OnlineMinjustMainPage().check_text_name(driver,
                                                u'«Iнформація з Державного реєстру речових прав на нерухоме майно»')
        OnlineMinjustMainPage().check_text_id(driver, new_number)
        OnlineMinjustMainPage().check_text_cost(driver, u'30,00 грн')
        OnlineMinjustMainPage().check_text_data(driver)
        OnlineMinjustMainPage().click_btn_payment_confirm(driver)
        PortmoneMainMethod().payment_on_site(driver, number=new_number)
        OnlineMinjustMainPage().close_tab_portmone(driver)
        OnlineMinjustMainPage().switch_to_tab_online_minjust(driver)
        OnlineMinjustMainPage().click_new_first_loaded_payment(driver, new_number)
        file = OnlineMinjustMainMethod().update_list_download_files(driver, files)
        file_path = OnlineMinjustMainMethod().get_abspath_file(file)

        SettingAllure.save_pdf_file(file_path)

        # извлечение текста с загруженного pdf файла
        time.sleep(4)
        text_file = extract_text_from_pdf_pypdf2(file_path)
        # извлечение текста c необходимой точки и до конца
        index_file = text_file.find('Підстава формування')
        t = text_file[index_file:-1]

        # извлечение текста с шаблона pdf файла
        text_file_pattern = extract_text_from_pdf_pypdf2(
            OnlineMinjustMainMethod().get_abspath_pattern_file(pattern_file))
        # извлечение текста c необходимой точки и до конца
        index_file_pattern = text_file_pattern.find('Підстава формування')
        tp = text_file[index_file_pattern:-1]

        assert t == tp

    def get_status_bulk(self, path, headers):
        lst = []
        num = None
        data_get_status_bulk = [
            {
                "entity": "pkg_package",
                "method": "getStatusBulk",
                "seconds": 600,
                "isReques": 1
            }
        ]

        response_get_st = requests.post(path, headers=headers, data=json.dumps(data_get_status_bulk)).json()[0]
        result_data = response_get_st.get('resultData')
        re_requests = json.loads(result_data).get('requests')
        if re_requests:
            for request in re_requests:
                lst.append(request.get('requestId'))
            lst.sort(reverse=True)
            num = lst[0]

        return num
