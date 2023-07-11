import time

from helpers import base
from service.erc.locators.common_locator import ErcCommonLocator


class ErcCommonPage(ErcCommonLocator):
    def click_btn_search(self, driver):
        base.move_to_element_and_click(driver, self.btn_search, index=1)

    def count_elem_tr_ubtableview(self, driver):
        return len(base.get_web_elements(driver, self.tr_ubtableview))

    def click_btn_clear(self, driver):
        base.move_to_element_and_click(driver, self.btn_clear)

    def check_invisible_tr_ubtableview(self, driver):
        base.check_invisible_element(driver, self.tr_ubtableview)

    def click_btn_menu_add(self, driver):
        base.move_to_element_and_click(driver, self.btn_menu_add)

    def click_btn_loupe(self, driver):
        base.move_to_element_and_click(driver, self.btn_loupe)

    def click_btn_filter(self, driver):
        base.move_to_element_and_click(driver, self.btn_filter)

    def visible_x_menu(self, driver):
        base.get_visible_element(driver, self.x_menu)

    def select_search_param(self, driver, index=None):
        base.move_to_element_and_click(driver, self.search_param, index)

    def insert_input_textfield(self, driver, value):
        base.get_web_element(driver, self.input_textfield).send_keys(value)

    def click_btn_change_company(self, driver):
        base.move_to_element_and_click(driver, self.btn_change_company)
