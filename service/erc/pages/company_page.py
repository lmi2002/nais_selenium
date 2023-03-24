from helpers import base
from service.erc.locators.common_locator import ErcCommonLocator
from service.erc.locators.company_locator import ErcCompanyLocator


class ErcCompanyPage(ErcCompanyLocator, ErcCommonLocator):
    def visible_category(self, driver):
        base.get_visible_element(driver, self.operation_company_name_column_category)

    def visible_tab_general_statements_company(self, driver):
        base.get_visible_element(driver, self.tab_general_statements_company)

    def click_field_operation_company_category(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_ext_gen, index=1)

    def select_operation_category_name(self, driver):
        base.move_to_element_and_click(driver, self.operation_category_name)

    def insert_value_operation_company_name(self, driver, value):
        base.get_web_element(driver, self.operation_company_name).send_keys(value)

    def insert_value_operation_company_shortname(self, driver, value):
        base.get_web_element(driver, self.operation_company_shortname).send_keys(value)

    def insert_value_operation_company_phone(self, driver, value):
        base.get_web_element(driver, self.operation_company_phone).send_keys(value)

    def insert_value_operation_company_edrpou(self, driver, value):
        base.get_web_element(driver, self.operation_company_edrpou).send_keys(value)

    def insert_value_operation_company_asfo(self, driver, value):
        base.get_web_element(driver, self.operation_company_asfo).send_keys(value)

    def insert_value_operation_company_address_street(self, driver, value):
        base.get_web_element(driver, self.operation_company_address_street).send_keys(value)

    def click_operation_company_locality(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_ext_gen, index=3)

    def click_operation_company_region(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_ext_gen, index=4)

    def select_operation_company_locality(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_locality)

    def select_operation_company_region(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_region)

    def insert_value_operation_company_locality(self, driver, value):
        base.get_web_elements(driver, self.operation_company_ubcombobox)[1].send_keys(value)

    def insert_value_field_operation_category_region(self, driver, value):
        base.get_web_element(driver, self.field_operation_category_region).send_keys(value)

    def insert_value_field_operation_category_name(self, driver, value):
        base.get_web_element(driver, self.field_operation_category_name).send_keys(value)

    def insert_value_operation_company_address_index(self, driver, value):
        base.get_web_element(driver, self.operation_company_address_index).send_keys(value)

    def insert_value_field_operation_category_address_address(self, driver, value):
        base.get_web_element(driver, self.field_operation_category_address_address).send_keys(value)

    def select_operation_company_address_address(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_address_address)

    def click_operation_company_post(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_post)

    def insert_value_operation_company_post_index(self, driver, value):
        base.get_web_element(driver, self.operation_company_post_index).send_keys(value)

    def insert_value_field_operation_company_post_address(self, driver, value):
        base.get_web_element(driver, self.field_operation_company_post_address).send_keys(value)

    def insert_value_operation_company_post_street(self, driver, value):
        base.get_web_element(driver, self.operation_company_post_street).send_keys(value)

    def select_operation_company_post_address(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_post_address, index=1)

    def insert_value_operation_company_subord(self, driver, value):
        base.get_web_elements(driver, self.operation_company_ubcombobox)[3].send_keys(value)

    def select_operation_company_subord_list(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_subord_list)

    def click_operation_company_subord(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_subord)

    def click_btn_save(self, driver):
        base.move_to_element_and_click(driver, self.btn_save)

    def click_tab_service_area(self, driver):
        base.move_to_element_and_click(driver, self.tab_service_area)

    def click_tab_rename_company(self, driver):
        base.move_to_element_and_click(driver, self.tab_rename_company)

    def click_btn_edit_service_area(self, driver):
        base.move_to_element_and_click(driver, self.btn_edit_service_area)

    def visible_text_edit_service_area(self, driver):
        base.get_visible_element(driver, self.text_edit_service_area)

    def click_list_service_area(self, driver):
        base.move_to_element_and_click(driver, self.list_service_area)

    def click_add_service_area(self, driver):
        base.move_to_element_and_click(driver, self.fas_fa_angle_right)

    def click_btn_company_exit_form(self, driver):
        base.move_to_element_and_click(driver, self.btn_company_exit_form)

    def count_elem_grid_company(self, driver):
        return len(base.get_web_elements(driver, self.grid_company))

    def click_form_rename_company(self, driver):
        base.move_to_element_and_click(driver, self.fas_fa_plus_company)

    def insert_value_field_rename_company(self, driver, value):
        elem = base.move_to_element_and_click(driver, self.inputs_rename_company, index=1)
        elem.send_keys(value)

    def insert_value_field_shortname_company(self, driver, value):
        elem = base.move_to_element_and_click(driver, self.inputs_rename_company, index=2)
        elem.send_keys(value)

    def insert_value_rename_company_date(self, driver, value):
        elem = base.move_to_element_and_click(driver, self.input_rename_company_date)
        elem.send_keys(value)

    def insert_input_textfield_rename_company(self, driver, value):
        base.get_web_elements(driver, self.input_textfield_rename_company)[13].send_keys(value)

    def check_text_rename_company(self, driver, text):
        base.get_element_containing_text(driver, text)

    def visible_form_edit_rename_company(self, driver):
        base.get_visible_element(driver, self.text_edit_rename_company)

    def click_tab_doc_company(self, driver):
        base.move_to_element_and_click(driver, self.tab_doc_company)

    def click_form_doc_company(self, driver):
        base.move_to_element_and_click(driver, self.fas_fa_plus_company, index=1)

    def visible_form_scan_doc_company(self, driver):
        base.get_visible_element(driver, self.text_scan_doc_company)

    def click_btn_add_scan_doc(self, driver):
        base.move_to_element_and_click(driver, self.btn_add_scan_doc)

    def click_btn_add_file(self, driver):
        base.move_to_element_and_click(driver, self.btn_add_file)

    def insert_value_input_select_file(self, driver, value):
        elem = base.move_to_element_and_click(driver, self.input_select_file)
        elem.send_keys(value)
