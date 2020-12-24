from helpers import base
from service.drrp.locators.decision_statement_locator import DrrpDecisionStatementLocator


class DrrpDecisionStatementPage(DrrpDecisionStatementLocator):

    def click_decision_type(self, driver):
        base.move_to_element_and_click(driver, self.decision_type)

    def insert_value_decision_addition_subtype(self, driver, value):
        base.get_web_element(driver, self.decision_addition_subtype).send_keys(value)

    def insert_value_decision_additional_info(self, driver, value):
        base.get_web_element(driver, self.decision_additional_info).send_keys(value)

    def select_decision_type_list(self, driver):
        base.move_to_element_and_click(driver, self.decision_type_list)
