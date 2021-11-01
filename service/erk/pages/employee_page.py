from helpers import base
from service.erk.locators.common_locator import ErkCommonLocator
from service.erk.locators.employee_locator import ErkEmployeeLocator
from settings import setting_erk_data_info


class ErkEmployeePage(ErkEmployeeLocator, ErkCommonLocator):

    def click_tab_employee(self, driver):
        base.move_to_element_and_click(driver, self.tab_employee)

    def click_form_employee(self, driver):
        base.move_to_element_and_click(driver, self.fas_fa_plus_employee)

    def insert_value_field_category_employee(self, driver, value):
        base.get_web_elements(driver, self.field_category_employee)[1].send_keys(value)

    def select_category_employee_list(self, driver):
        base.move_to_element_and_click(driver, self.category_employee_list)

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

    def insert_value_field_last_name_employee(self, driver, value):
        base.get_web_elements(driver, self.inputs_name_employee)[1].send_keys(value)

    def insert_value_field_father_name_employee(self, driver, value):
        base.get_web_elements(driver, self.inputs_name_employee)[3].send_keys(value)

    def visible_form_edit_employee(self, driver):
        base.get_visible_element(driver, self.text_edit_employee)

    def insert_value_field_phone_employee(self, driver, value):
        base.get_web_elements(driver, self.field_phone_employee)[1].send_keys(value)

    def click_btn_save_form_employee(self, driver):
        base.move_to_element_and_click(driver, self.btn_save, index=1)

    def visible_tab_employee(self, driver):
        base.get_visible_element(driver, self.tab_employee)

    def click_tab_attributes_employee(self, driver):
        base.move_to_element_and_click(driver, self.tab_attributes_employee, index=1)

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

    def insert_value_field_value_attributes_employee(self, driver, value):
        elem = base.move_to_element_and_click(driver, self.field_value_attributes_employee, index=1)
        elem.send_keys(value)

    def select_operator_registrar_attributes_employee_list(self, driver):
        base.move_to_element_and_click(driver, self.operator_registrar_attributes_employee_list)

    def visible_form_attribute_employee(self, driver):
        base.get_visible_element(driver, self.form_attribute_employee)

    def select_notarius_status_attributes_employee_list(self, driver):
        base.move_to_element_and_click(driver, self.notarius_status_attributes_employee_list)

    def select_notarius_position_attributes_employee_list(self, driver):
        base.move_to_element_and_click(driver, self.notarius_position_attributes_employee_list, index=1)

    def click_btn_save_and_close_employee(self, driver):
        base.move_to_element_and_click(driver, self.btn_save_and_close_employee, index=1)

    def check_invisible_form_edit_employee(self, driver):
        base.check_invisible_element(driver, self.text_edit_employee)

    def check_text_fio_employee(self, driver):
        base.get_element_containing_text(driver,
                                         '{last_name_employee} {first_name_employee} {father_name_employee}'.format(
                                             last_name_employee=setting_erk_data_info.employee['last_name_employee'],
                                             first_name_employee=setting_erk_data_info.employee['first_name_employee'],
                                             father_name_employee=setting_erk_data_info.employee[
                                                 'father_name_employee']))
