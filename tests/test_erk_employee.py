import time

import allure
import pytest

from helpers import func
from service.auth.methods.auth_method import AuthMethod
from service.erk.method.common_method import ErkMethodMain
from service.erk.pages.employee_page import ErkEmployeePage
from service.erk.pages.main_page import ErkMainPage
from settings import setting_erk_data_info, setting_project


@allure.severity(allure.severity_level.NORMAL)
class TestErkEmployee(AuthMethod, ErkMainPage, ErkMethodMain, ErkEmployeePage):
    dict_employee = {}
    dict_employee['company_name'] = setting_erk_data_info.company['operation_company_name']
    dict_employee[
        'fio_employee'] = '{last_name_employee}{space}{first_name_employee}{space}{father_name_employee}'.format(
        first_name_employee=setting_erk_data_info.employee['first_name_employee'],
        last_name_employee=setting_erk_data_info.employee['last_name_employee'],
        father_name_employee=setting_erk_data_info.employee['father_name_employee'],
        space=" ")

    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_employee
    def test_auth(self, start_session):
        browser = start_session
        data_admin = setting_project.project_rule.get('erk').get('admin')
        AuthMethod().login(browser, data_admin.get('username'), data_admin.get('passw'),
                            data_admin.get('key_path'), data_admin.get('passw_key'),
                            data_admin.get('certificate'))

    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_employee
    def test_create_employee(self, start_session):
        browser = start_session
        if func.get_host_name() == setting_project.REMOTE_SERVER:
            self.click_u_sidebar_collapse_button(browser)

        self.click_desktop_select_button(browser)
        self.click_u_desktop_drawer_item_title(browser)
        self.visible_desktop_select_button_users(browser)
        if func.get_host_name() == setting_project.REMOTE_SERVER:
            self.open_label_operations(browser)
        else:
            self.click_label_operations(browser)
            self.visible_label_search_is_opened(browser)
            self.check_invisible_v_enter_active(browser)
        self.click_sublabel_employee(browser)
        self.click_btn_menu_add(browser)
        self.visible_operation_employee(browser)

        self.insert_value_operation_employee_company(browser, setting_erk_data_info.employee[
            'operation_employee_company'])
        time.sleep(2)
        self.select_operation_employee_company_list(browser)

        self.insert_value_operation_employee_category(browser, setting_erk_data_info.employee[
            'operation_employee_category'])
        time.sleep(2)
        self.select_operation_employee_category_list(browser)

        time.sleep(2)
        self.insert_value_field_last_name_employee_employee(browser, setting_erk_data_info.employee[
            'last_name_employee'])
        self.insert_value_field_first_name_employee_employee(browser, setting_erk_data_info.employee[
            'first_name_employee'])
        self.insert_value_field_father_name_employee_employee(browser, setting_erk_data_info.employee[
            'father_name_employee'])

        self.insert_value_field_position_employee(browser,
                                                  setting_erk_data_info.employee['operation_employee_position'])
        time.sleep(2)
        self.select_operation_employee_position_list(browser)
        self.insert_value_field_code_employee(browser, setting_erk_data_info.employee['code_employee'])
        self.insert_value_field_phone_operation_employee(browser, setting_erk_data_info.employee['phone_employee'])
        self.insert_value_field_additional_operation_employee(browser,
                                                              setting_erk_data_info.employee['additional_employee'])

        self.click_tab_attributes_operation_employee(browser)

        self.double_click_region_attributes_operation_employee(browser)
        self.visible_form_attribute_employee(browser)

        self.click_value_field_value_attributes_employee(browser, index=2)
        self.click_operation_employee_x_form_trigger_first(browser)
        time.sleep(2)
        self.select_operator_region_attributes_operation_employee_list(browser)
        self.click_btn_admit_employee(browser)
        self.double_click_date_open_attributes_operation_employee(browser)
        self.click_btn_admit_employee(browser)

        self.click_btn_save_and_close_operation_employee(browser)

        time.sleep(5)
        self.filter_form(browser, setting_erk_data_info.employee['code_employee'], index=5)
        time.sleep(2)
        assert self.count_elem_x_grid_data_row_employee(browser) == 1
        self.create_screenshot(browser)

    @pytest.mark.erk
    @pytest.mark.admin
    def test_add_substitution_employee(self, start_session):
        browser = start_session
        self.double_click_x_grid_data_row_employee(browser)
        self.click_close_tab_admin_first(browser)
        self.visible_tab_active_employee(browser)
        self.click_tab_substitution_employee(browser)
        self.click_form_substitution_employee(browser)
        self.visible_form_substitution_employee(browser)

        self.click_substitution_employee_region(browser)
        self.insert_substitution_employee_region(browser,
                                                 setting_erk_data_info.employee['substitution_employee_region'])
        self.select_substitution_employee_region_list(browser)

        self.click_substitution_employee_category(browser)
        self.insert_substitution_employee_category(browser,
                                                   setting_erk_data_info.employee['substitution_employee_category'])
        self.select_substitution_employee_category_list(browser)

        self.click_substitution_employee_company(browser)

        self.insert_substitution_employee_company(browser,
                                                  setting_erk_data_info.employee['substitution_employee_company'])
        self.select_substitution_employee_company_list(browser)

        self.click_substitution_employee_type(browser)
        self.insert_substitution_employee_type(browser, setting_erk_data_info.employee['substitution_employee_type'])
        self.select_substitution_employee_type_list(browser)
        self.click_btn_admit_employee(browser)
        assert self.count_elem_x_grid_data_row_employee(browser) == 1
        self.create_screenshot(browser)

    @pytest.mark.erk
    @pytest.mark.admin
    def test_employee_passed_company(self, start_session):
        browser = start_session
        self.click_btn_change_company(browser)
        self.visible_form_form_passed_employee(browser)
        self.click_substitution_employee_region(browser)
        self.insert_passed_employee_region(browser,
                                           setting_erk_data_info.employee['passed_employee_new_region'])
        self.select_passed_employee_region_list(browser)

        self.click_substitution_employee_category(browser)
        self.insert_substitution_employee_category(browser,
                                                   setting_erk_data_info.employee[
                                                       'passed_employee_new_category_company'])
        self.select_passed_employee_category_company_list(browser)
        self.click_substitution_employee_company(browser)
        self.insert_substitution_employee_company(browser,
                                                  setting_erk_data_info.employee['passed_employee_new_company'])
        time.sleep(2)
        self.select_passed_employee_company_list(browser)
        self.click_passed_employee_category(browser)
        time.sleep(2)
        self.insert_passed_employee_category(browser,
                                             setting_erk_data_info.employee['passed_employee_new_category_employee'])

        time.sleep(2)
        self.select_passed_employee_category_list(browser)
        self.click_btn_continue_and_close_employee(browser)
        self.visible_operation_employee(browser)
        self.click_field_position_employee(browser)
        self.insert_value_field_position_employee(browser,
                                                  setting_erk_data_info.employee['position_employee'])
        time.sleep(2)
        self.select_operation_employee_notarius_position(browser)

        self.click_tab_attributes_employee(browser)

        self.double_click_date_start_status_attributes_employee(browser)
        self.click_btn_admit_employee(browser)

        self.double_click_date_licence_attributes_employee(browser)
        self.click_btn_admit_employee(browser)

        self.double_click_operator_registrar_attributes_employee(browser)
        self.visible_form_attribute_employee(browser)

        time.sleep(2)
        self.insert_value_field_value_attributes_employee(browser,
                                                          setting_erk_data_info.employee[
                                                              'value_operator_registrar_attributes_employee'], index=1)

        self.select_operator_registrar_attributes_employee_list(browser)
        self.click_btn_admit_employee(browser)

        self.double_click_notarius_status_attributes_employee(browser)
        self.visible_form_attribute_employee(browser)
        time.sleep(2)
        self.insert_value_field_value_attributes_employee(browser,
                                                          setting_erk_data_info.employee[
                                                              'value_notarius_status_attributes_employee'], index=1)

        time.sleep(2)
        self.select_notarius_status_attributes_employee_list(browser)
        self.click_btn_admit_employee(browser)

        self.double_click_notarius_position_attributes_employee(browser)
        self.visible_form_attribute_employee(browser)
        time.sleep(2)
        self.insert_value_field_value_attributes_employee(browser,
                                                          setting_erk_data_info.employee[
                                                              'value_notarius_position_attributes_employee'], index=1)
        time.sleep(2)
        self.select_notarius_position_attributes_employee_list(browser)
        self.click_btn_admit_employee(browser)
        self.click_btn_save_and_close_employee(browser)

        self.visible_form_fio_employee_dublicated(browser)
        self.click_button_continue(browser)
        self.check_invisible_form_edit_employee(browser)
        self.click_sublabel_employee(browser)
        self.filter_form(browser, self.dict_employee['fio_employee'], index=3)
        self.check_visible_row_employee(browser, 3)
        assert self.text_list_state_employee(browser) == ['діє', 'не діє']
        self.create_screenshot(browser)
