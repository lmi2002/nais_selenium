from helpers import base
from service.erk.locators.search_locator import ErkSearchLocator


class ErkSearchPage(ErkSearchLocator):

    def insert_value_field_name(self, driver, value):
        base.get_web_element(driver, self.field_name).send_keys(value)

    def insert_value_field_code(self, driver, value):
        base.get_web_element(driver, self.field_code).send_keys(value)

    def click_field_company_category(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=2)

    def click_field_employee_category(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=1)

    def select_category_lawyers(self, driver):
        base.move_to_element_and_click(driver, self.category_lawyers)

    def select_employee_category_gov_notar(self, driver):
        base.move_to_element_and_click(driver, self.employee_category_gov_notar)

    def click_field_state(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=3)

    def select_company_state_is_active(self, driver):
        base.move_to_element_and_click(driver, self.company_state_is_active)

    def select_employee_state_is_active(self, driver):
        base.move_to_element_and_click(driver, self.employee_state_is_active)

    def click_field_region(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=4)

    def select_region_kiev(self, driver):
        base.move_to_element_and_click(driver, self.region_kiev)

    def select_employee_position_engineer(self, driver):
        base.move_to_element_and_click(driver, self.employee_position_engineer)

    def click_field_address(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=5)

    def select_company_address(self, driver):
        base.move_to_element_and_click(driver, self.company_address, index=0)

    def insert_value_field_rk(self, driver, value):
        base.get_web_element(driver, self.field_rk).send_keys(value)

    def click_field_subord(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen)

    def select_subord_list(self, driver):
        base.move_to_element_and_click(driver, self.x_list_plain, index=9)

    def insert_value_field_asfo(self, driver, value):
        base.get_web_element(driver, self.field_asfo).send_keys(value)

    def insert_value_field_index(self, driver, value):
        base.get_web_element(driver, self.field_index).send_keys(value)

    def insert_value_field_street(self, driver, value):
        base.get_web_element(driver, self.field_street).send_keys(value)

    def insert_value_field_address(self, driver, value):
        base.get_web_element(driver, self.field_address).send_keys(value)

    def insert_value_field_subord(self, driver, value):
        base.get_web_element(driver, self.field_subord).send_keys(value)

    def insert_value_field_employee_first_name(self, driver, value):
        base.get_web_element(driver, self.field_employee_first_name).send_keys(value)

    def insert_value_field_employee_father_name(self, driver, value):
        base.get_web_element(driver, self.field_employee_father_name).send_keys(value)

    def visible_found_employees(self, driver):
        return base.get_visible_elements(driver, self.found_employees)

    def visible_found_users(self, driver):
        return base.get_visible_elements(driver, self.found_users)

    def visible_found_companyes(self, driver):
        return base.get_visible_elements(driver, self.found_companyes)

    def insert_value_field_employee_license(self, driver, value):
        base.get_web_element(driver, self.field_employee_license).send_keys(value)

    def click_field_employee_position(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=2)

    def insert_value_field_employee_code(self, driver, value):
        base.get_web_element(driver, self.field_employee_code).send_keys(value)

    def click_field_user_state(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=1)

    def select_user_state(self, driver):
        base.move_to_element_and_click(driver, self.user_state)

    def click_field_user_user_web(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=2)

    def select_user_user_web(self, driver):
        base.move_to_element_and_click(driver, self.user_user_web)

    def click_field_user_category(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=3)

    def select_user_category_gov_notar(self, driver):
        base.move_to_element_and_click(driver, self.user_category_gov_notar)

    def click_field_user_role_rk(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=4)

    def select_user_role_rk(self, driver):
        base.move_to_element_and_click(driver, self.user_role_rk)

    def click_field_user_role_web(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=5)

    def select_user_role_web(self, driver):
        base.move_to_element_and_click(driver, self.user_role_web)

    def insert_value_field_statement_num(self, driver, value):
        base.get_web_element(driver, self.field_statement_num).send_keys(value)

    def insert_value_field_statement_employee(self, driver, value):
        base.get_web_element(driver, self.field_statement_employee).send_keys(value)

    def select_statement_employee_list(self, driver):
        base.move_to_element_and_click(driver, self.statement_employee_list, index=2)

    def insert_value_field_statement_user(self, driver, value):
        base.get_web_element(driver, self.field_statement_user).send_keys(value)

    def select_statement_user_list(self, driver):
        base.move_to_element_and_click(driver, self.statement_user_list)

    def insert_value_field_statement_start_date(self, driver, value):
        base.get_web_element(driver, self.field_statement_start_date).send_keys(value)

    def insert_value_field_statement_end_date(self, driver, value):
        base.get_web_element(driver, self.field_statement_end_date).send_keys(value)

    def click_field_statement_state(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=4)

    def select_statement_state(self, driver):
        base.move_to_element_and_click(driver, self.statement_state)

    def click_field_statement_progress(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=5)

    def select_statement_progress(self, driver):
        base.move_to_element_and_click(driver, self.statement_progress)

    def click_field_statement_blocked(self, driver):
        base.move_to_element_and_click(driver, self.ext_gen, index=6)

    def select_statement_blocked(self, driver):
        base.move_to_element_and_click(driver, self.statement_blocked, index=1)



