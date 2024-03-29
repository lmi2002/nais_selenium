import allure
import pytest

from helpers import func
from service.auth.methods.auth_method import AuthMethod
from service.erc.pages.common_page import ErcCommonPage
from service.erc.pages.main_page import ErcMainPage
from service.erc.pages.search_page import ErcSearchPage
from settings import setting_erc_data_info, setting_project


@allure.severity(allure.severity_level.NORMAL)
class TestErcSearch(AuthMethod, ErcMainPage, ErcSearchPage, ErcCommonPage):

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_auth(self, start_session):
        browser = start_session
        data_admin = setting_project.project_rule.get('erc').get('admin')
        AuthMethod().login(browser, data_admin.get('username'), data_admin.get('passw'),
                            data_admin.get('key_path'), data_admin.get('passw_key'),
                            data_admin.get('certificate'))

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_open_page_search_company(self, start_session):
        browser = start_session
        if func.get_host_name() == setting_project.REMOTE_SERVER:
            self.click_u_sidebar_collapse_button(browser)
        self.click_desktop_select_button(browser)
        self.click_u_desktop_drawer_item_title(browser)
        self.visible_desktop_select_button_users(browser)
        self.click_label_search(browser)
        self.visible_label_search_is_opened(browser)
        self.click_sublabel_company(browser)
        assert self.visible_found_companyes(browser)
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_company_params_name(self, start_session):
        browser = start_session
        self.insert_value_field_name(browser, setting_erc_data_info.company['name'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) == 1
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_company_params_code(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_code(browser, setting_erc_data_info.company['code'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) == 1
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_company_params_category(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_company_category(browser)
        self.select_category_lawyers(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.skip
    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_company_params_state(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_state(browser)
        self.select_company_state_is_active(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_company_params_region(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_region(browser)
        self.select_region_kiev(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_company_params_address(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_address(browser, setting_erc_data_info.company['address'])
        self.select_company_address(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_company_params_rk(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_rk(browser, setting_erc_data_info.company['rk'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) == 1
        self.create_screenshot(browser)

    @pytest.mark.skip
    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_company_params_subord(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_subord(browser, setting_erc_data_info.company['subord'])
        self.click_field_subord(browser)
        self.select_subord_list(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_company_params_asfo(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_asfo(browser, setting_erc_data_info.company['asfo'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) == 1
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_company_params_index(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_index(browser, setting_erc_data_info.company['index'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) == 6
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_company_params_street(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_street(browser, setting_erc_data_info.company['street'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) == 13
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_open_page_search_employee(self, start_session):
        browser = start_session
        self.click_close_tab_admin_first(browser)
        self.click_search_sublabel_employee(browser)
        assert self.visible_found_employees(browser)
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_employee_params_fio(self, start_session):
        browser = start_session
        self.insert_value_field_employee_first_name(browser, setting_erc_data_info.employee['first_name'])
        self.insert_value_field_name(browser, setting_erc_data_info.employee['last_name'])
        self.insert_value_field_employee_father_name(browser, setting_erc_data_info.employee['father_name'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) == 1
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_employee_params_license(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_employee_license(browser, setting_erc_data_info.employee['license'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) == 1
        self.create_screenshot(browser)

    @pytest.mark.skip
    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_employee_params_state(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_state(browser)
        self.select_employee_state_is_active(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_employee_params_category(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_employee_category(browser)
        self.select_employee_category_gov_notar(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_employee_params_position(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_employee_position(browser)
        self.select_employee_position_engineer(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_employee_params_code(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_employee_code(browser, setting_erc_data_info.employee['code'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) == 1
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_employee_params_asfo(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_asfo(browser, setting_erc_data_info.employee['asfo'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) == 1
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_open_page_search_user(self, start_session):
        browser = start_session
        self.click_close_tab_admin_first(browser)
        self.click_sublabel_user(browser, index=1)
        assert self.visible_found_users(browser)
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_user_params_login(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_name(browser, setting_erc_data_info.user.get('username'))
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) == 1
        self.create_screenshot(browser)

    # Тест забирает всю память
    @pytest.mark.skip
    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_user_params_state(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_user_state(browser)
        self.select_user_state(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    # Тест забирает всю память
    @pytest.mark.skip
    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_user_params_user_web(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_user_user_web(browser)
        self.select_user_user_web(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_user_params_category(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_user_category(browser)
        self.select_user_category_gov_notar(browser)
        self.click_field_user_category(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_user_params_role_rk(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_user_role_rk(browser)
        self.select_user_role_rk(browser)
        self.click_field_user_role_rk(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_user_params_role_web(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_user_role_web(browser)
        self.select_user_role_web(browser)
        self.click_field_user_role_web(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_open_page_search_statement(self, start_session):
        browser = start_session
        self.click_close_tab_admin_first(browser)
        self.click_sublabel_search_statement(browser)
        assert self.visible_found_companyes(browser)
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_statement_params_st_num(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_statement_num(browser, setting_erc_data_info.statement['num'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) == 1
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_statement_params_employee(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_statement_employee(browser, setting_erc_data_info.statement['employee'])
        self.select_statement_employee_list(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_statement_params_fio(self, start_session):
        browser = start_session
        self.insert_value_field_employee_first_name(browser, setting_erc_data_info.statement['first_name'])
        self.insert_value_field_name(browser, setting_erc_data_info.statement['last_name'])
        self.insert_value_field_employee_father_name(browser, setting_erc_data_info.statement['father_name'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_statement_params_user(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_statement_user(browser, setting_erc_data_info.statement['user'])
        self.select_statement_user_list(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_statement_params_date_period(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.insert_value_field_statement_start_date(browser, setting_erc_data_info.statement['start_date'])
        self.insert_value_field_statement_end_date(browser, setting_erc_data_info.statement['end_date'])
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_statement_params_state(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_statement_state(browser)
        self.select_statement_state(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_statement_params_progress(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_statement_progress(browser)
        self.select_statement_progress(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)

    @pytest.mark.skip
    @pytest.mark.erc
    @pytest.mark.admin
    @pytest.mark.erc_search
    def test_search_statement_params_blocked(self, start_session):
        browser = start_session
        self.click_btn_clear(browser)
        self.check_invisible_tr_ubtableview(browser)
        self.click_field_statement_blocked(browser)
        self.select_statement_blocked(browser)
        self.click_btn_search(browser)
        assert self.count_elem_tr_ubtableview(browser) > 0
        self.create_screenshot(browser)
