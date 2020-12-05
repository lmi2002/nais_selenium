from service.drrp.methods.common_method import DrrpCommonMethod
from service.drrp.pages.statement_page import DrrpStatementPage
from settings.setting_data_info import data_info


class DrrpBlockStatement(DrrpStatementPage, DrrpCommonMethod):
    def fill_block_statement(self, driver):
        self.insert_value_statement_num(driver, data_info['statement']['statement_num'])
        self.insert_value_statement_date(driver, data_info['statement']['statement_date'])
        self.click_statement_term_review(driver)
        self.click_statement_term_review_list(driver)
        self.click_statement_receive_type(driver)
        self.click_statement_receive_type_list(driver)
        self.insert_value_addition_of_statement(driver, data_info['statement']['addition_of_statement'])
