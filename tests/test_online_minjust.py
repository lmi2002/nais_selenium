#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time

import pytest
import requests

import allure
from service.auth.methods.auth_method import AuthMethod
from service.drrp.pages.common_page import DrrpCommonPage
from service.drrp.pages.queue_statement_page import DrrpQueueStatementPage
from service.drrp.pages.statement_page import DrrpStatementPage
from service.online_minjust.methods.main_method import OnlineMinjustMainMethod
from settings import setting_project
from service.payments.portmone.methods.main_method import PortmoneMainMethod
from settings.setting_online_minjust_data_info import onm, cad_num, address, owner_code, owner_name, company_code, \
    company_name, owner_address, company_onm, owner_address_zaborona
from service.online_minjust.methods.auth_method import OnlineMinjustAuthMethod
from service.online_minjust.pages.main_page import OnlineMinjustMainPage



@allure.severity(allure.severity_level.NORMAL)
class TestOnlineMinjust(OnlineMinjustAuthMethod):

    data_obu = setting_project.project_rule.get('online_minjust').get('user1')

    # @pytest.mark.skip
    @pytest.mark.online_minjust
    def test_search_onm(self, start_browser_obu):
        browser = start_browser_obu
        pattern_file = 'onm.pdf'
        files = OnlineMinjustMainMethod().get_list_download_files()
        OnlineMinjustMainMethod().pass_to_page_service(browser, self.data_obu.get('key_path'), self.data_obu.get('passw_key'))
        OnlineMinjustMainPage().click_btn_pass_to_info_rrp(browser)
        time.sleep(2)
        number = OnlineMinjustMainPage().get_text_first_number(browser)
        OnlineMinjustMainPage().click_checkbox_onm(browser)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainPage().insert_input_field_onm(browser, onm)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainMethod().validation_infospravka(browser, files, number, pattern_file)

    # @pytest.mark.skip
    @pytest.mark.online_minjust
    def test_search_address(self, start_browser_obu):
        browser = start_browser_obu
        pattern_file = 'address.pdf'
        files = OnlineMinjustMainMethod().get_list_download_files()
        OnlineMinjustMainMethod().pass_to_page_service(browser, self.data_obu.get('key_path'), self.data_obu.get('passw_key'))
        OnlineMinjustMainPage().click_btn_pass_to_info_rrp(browser)
        time.sleep(2)
        number = OnlineMinjustMainPage().get_text_first_number(browser)
        OnlineMinjustMainPage().click_checkbox_address(browser)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainPage().click_field_region(browser)
        OnlineMinjustMainMethod().check_elems_in_dropdown_list(browser, 6)
        OnlineMinjustMainPage().select_region(browser, 10)
        OnlineMinjustMainPage().click_field_city(browser, 1)
        OnlineMinjustMainMethod().check_elems_in_dropdown_list(browser, 6)
        OnlineMinjustMainPage().select_city(browser, 12)
        OnlineMinjustMainPage().click_field_street(browser, 3)
        OnlineMinjustMainMethod().check_elems_in_dropdown_list(browser, 6)
        OnlineMinjustMainPage().select_street(browser)
        OnlineMinjustMainPage().select_house_type(browser, address.get('house_type'))
        OnlineMinjustMainPage().insert_input_field_num_house(browser, address.get('house'))
        OnlineMinjustMainPage().select_object_num_type(browser, address.get('object_type'))
        OnlineMinjustMainPage().insert_input_field_num_appart(browser, address.get('appartment'))
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainMethod().validation_infospravka(browser, files, number, pattern_file)

    # @pytest.mark.skip
    @pytest.mark.online_minjust
    def test_search_cad_num(self, start_browser_obu):
        browser = start_browser_obu
        pattern_file = 'cad_num.pdf'
        files = OnlineMinjustMainMethod().get_list_download_files()
        OnlineMinjustMainMethod().pass_to_page_service(browser, self.data_obu.get('key_path'), self.data_obu.get('passw_key'))
        OnlineMinjustMainPage().click_btn_pass_to_info_rrp(browser)
        time.sleep(2)
        number = OnlineMinjustMainPage().get_text_first_number(browser)
        OnlineMinjustMainPage().click_checkbox_cad_num(browser)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainPage().insert_input_field_cad_num(browser, cad_num)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainMethod().validation_infospravka(browser, files, number, pattern_file)

    # @pytest.mark.skip
    @pytest.mark.online_minjust
    def test_search_persone_code(self, start_browser_obu):
        browser = start_browser_obu
        pattern_file = 'pers_code.pdf'
        prop = owner_address
        files = OnlineMinjustMainMethod().get_list_download_files()
        OnlineMinjustMainMethod().pass_to_page_service(browser, self.data_obu.get('key_path'), self.data_obu.get('passw_key'))
        OnlineMinjustMainPage().click_btn_pass_to_info_rrp(browser)
        time.sleep(2)
        number = OnlineMinjustMainPage().get_text_first_number(browser)
        OnlineMinjustMainPage().click_checkbox_persone(browser)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainPage().insert_input_field_persone_code(browser, owner_code)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainMethod().validation_infospravka(browser, files, number, pattern_file, prop=prop,
                                                         owner_prop=True)

    # @pytest.mark.skip
    @pytest.mark.online_minjust
    def test_search_persone_name(self, start_browser_obu):
        browser = start_browser_obu
        pattern_file = 'pers_name.pdf'
        files = OnlineMinjustMainMethod().get_list_download_files()
        OnlineMinjustMainMethod().pass_to_page_service(browser, self.data_obu.get('key_path'), self.data_obu.get('passw_key'))
        OnlineMinjustMainPage().click_btn_pass_to_info_rrp(browser)
        time.sleep(2)
        number = OnlineMinjustMainPage().get_text_first_number(browser)
        OnlineMinjustMainPage().click_checkbox_persone(browser)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainPage().insert_input_field_persone_name(browser, owner_name)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainMethod().validation_infospravka(browser, files, number, pattern_file, owner_prop=True,
                                                         all_prop=True)

    # @pytest.mark.skip
    @pytest.mark.online_minjust
    def test_search_comp_code(self, start_browser_obu):
        browser = start_browser_obu
        pattern_file = 'comp_code.pdf'
        prop = company_onm
        files = OnlineMinjustMainMethod().get_list_download_files()
        OnlineMinjustMainMethod().pass_to_page_service(browser, self.data_obu.get('key_path'), self.data_obu.get('passw_key'))
        OnlineMinjustMainPage().click_btn_pass_to_info_rrp(browser)
        time.sleep(2)
        number = OnlineMinjustMainPage().get_text_first_number(browser)
        OnlineMinjustMainPage().click_checkbox_company(browser)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainPage().insert_input_field_persone_code(browser, company_code)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainMethod().validation_infospravka(browser, files, number, pattern_file, prop=prop,
                                                         owner_prop=True)

    # @pytest.mark.skip
    @pytest.mark.online_minjust
    def test_search_comp_name(self, start_browser_obu):
        browser = start_browser_obu
        pattern_file = 'comp_name.pdf'
        files = OnlineMinjustMainMethod().get_list_download_files()
        OnlineMinjustMainMethod().pass_to_page_service(browser, self.data_obu.get('key_path'), self.data_obu.get('passw_key'))
        OnlineMinjustMainPage().click_btn_pass_to_info_rrp(browser)
        time.sleep(2)
        number = OnlineMinjustMainPage().get_text_first_number(browser)
        OnlineMinjustMainPage().click_checkbox_company(browser)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainPage().insert_input_field_persone_name(browser, company_name)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainMethod().validation_infospravka(browser, files, number, pattern_file, owner_prop=True,
                                                         all_prop=True)

    # @pytest.mark.skip
    @pytest.mark.online_minjust
    def test_api_infospraavka_obu(self):

        path = setting_project.project_rule.get('online_minjust').get('for_req').get("host")
        headers = setting_project.project_rule.get('online_minjust').get('for_req').get("headers")

        # ---
        data_get_id = [
            {
                "entity": "pkg_infoRrp",
                "method": "getId"
            }
        ]

        response_get_id = requests.post(path, headers=headers, data=json.dumps(data_get_id))
        assert response_get_id.status_code == 200
        get_id = response_get_id.json()[0].get('resultData')

        # ---
        data_upload_package = [
            {
                "entity": "pkg_infoRrp",
                "method": "uploadPackage",
                "id": get_id,
                "packageContent": "{\"time\":\"2019-01-08T23:53:38+02:00\",\"version\":\"2.0\",\"userInfo\":{\"userName\":\"никитина1849\",\"userType\":\"1\",\"userCode\":\"1234567890\",\"userPassport\":\"АА458978\"},\"searchParams\":{\"reason\":\"Надання інформаційной довідки через реестраціїний портал\",\"searchType\":\"2\",\"subjectSearchInfo\":{\"sbjType\":\"1\",\"sbjCode\":\"2529121363\"}}}"
            }
        ]
        response_upload_package = requests.post(path, headers=headers, data=json.dumps(data_upload_package))
        assert response_upload_package.status_code == 200
        result_data = json.loads(response_upload_package.json()[0].get('resultData'))
        report_result_id = result_data.get('reportResultID')
        group_result_id = result_data.get('groupResult')[0].get('ID')

        # ---
        data_generate_pdf = [
            {
                "entity": "pkg_infoRrp",
                "method": "generatePdf",
                "id": get_id,
                "reportResultID": report_result_id,
                "groupID": group_result_id
            }
        ]
        response_generate_pdf = requests.post(path, headers=headers, data=json.dumps(data_generate_pdf))
        assert response_generate_pdf.status_code == 200
        assert bool(response_generate_pdf.json()[0].get('docID')) == True

        # ---
        data_get_result = [
            {
                "entity": "pkg_infoRrp",
                "method": "getResult",
                "id": get_id
            }
        ]
        response_get_result = requests.post(path, headers=headers, data=json.dumps(data_get_result))
        assert response_get_result.status_code == 200
        assert bool(response_get_result.json()[0].get('resultData')) == True

    # Сервис закрыт. Автотест не дописан, осталось дописать принятие заявки в реестре РРП.
    @pytest.mark.skip
    @pytest.mark.online_minjust
    def test_zaborona(self, start_browser_obu):

        path = setting_project.project_rule.get('online_minjust').get('for_req').get("host")
        headers = setting_project.project_rule.get('online_minjust').get('for_req').get("headers")

        browser = start_browser_obu

        # # Регистрация в ОБЮ
        prop = owner_address_zaborona
        OnlineMinjustMainMethod().pass_to_page_service(browser, self.data_obu.get('key_path'), self.data_obu.get('passw_key'))
        OnlineMinjustMainPage().click_btn_pass_to_zaborona_rrp(browser)
        number = OnlineMinjustMainPage().get_text_first_number(browser)
        OnlineMinjustMainPage().click_btn_get_obj(browser)
        new_number = OnlineMinjustMainPage().check_visible_new_first_number(browser, number)
        OnlineMinjustMainPage().click_new_first_number_select_obj_zaborona(browser, new_number)
        OnlineMinjustMainPage().click_href_onm_zaborona(browser, prop=prop)
        OnlineMinjustMainMethod().auth_online_minjust(browser)
        OnlineMinjustMainPage().check_invisible_modal_content(browser)
        new_number1 = OnlineMinjustMainPage().check_visible_new_first_number(browser, new_number)
        OnlineMinjustMainPage().click_first_number_payment(browser, new_number1)

        OnlineMinjustMainPage().switch_to_tab_portmone(browser)
        OnlineMinjustMainPage().click_btn_payment_type_portmone(browser)
        OnlineMinjustMainPage().check_text_name(browser,
                                                u'«Заява на заборону вчинення дії з нерухомим майном»')

        OnlineMinjustMainPage().check_text_id(browser, new_number1)
        OnlineMinjustMainPage().check_text_cost(browser, u'3,00 грн')
        OnlineMinjustMainPage().check_text_data(browser)
        OnlineMinjustMainPage().click_btn_payment_confirm(browser)
        time.sleep(1)
        PortmoneMainMethod().payment_on_site(browser, number=new_number1)
        OnlineMinjustMainPage().close_tab_portmone(browser)
        OnlineMinjustMainPage().switch_to_tab_online_minjust(browser)
        OnlineMinjustMainPage().check_visible_text_actions_text_center(browser, 'Сплачено')
        # OnlineMinjustMainPage().check_visible_text_actions_text_center(browser, 'Завантажено')
        num = OnlineMinjustMainMethod().get_status_bulk(path, headers)
        # OnlineMinjustMainPage().click_new_first_loaded_payment(browser, new_number1)

        # Создание и переход на новую вкладку
        OnlineMinjustMainPage().create_new_tab(browser)
        OnlineMinjustMainPage().switch_to_tab(browser, index=1)

        browser.get(setting_project.URL)

        # Регистрация в реестре ДРРП
        data_gov_reg = setting_project.project_rule.get('drrp').get('gov_reg')
        AuthMethod().login(browser, data_gov_reg.get('username'), data_gov_reg.get('passw'),
                            data_gov_reg.get('key_path'), data_gov_reg.get('passw_key'),
                            data_gov_reg.get('certificate'))


        DrrpCommonPage().click_main_menu_statement(browser)
        DrrpStatementPage().visible_li_is_opened(browser)
        time.sleep(2)
        DrrpStatementPage().click_sub_menu_create_queue_statement(browser)
        DrrpQueueStatementPage().check_visible_result_el_st(browser)
        DrrpQueueStatementPage().click_header_trigger(browser)
        DrrpQueueStatementPage().click_sort_desc(browser)
        import pdb;
        pdb.set_trace()

