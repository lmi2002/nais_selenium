from helpers import base
from service.erk.locators.company_locator import ErkCompanyLocator


class ErkCompanyPage(ErkCompanyLocator):
    def visible_short_name(self, driver):
        base.get_visible_element(driver, self.operation_company_short_name)

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

    def insert_value_operation_company_post_index(self, driver, value):
        base.get_web_element(driver, self.operation_company_post_index).send_keys(value)

    def insert_value_operation_company_post_street(self, driver, value):
        base.get_web_element(driver, self.operation_company_post_street).send_keys(value)

    def click_operation_company_locality(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_ext_gen, index=3)

    def click_operation_company_region(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_ext_gen, index=4)

    def select_operation_company_locality(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_locality)

    def select_peration_company_region(self, driver):
        base.move_to_element_and_click(driver, self.operation_company_region)

    def insert_value_operation_company_locality(self, driver, value):
        base.get_web_elements(driver, self.operation_company_ubcombobox)[1].send_keys(value)

    def insert_value_operation_company_category(self, driver, value):
        base.get_web_element(driver, self.operation_category_name).send_keys(value)
