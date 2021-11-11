import time

import allure
import pytest

from service.auth.methods.auth_method import AuthMethod
from service.erk.pages.common_page import ErkCommonPage
from service.erk.pages.employee_page import ErkEmployeePage
from service.erk.pages.main_page import ErkMainPage
from settings import setting_erk_data_info


@allure.severity(allure.severity_level.NORMAL)
class TestErkEmployee(AuthMethod, ErkMainPage, ErkCommonPage, ErkEmployeePage):
    dict_employee = {}
    dict_employee['company_name'] = setting_erk_data_info.company['operation_company_name']

    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_employee
    def test_create_employee(self, start_session):
        browser = start_session
        self.click_desktop_select_button(browser)
        self.click_u_desktop_drawer_item_title(browser)
        self.visible_desktop_select_button_users(browser)
        self.click_label_operations(browser)
        self.visible_label_search_is_opened(browser)
        self.check_invisible_v_enter_active(browser)
        self.click_sublabel_employee(browser)
        self.click_btn_menu_add(browser)
        self.visible_operation_employee(browser)

        self.insert_value_operation_employee_company(browser, setting_erk_data_info.employee[
            'operation_employee_company'])
        time.sleep(1)
        self.select_operation_employee_company_list(browser)

        self.insert_value_operation_employee_category(browser, setting_erk_data_info.employee[
            'operation_employee_category'])
        time.sleep(1)
        self.select_operation_employee_category_list(browser)

        self.insert_value_field_last_name_employee_employee(browser, setting_erk_data_info.employee[
            'last_name_employee'])
        self.insert_value_field_first_name_employee_employee(browser, setting_erk_data_info.employee[
            'first_name_employee'])
        self.insert_value_field_father_name_employee_employee(browser, setting_erk_data_info.employee[
            'father_name_employee'])

        self.insert_value_field_position_employee(browser,
                                                  setting_erk_data_info.employee['operation_employee_position'])
        time.sleep(1)
        self.select_operation_employee_position_list(browser)
        self.insert_value_field_code_employee(browser, setting_erk_data_info.employee['code_employee'])
        self.insert_value_field_phone_operation_employee(browser, setting_erk_data_info.employee['phone_employee'])
        self.insert_value_field_additional_operation_employee(browser,
                                                              setting_erk_data_info.employee['additional_employee'])

        self.click_tab_attributes_operation_employee(browser)

        self.double_click_region_attributes_operation_employee(browser)
        self.visible_form_attribute_employee(browser)

        self.click_operation_employee_x_form_trigger_first(browser)
        self.select_operator_region_attributes_operation_employee_list(browser)

        self.click_btn_admit_employee(browser)
        self.double_click_date_open_attributes_operation_employee(browser)
        self.click_btn_admit_employee(browser)

        self.click_btn_save_and_close_operation_employee(browser)
        time.sleep(4)
        self.create_screenshot(browser)
        # import pdb;
        # pdb.set_trace()
