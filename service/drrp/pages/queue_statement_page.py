#!/usr/bin/env python
# -*- coding: utf-8 -*-

from helpers import base
from service.drrp.locators.queue_statement_locator import DrrpQueueStatementLocator


class DrrpQueueStatementPage(DrrpQueueStatementLocator):

    def click_header_trigger(self, driver):
        elem = base.get_web_element(driver, self.col_account_number)
        driver.execute_script(
            "arguments[0].setAttribute('class', 'x-column-header-over');", elem)
        base.move_to_element_and_click(driver, self.x_column_header_trigger)

    def click_sort_desc(self, driver):
        base.move_to_element_and_click(driver, self.sort_desc)

    def check_visible_result_el_st(self, driver):
        base.get_visible_element(driver, self.result_el_st)



