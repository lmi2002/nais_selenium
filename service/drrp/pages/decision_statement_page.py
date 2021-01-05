from helpers import base
from service.drrp import list_text_line
from service.drrp.locators.common_locator import DrrpCommonLocator
from service.drrp.locators.decision_statement_locator import DrrpDecisionStatementLocator
from settings.setting_data_info import data_info


class DrrpDecisionStatementPage(DrrpDecisionStatementLocator, DrrpCommonLocator):

    def click_decision_type(self, driver):
        base.move_to_element_and_click(driver, self.decision_type)

    def select_decision_type_list(self, driver):
        base.move_to_element_and_click(driver, self.decision_type_list)

    def insert_value_decision_addition_subtype(self, driver):
        base.get_web_element(driver, self.decision_addition_subtype).send_keys(
            data_info['decision_statement']['decision_addition_subtype'])

    def insert_value_decision_part_size(self, driver):
        base.get_web_element(driver, self.decision_part_size).send_keys(
            data_info['decision_statement']['decision_part_size'])

    def insert_value_decision_additional_info(self, driver):
        base.get_web_element(driver, self.decision_additional_info).send_keys(
            data_info['decision_statement']['decision_additional_info'])

    def click_decision_btn_registration(self, driver):
        base.move_to_element_and_click(driver, self.btn_registretion)

    def get_text_decision_block_info(self, driver):
        return base.get_element_locator(driver, self.decision_block_info).text
