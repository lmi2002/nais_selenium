from helpers import base
from service.erk.locators.common_locator import ErkCommonLocator


class ErkCommonPage(ErkCommonLocator):
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
