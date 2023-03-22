import time

import allure
import pytest

from service.auth.list_auth_test import data_auth_test, message_text_invalid_cert_login_passw, \
    message_text_session_mode_singleton
from service.auth.methods.auth_method import AuthMethod
from service.auth.pages.auth_page import AuthPage
from service.drrp.pages.common_page import DrrpCommonPage
from service.drrp.pages.statement_page import DrrpStatementPage


@allure.severity(allure.severity_level.NORMAL)
class TestUbAuth(AuthMethod):

    @pytest.mark.auth
    def test_valid_login_passw(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)

        # Check
        self.check_visible_u_navbar_dropdown(browser)
        self.create_screenshot(browser)

    @pytest.mark.auth
    def test_empty_fields_login_passw(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)

        # Check
        self.check_text_required_field_login(browser)
        self.check_text_required_field_passw(browser)

    @pytest.mark.auth
    def test_empty_login(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)

        # Check
        self.check_text_required_field_login(browser)

    @pytest.mark.auth
    def test_empty_passw(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)

        # Check
        self.check_text_required_field_passw(browser)

    @pytest.mark.auth
    def test_invalid_login_passw(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)
        time.sleep(1)
        assert self.check_text_in_ub_dialog_break_word(browser) in message_text_invalid_cert_login_passw

    @pytest.mark.auth
    def test_empty_fields_second_level(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        assert self.get_attr_btn_load(browser) == 'true'

    @pytest.mark.auth
    def test_invalid_type_device(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.visible_el_popup_parent_hidden(browser)
        self.visible_v_modal(browser)
        self.click_input_type_key(browser)
        self.visible_div_is_focus(browser)
        time.sleep(2)
        self.set_attr_hover_first_element(browser, 7)
        self.set_attr_selected_first_element(browser, 7)
        self.select_type_key_list_first_element(browser, 7)
        self.click_field_select_device(browser)

        # Check that selected of device dropdown is empty
        self.visible_el_select_dropdown_empty(browser)

    @pytest.mark.auth
    def test_invalid_key(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)
        time.sleep(1)
        assert self.check_text_in_ub_dialog_break_word(browser) in message_text_invalid_cert_login_passw

    @pytest.mark.auth
    def test_invalid_passw_key(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level_w_o_added_certificate(browser, test_name)

        # Check
        self.check_text_message_invalid_passw_of_key(browser)

    @pytest.mark.auth
    def test_spec_char_in_login(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)
        time.sleep(1)
        assert self.check_text_in_ub_dialog_break_word(browser) in message_text_invalid_cert_login_passw

    @pytest.mark.auth
    def test_spec_char_in_passw(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)
        time.sleep(1)
        assert self.check_text_in_ub_dialog_break_word(browser) in message_text_invalid_cert_login_passw

    # Только пробелы в поле
    @pytest.mark.auth
    def test_space_char_in_login(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)
        time.sleep(1)
        assert self.check_text_in_ub_dialog_break_word(browser) in message_text_invalid_cert_login_passw

    # Только пробелы в поле
    @pytest.mark.auth
    def test_space_char_in_passw(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)
        time.sleep(1)
        assert self.check_text_in_ub_dialog_break_word(browser) in message_text_invalid_cert_login_passw

    # Несколько пробелов в начале и в конце  текста
    @pytest.mark.auth
    def test_space_char_in_text_login(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)

        # Check
        self.check_visible_u_navbar_dropdown(browser)

    # Несколько пробелов в начале и в конце  текста
    @pytest.mark.auth
    def test_space_char_in_text_passw(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)
        time.sleep(1)
        assert self.check_text_in_ub_dialog_break_word(browser) in message_text_invalid_cert_login_passw

    @pytest.mark.skip
    @pytest.mark.auth
    def test_xss_in_login(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)
        time.sleep(1)
        assert self.check_text_in_ub_dialog_break_word(browser) in message_text_invalid_cert_login_passw

    @pytest.mark.skip
    @pytest.mark.auth
    def test_html_tags_in_login(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)
        time.sleep(1)
        assert self.check_text_in_ub_dialog_break_word(browser) in message_text_invalid_cert_login_passw

    @pytest.mark.skip
    @pytest.mark.auth
    def test_sql_in_login(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)
        time.sleep(1)
        assert self.check_text_in_ub_dialog_break_word(browser) in message_text_invalid_cert_login_passw

    @pytest.mark.auth
    def test_back_page(self, start_browser, request):
        test_name = request.node.name
        browser = start_browser
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level_wo_click(browser, test_name)
        browser.back()
        browser.forward()

        # Check
        self.visible_entry(browser)

    @pytest.mark.auth
    def test_user_session_mode_displacing(self, start_browser, request):
        test_name = request.node.name
        host = data_auth_test.get(test_name).get('host')
        browser = start_browser
        browser.get(host)
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)
        self.check_visible_u_navbar_dropdown(browser)

        browser.execute_script('window.open("{url}");'.format(url=host))
        browser.switch_to_window(browser.window_handles[1])
        self.clear_text_user_field(browser)
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level_w_o_added_certificate(browser, test_name)

        self.check_visible_u_navbar_dropdown(browser)
        browser.switch_to_window(browser.window_handles[0])
        DrrpCommonPage().click_main_menu_statement(browser)
        time.sleep(2)
        DrrpStatementPage().click_sub_menu_create_statement(browser)
        AuthPage().check_visible_field_user(browser)

    @pytest.mark.auth
    def test_user_session_mode_singleton(self, start_browser, request):
        test_name = request.node.name
        host = data_auth_test.get(test_name).get('host')
        browser = start_browser
        browser.get(host)
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level(browser, test_name)
        self.check_visible_u_navbar_dropdown(browser)

        browser.execute_script('window.open("{url}");'.format(url=host))
        browser.switch_to_window(browser.window_handles[1])
        self.clear_text_user_field(browser)
        self.login_auth_first_level(browser, test_name)
        self.login_auth_second_level_w_o_added_certificate(browser, test_name)
        time.sleep(2)
        self.check_text_message_session_mode_singleton(browser, message_text_session_mode_singleton)
        browser.switch_to_window(browser.window_handles[0])
        DrrpCommonPage().click_main_menu_statement(browser)
        time.sleep(2)
        DrrpStatementPage().click_sub_menu_create_statement(browser)
        self.logout(browser)




