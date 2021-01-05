import time

from helpers import base
from service.drrp.locators.search_statement_locator import DrrpSearchStatementLocator


class DrrpSearchStatementPage(DrrpSearchStatementLocator):

    def click_sub_menu_search_statement(self, driver):
        time.sleep(0.5)
        base.move_to_element_and_click(driver, self.sub_menu_search_statement)

    def insert_value_num_statement(self, driver, value):
        base.get_web_element(driver, self.num_statement).send_keys(value)

