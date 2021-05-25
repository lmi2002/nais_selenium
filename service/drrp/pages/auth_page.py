
from helpers import base
from service.drrp.locators.auth_locator import DrrpAuthLocator


class DrrpAuthPage(DrrpAuthLocator):

    def get_user(self, driver):
        return base.get_web_element(driver, self.user)

    def get_passw(self, driver):
        return base.get_web_elements(driver, self.passw)[1]

    def get_entry(self, driver):
        return base.get_web_element(driver, self.entry)

    def click_input_type_key(self, driver):
        base.move_to_element_and_click(driver, self.input_type_key)

    def select_type_key_list_first_element(self, driver):
        base.move_to_element_and_click(driver, self.type_key_list)

    def insert_input_select_file(self, driver, value):
        base.get_web_element(driver, self.input_select_file).send_keys(value)

    def insert_input_passw(self, driver, value):
        base.get_web_elements(driver, self.input_passw)[1].send_keys(value)

    def click_btn_load(self, driver):
        base.move_to_element_and_click(driver, self.btn_load)
