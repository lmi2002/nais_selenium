import time

from exception import InvisibleCountElementsException
from helpers import base
from service.erk.locators.common_locator import ErkCommonLocator
from service.erk.locators.employee_locator import ErkEmployeeLocator
from settings import setting_erk_data_info


class ErkEmployeePage(ErkEmployeeLocator, ErkCommonLocator):

    def click_tab_employee(self, driver):
        base.move_to_element_and_click(driver, self.tab_employee)

    def click_form_employee(self, driver):
        base.move_to_element_and_click(driver, self.fas_fa_plus_employee, index=1)

    def insert_value_field_category_employee(self, driver, value):
        base.get_web_elements(driver, self.field_category_employee)[1].send_keys(value)

    def select_category_employee_list(self, driver):
        base.move_to_element_and_click(driver, self.category_employee_list)

    def click_field_position_employee(self, driver):
        base.get_web_element(driver, self.field_position_employee)

    def insert_value_field_position_employee(self, driver, value):
        base.get_web_element(driver, self.field_position_employee).send_keys(value)

    def select_position_employee_list(self, driver):
        base.move_to_element_and_click(driver, self.position_employee_list)

    def insert_value_field_code_employee(self, driver, value):
        base.get_web_element(driver, self.field_code_employee).send_keys(value)

    def insert_value_field_asfo_employee(self, driver, value):
        base.get_web_elements(driver, self.field_asfo_employee)[1].send_keys(value)

    def insert_value_field_license_employee(self, driver, value):
        base.get_web_element(driver, self.field_license_employee).send_keys(value)

    def insert_value_field_additional_employee(self, driver, value):
        base.get_web_elements(driver, self.field_additional_employee)[1].send_keys(value)

    def insert_value_field_first_name_employee(self, driver, value):
        base.get_web_elements(driver, self.inputs_name_employee)[2].send_keys(value)

    def insert_value_field_first_name_employee_employee(self, driver, value):
        base.get_web_elements(driver, self.inputs_name_employee)[1].send_keys(value)

    def insert_value_field_last_name_employee(self, driver, value):
        base.get_web_elements(driver, self.inputs_name_employee)[1].send_keys(value)

    def insert_value_field_last_name_employee_employee(self, driver, value):
        base.get_web_elements(driver, self.inputs_name_employee)[0].send_keys(value)

    def insert_value_field_father_name_employee(self, driver, value):
        base.get_web_elements(driver, self.inputs_name_employee)[3].send_keys(value)

    def insert_value_field_father_name_employee_employee(self, driver, value):
        base.get_web_elements(driver, self.inputs_name_employee)[2].send_keys(value)

    def visible_form_edit_employee(self, driver):
        base.get_visible_element(driver, self.text_edit_employee)

    def insert_value_field_phone_employee(self, driver, value):
        base.get_web_elements(driver, self.field_phone_employee)[1].send_keys(value)

    def click_btn_save_form_employee(self, driver):
        base.move_to_element_and_click(driver, self.btn_save, index=1)

    def visible_tab_employee(self, driver):
        base.get_visible_element(driver, self.tab_employee)

    def click_tab_attributes_employee(self, driver, index=None):
        base.move_to_element_and_click(driver, self.tab_attributes_employee, index=index)

    def double_click_date_start_status_attributes_employee(self, driver):
        base.double_click_element(driver, self.date_start_status_attributes_employee)

    def double_click_operator_registrar_attributes_employee(self, driver):
        base.double_click_element(driver, self.operator_registrar_attributes_employee)

    def double_click_date_licence_attributes_employee(self, driver):
        base.double_click_element(driver, self.date_licence_attributes_employee)

    def double_click_notarius_status_attributes_employee(self, driver):
        base.double_click_element(driver, self.notarius_status_attributes_employee)

    def double_click_notarius_position_attributes_employee(self, driver):
        base.double_click_element(driver, self.notarius_position_attributes_employee)

    def click_btn_admit_employee(self, driver):
        base.move_to_element_and_click(driver, self.btn_admit_employee)

    def insert_value_field_value_attributes_employee(self, driver, value, index=None):
        elem = base.move_to_element_and_click(driver, self.field_value_attributes_employee, index=index)
        elem.send_keys(value)

    def click_value_field_value_attributes_employee(self, driver, index=None):
        base.move_to_element_and_click(driver, self.field_value_attributes_employee, index=index)

    def select_operator_registrar_attributes_employee_list(self, driver):
        base.move_to_element_and_click(driver, self.operator_registrar_attributes_employee_list)

    def visible_form_attribute_employee(self, driver):
        base.get_visible_element(driver, self.form_attribute_employee)

    def select_notarius_status_attributes_employee_list(self, driver):
        base.move_to_element_and_click(driver, self.notarius_status_attributes_employee_list)

    def select_notarius_position_attributes_employee_list(self, driver, index=None):
        base.move_to_element_and_click(driver, self.notarius_position_attributes_employee_list, index=index)

    def click_btn_save_and_close_employee(self, driver, index=None):
        base.move_to_element_and_click(driver, self.btn_save_and_close_employee, index=index)

    def click_btn_save_and_close_operation_employee(self, driver):
        base.move_to_element_and_click(driver, self.btn_save_and_close_employee)

    def check_invisible_form_edit_employee(self, driver):
        base.check_invisible_element(driver, self.text_edit_employee)

    def check_text_fio_company_employee(self, driver):
        base.get_element_containing_text(driver,
                                         '{last_name_company_employee} {first_name_company_employee} {father_name_employee}'.format(
                                             last_name_company_employee=setting_erk_data_info.employee[
                                                 'last_name_company_employee'],
                                             first_name_company_employee=setting_erk_data_info.employee[
                                                 'first_name_company_employee'],
                                             father_name_employee=setting_erk_data_info.employee[
                                                 'father_name_employee']))

    def visible_operation_employee(self, driver):
        base.get_visible_element(driver, self.text_edit_operation_employee)

    def insert_value_operation_employee_company(self, driver, value):
        base.get_web_element(driver, self.operation_employee_company).send_keys(value)

    def select_operation_employee_company_list(self, driver):
        base.move_to_element_and_click(driver, self.operation_employee_company_list)

    def insert_value_operation_employee_category(self, driver, value):
        base.get_web_element(driver, self.field_category_employee).send_keys(value)

    def select_operation_employee_category_list(self, driver):
        base.move_to_element_and_click(driver, self.operation_employee_category_list)

    def select_operation_employee_position_list(self, driver):
        base.move_to_element_and_click(driver, self.operation_employee_position_list)

    def select_operation_employee_notarius_position(self, driver):
        base.move_to_element_and_click(driver, self.operation_employee_notarius_position)

    def insert_value_field_phone_operation_employee(self, driver, value):
        base.get_web_element(driver, self.field_phone_employee).send_keys(value)

    def insert_value_field_additional_operation_employee(self, driver, value):
        base.get_web_element(driver, self.field_additional_employee).send_keys(value)

    def click_tab_attributes_operation_employee(self, driver):
        base.move_to_element_and_click(driver, self.tab_attributes_employee)

    def double_click_date_open_attributes_operation_employee(self, driver):
        base.double_click_element(driver, self.date_open_attributes_operation_employee)

    def double_click_region_attributes_operation_employee(self, driver):
        base.double_click_element(driver, self.region_attributes_operation_employee)

    def select_operator_region_attributes_operation_employee_list(self, driver):
        driver.execute_script("document.querySelectorAll('.x-list-plain')[3].querySelectorAll('li')[1].click()")

    def click_operation_employee_x_form_trigger_first(self, driver):
        base.move_to_element_and_click(driver, self.operation_employee_x_form_trigger_first, index=8)

    def count_elem_x_grid_data_row_employee(self, driver):
        return len(base.get_web_elements(driver, self.x_grid_data_row_employee))

    def double_click_x_grid_data_row_employee(self, driver):
        base.double_click_element(driver, self.x_grid_data_row_employee)

    def click_tab_substitution_employee(self, driver):
        base.move_to_element_and_click(driver, self.tab_substitution_employee)

    def click_form_substitution_employee(self, driver):
        base.move_to_element_and_click(driver, self.fas_fa_plus_employee)

    def visible_form_substitution_employee(self, driver):
        base.get_visible_element(driver, self.form_substitution_employee)

    def click_substitution_employee_category(self, driver):
        base.move_to_element_and_click(driver, self.field_substitution_employee, index=4)

    def click_substitution_employee_company(self, driver):
        base.move_to_element_and_click(driver, self.field_substitution_employee, index=5)

    def insert_substitution_employee_category(self, driver, value):
        base.get_web_elements(driver, self.field_substitution_employee)[4].send_keys(value)

    def select_substitution_employee_category_list(self, driver):
        base.move_to_element_and_click(driver, self.substitution_employee_category_list)

    def insert_substitution_employee_company(self, driver, value):
        base.get_web_elements(driver, self.field_substitution_employee)[5].send_keys(value)

    def select_substitution_employee_company_list(self, driver):
        base.move_to_element_and_click(driver, self.substitution_employee_company_list)

    def click_substitution_employee_region(self, driver):
        base.move_to_element_and_click(driver, self.substitution_employee_region)

    def insert_substitution_employee_region(self, driver, value):
        base.get_web_element(driver, self.substitution_employee_region).send_keys(value)

    def select_substitution_employee_region_list(self, driver):
        base.move_to_element_and_click(driver, self.substitution_employee_region_list)

    def click_substitution_employee_type(self, driver):
        base.move_to_element_and_click(driver, self.substitution_employee_type)

    def insert_substitution_employee_type(self, driver, value):
        base.get_web_element(driver, self.substitution_employee_type).send_keys(value)

    def select_substitution_employee_type_list(self, driver):
        base.move_to_element_and_click(driver, self.substitution_employee_type_list)

    def visible_tab_active_employee(self, driver):
        base.get_visible_element(driver, self.tab_active_employee)

    def visible_form_form_passed_employee(self, driver):
        base.get_visible_element(driver, self.form_passed_employee)

    def select_passed_employee_region_list(self, driver):
        base.move_to_element_and_click(driver, self.passed_employee_region_list)

    def insert_passed_employee_region(self, driver, value):
        base.get_web_element(driver, self.substitution_employee_region).send_keys(value)

    def select_passed_employee_category_company_list(self, driver):
        base.move_to_element_and_click(driver, self.passed_employee_category_company_list)

    def select_passed_employee_company_list(self, driver):
        base.move_to_element_and_click(driver, self.passed_employee_company_list)

    def click_passed_employee_category(self, driver):
        base.move_to_element_and_click(driver, self.field_substitution_employee, index=6)

    def insert_passed_employee_category(self, driver, value):
        base.get_web_elements(driver, self.field_substitution_employee)[6].send_keys(value)

    def select_passed_employee_category_list(self, driver):
        base.move_to_element_and_click(driver, self.passed_employee_category_list)

    def click_btn_continue_and_close_employee(self, driver):
        base.move_to_element_and_click(driver, self.btn_continue_and_close_employee)

    def visible_form_fio_employee_dublicated(self, driver):
        base.get_visible_element(driver, self.form_fio_employee_dublicated)

    def text_list_state_employee(self, driver):
        return [elem.text for elem in base.get_web_elements(driver, self.x_grid_cell_last)]

    def click_sse(self, driver):
        driver.execute_script("document.querySelectorAll('.x-list-plain')[3].querySelectorAll('li')[1].click()")

    def check_visible_row_employee(self, driver, count):
        timeout = base.timeout
        poll = 0.5
        end_time = time.time() + timeout
        time.sleep(1)
        while True:
            count_elem = self.count_elem_x_grid_data_row_employee(driver)
            if count_elem < count:
                return True
            time.sleep(poll)
            if time.time() > end_time:
                break
        base.ssc.create_screenshot(driver)
        raise InvisibleCountElementsException(count)

