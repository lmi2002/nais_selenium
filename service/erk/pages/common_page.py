import time

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

    def click_btn_loupe(self, driver):
        base.move_to_element_and_click(driver, self.btn_loupe)

    # def check_invisible_loaded_page(self, driver):
    #     timeout = base.timeout
    #     poll = 0.5
    #     end_time = time.time() + timeout
    #     time.sleep(1)
    #     while True:
    #         value = driver.execute_script(
    #             "return document.querySelector('.x-mask-msg').style.getPropertyValue('display')")
    #         if value == 'none':
    #             return True
    #         time.sleep(poll)
    #         if time.time() > end_time:
    #             break
    #     base.ssc.create_screenshot(driver)
    #     raise VisibleLoadedPageException()

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
