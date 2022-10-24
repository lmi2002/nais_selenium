import os
import time
import pytest

from helpers.func import extract_text_from_pdf
from service.online_minjust.methods.auth_method import OnlineMinjustAuthMethod
from service.online_minjust.methods.main_method import OnlineMinjustMainMethod
from service.online_minjust.pages.main_page import OnlineMinjustMainPage
from service.payments.portmone.pages.main_page import PortmoneMainPage


# @allure.severity(allure.severity_level.NORMAL)
class TestOnlineMinjust(OnlineMinjustAuthMethod):

    # @pytest.mark.skip
    @pytest.mark.online_minjust
    def test_search_onm(self, start_session):
        browser = start_session
        files = OnlineMinjustMainMethod().get_list_download_files()
        OnlineMinjustMainPage().click_btn_pass_to_rrp(browser)
        OnlineMinjustMainPage().click_btn_pass_to_auth_page(browser)
        OnlineMinjustMainPage().select_csk(browser, 1)
        OnlineMinjustMainPage().insert_input_select_file(browser)
        OnlineMinjustMainPage().insert_input_pkey_password(browser)
        OnlineMinjustMainPage().click_submit_ecp(browser)
        OnlineMinjustMainPage().click_btn_service(browser)
        OnlineMinjustMainPage().click_btn_pass_to_auth_page(browser)
        time.sleep(2)
        number = OnlineMinjustMainPage().get_text_first_number(browser)
        OnlineMinjustMainPage().click_checkbox_onm(browser)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainPage().insert_input_field_onm(browser)
        OnlineMinjustMainPage().click_btn_next(browser)
        OnlineMinjustMainPage().check_visible_form_group_title(browser)
        OnlineMinjustMainPage().check_visible_new_first_number(browser, number)
        new_number = OnlineMinjustMainPage().get_text_first_number(browser)
        OnlineMinjustMainPage().check_visible_new_first_number_payment(browser, new_number)
        OnlineMinjustMainPage().click_first_number_payment(browser)
        OnlineMinjustMainPage().switch_to_tab_portmone(browser)
        OnlineMinjustMainPage().click_btn_payment_type_portmone(browser)
        OnlineMinjustMainPage().check_text_name(browser,
                                                '«Iнформація з Державного реєстру речових прав на нерухоме майно»')
        OnlineMinjustMainPage().check_text_id(browser, new_number)
        OnlineMinjustMainPage().check_text_cost(browser, '30,00 грн')
        OnlineMinjustMainPage().check_text_data(browser)
        OnlineMinjustMainPage().click_btn_payment_confirm(browser)
        time.sleep(1)
        PortmoneMainPage().insert_field_number_card(browser)
        PortmoneMainPage().insert_field_exp_date_card(browser)
        PortmoneMainPage().insert_field_cvv2_card(browser)
        PortmoneMainPage().insert_field_email(browser)
        PortmoneMainPage().click_btn_payment(browser)
        time.sleep(1)
        PortmoneMainPage().check_text_present_in_total_amount(browser, '33.00')
        PortmoneMainPage().click_btn_payment_confirm(browser)
        PortmoneMainPage().check_current_url(browser, new_number)
        OnlineMinjustMainPage().close_tab_portmone(browser)
        OnlineMinjustMainPage().switch_to_tab_online_minjust(browser)
        OnlineMinjustMainPage().check_visible_new_first_loaded_payment(browser, new_number)
        OnlineMinjustMainPage().click_first_number_payment(browser)
        OnlineMinjustMainMethod().update_list_download_files(len(files))
        new_files = OnlineMinjustMainMethod().get_list_download_files()
        last_download_file = new_files.difference(files)
        get_download_file = OnlineMinjustMainMethod().get_first_file(last_download_file)
        file_onm = OnlineMinjustMainMethod().get_abspath_file(get_download_file)
        time.sleep(4)
        print(file_onm)
        # file_onm_pattern
        text_file_onm = extract_text_from_pdf(file_onm)
        print(text_file_onm)

        time.sleep(12)

    @pytest.mark.skip
    @pytest.mark.online_minjust
    def test_search_address(self, start_session):
        browser = start_session
        OnlineMinjustMainPage().click_btn_pass_to_rrp(browser)
        OnlineMinjustMainPage().click_btn_pass_to_auth_page(browser)
        OnlineMinjustMainPage().select_csk(browser, 1)
        OnlineMinjustMainPage().insert_input_select_file(browser)
        OnlineMinjustMainPage().insert_input_pkey_password(browser)
        OnlineMinjustMainPage().click_submit_ecp(browser)
        OnlineMinjustMainPage().click_btn_service(browser)
        OnlineMinjustMainPage().click_btn_pass_to_auth_page(browser)
        time.sleep(2)
        number = OnlineMinjustMainPage().get_text_first_number(browser)
        OnlineMinjustMainPage().click_checkbox_address(browser)
        OnlineMinjustMainPage().click_btn_next(browser)
        time.sleep(12)

    @pytest.mark.skip
    @pytest.mark.online_minjust
    def test_search_onm1(self):
        OnlineMinjustMainMethod().get_last_download_file()
