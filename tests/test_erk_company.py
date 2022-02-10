import time

import allure
import pytest

from helpers import func
from helpers.func import get_data_tomorrow
from service.auth.methods.auth_method import AuthMethod
from service.erk.pages.common_page import ErkCommonPage
from service.erk.pages.company_page import ErkCompanyPage
from service.erk.pages.employee_page import ErkEmployeePage
from service.erk.pages.main_page import ErkMainPage
from settings import setting_erk_data_info
from settings.setting_project import REMOTE_SERVER


@allure.severity(allure.severity_level.NORMAL)
class TestErkCompany(AuthMethod, ErkMainPage, ErkCompanyPage, ErkCommonPage, ErkEmployeePage):
    dict_company = {}
    dict_company['company_name'] = setting_erk_data_info.company['operation_company_name']

    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_company
    def test_create_company(self, start_session):
        browser = start_session
        if func.get_host_name() == REMOTE_SERVER:
            self.click_u_sidebar_collapse_button(browser)
        self.click_desktop_select_button(browser)
        self.click_u_desktop_drawer_item_title(browser)
        self.visible_desktop_select_button_users(browser)
        if func.get_host_name() == REMOTE_SERVER:
            self.open_label_operations(browser)
        else:
            self.click_label_operations(browser)
            self.visible_label_search_is_opened(browser)
        self.click_sublabel_operation_company(browser)
        self.visible_category(browser)
        self.click_btn_menu_add(browser)
        self.visible_tab_general_statements_company(browser)
        self.click_field_operation_company_category(browser)

        self.insert_value_field_operation_category_name(browser,
                                                        setting_erk_data_info.company['operation_company_category'])
        time.sleep(2)
        self.select_operation_category_name(browser)
        time.sleep(1)
        self.insert_value_operation_company_name(browser, self.dict_company['company_name'])
        self.insert_value_operation_company_shortname(browser, self.dict_company['company_name'])
        self.insert_value_operation_company_phone(browser, setting_erk_data_info.company['operation_company_phone'])
        self.insert_value_operation_company_edrpou(browser, setting_erk_data_info.company['operation_company_edrpou'])
        self.insert_value_operation_company_asfo(browser, setting_erk_data_info.company['operation_company_asfo'])
        self.insert_value_operation_company_locality(browser,
                                                     setting_erk_data_info.company['operation_company_locality'])
        time.sleep(2)
        self.select_operation_company_locality(browser)
        self.click_operation_company_region(browser)
        self.insert_value_field_operation_category_region(browser,
                                                          setting_erk_data_info.company['operation_company_region'])
        time.sleep(2)
        self.select_operation_company_region(browser)

        self.insert_value_operation_company_address_index(browser,
                                                          setting_erk_data_info.company['operation_company_index'])
        self.insert_value_field_operation_category_address_address(browser,
                                                                   setting_erk_data_info.company[
                                                                       'operation_company_address'])
        time.sleep(2)
        self.select_operation_company_address_address(browser)

        self.insert_value_operation_company_address_street(browser,
                                                           setting_erk_data_info.company['operation_company_street'])

        self.click_operation_company_post(browser)

        self.insert_value_operation_company_post_index(browser, setting_erk_data_info.company[
            'operation_company_index'])

        self.insert_value_field_operation_company_post_address(browser, setting_erk_data_info.company[
            'operation_company_address'])

        time.sleep(2)
        self.select_operation_company_post_address(browser)

        self.insert_value_operation_company_post_street(browser,
                                                        setting_erk_data_info.company['operation_company_street'])

        self.click_operation_company_subord(browser)
        self.insert_value_operation_company_subord(browser, setting_erk_data_info.company['operation_company_subord'])
        self.select_operation_company_subord_list(browser)

        self.click_btn_save(browser)
        time.sleep(4)
        self.create_screenshot(browser)

    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_company
    def test_add_service_area(self, start_session):
        browser = start_session
        self.click_tab_service_area(browser)
        self.click_btn_edit_service_area(browser)
        self.visible_text_edit_service_area(browser)
        self.click_list_service_area(browser)
        self.click_add_service_area(browser)
        self.click_btn_company_exit_form(browser)
        self.click_btn_save(browser)
        assert self.count_elem_grid_company(browser) == 1
        self.create_screenshot(browser)

    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_company
    def test_rename_company(self, start_session):
        browser = start_session
        self.click_tab_rename_company(browser)
        self.click_form_rename_company(browser)
        self.visible_form_edit_rename_company(browser)
        self.insert_value_field_rename_company(browser, '{new}_{name}'.format(new="Переименование",
                                                                              name=self.dict_company[
                                                                                  'company_name']))
        self.insert_value_field_shortname_company(browser, '{new}_{name}'.format(new="Переименование",
                                                                                 name=self.dict_company[
                                                                                     'company_name']))
        self.insert_value_rename_company_date(browser, get_data_tomorrow())
        self.insert_input_textfield_rename_company(browser, 'Автотест')
        self.click_btn_company_exit_form(browser)
        self.check_text_rename_company(browser, '{new}_{name}'.format(new="Переименование",
                                                                      name=self.dict_company[
                                                                          'company_name']))
        self.create_screenshot(browser)

    # Не доделан!
    @pytest.mark.skip
    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_company
    def test_add_doc_company(self, start_session):
        browser = start_session
        self.click_tab_doc_company(browser)
        self.click_form_doc_company(browser)
        self.visible_form_scan_doc_company(browser)
        self.click_btn_add_scan_doc(browser)
        self.click_btn_add_file(browser)
        self.insert_value_input_select_file(browser, "122")
        self.create_screenshot(browser)

    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_company
    def test_add_employee_company(self, start_session):
        browser = start_session
        self.click_tab_employee(browser)
        self.click_form_employee(browser)
        self.visible_form_edit_employee(browser)
        self.insert_value_field_category_employee(browser,
                                                  setting_erk_data_info.employee['category_employee'])
        time.sleep(1)
        self.select_category_employee_list(browser)
        time.sleep(1)
        self.insert_value_field_last_name_employee(browser, setting_erk_data_info.employee[
            'last_name_company_employee'])
        self.insert_value_field_first_name_employee(browser, setting_erk_data_info.employee[
            'first_name_company_employee'])
        self.insert_value_field_father_name_employee(browser, setting_erk_data_info.employee[
            'father_name_employee'])
        self.insert_value_field_position_employee(browser,
                                                  setting_erk_data_info.employee['position_employee'])
        time.sleep(1)
        self.select_position_employee_list(browser)
        self.insert_value_field_code_employee(browser, setting_erk_data_info.employee['code_company_employee'])
        self.insert_value_field_asfo_employee(browser, setting_erk_data_info.employee['asfo_employee'])
        self.insert_value_field_license_employee(browser,
                                                 setting_erk_data_info.employee['code_employee'])
        self.insert_value_field_phone_employee(browser, setting_erk_data_info.employee['phone_employee'])
        self.insert_value_field_additional_employee(browser, setting_erk_data_info.employee['additional_employee'])

        self.click_tab_attributes_employee(browser, index=1)

        self.double_click_date_start_status_attributes_employee(browser)
        self.click_btn_admit_employee(browser)

        self.double_click_date_licence_attributes_employee(browser)
        self.click_btn_admit_employee(browser)

        self.double_click_operator_registrar_attributes_employee(browser)
        self.visible_form_attribute_employee(browser)
        self.insert_value_field_value_attributes_employee(browser,
                                                          setting_erk_data_info.employee[
                                                              'value_operator_registrar_attributes_employee'], index=1)

        self.select_operator_registrar_attributes_employee_list(browser)
        self.click_btn_admit_employee(browser)

        self.double_click_notarius_status_attributes_employee(browser)
        self.visible_form_attribute_employee(browser)
        self.insert_value_field_value_attributes_employee(browser,
                                                          setting_erk_data_info.employee[
                                                              'value_notarius_status_attributes_employee'], index=1)

        time.sleep(1)
        self.select_notarius_status_attributes_employee_list(browser)
        self.click_btn_admit_employee(browser)

        self.double_click_notarius_position_attributes_employee(browser)
        self.visible_form_attribute_employee(browser)
        self.insert_value_field_value_attributes_employee(browser,
                                                          setting_erk_data_info.employee[
                                                              'value_notarius_position_attributes_employee'], index=1)
        time.sleep(1)
        self.select_notarius_position_attributes_employee_list(browser, index=1)
        self.click_btn_admit_employee(browser)
        self.click_btn_save_and_close_employee(browser, index=1)
        self.check_invisible_form_edit_employee(browser)
        self.check_text_fio_company_employee(browser)
        self.create_screenshot(browser)
