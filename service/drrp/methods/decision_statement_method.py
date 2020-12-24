from service.drrp.pages.decision_statement_page import DrrpDecisionStatementPage
from settings.setting_data_info import data_info


class DrrpDecisionStatementMethod(DrrpDecisionStatementPage):

    def fill_decision(self, driver):
        self.click_decision_type(driver)
        self.select_field_type_irp_list(driver)
        self.insert_value_decision_addition_subtype(driver,
                                                    data_info['decision_statement']['decision_addition_subtype'])
        self.insert_value_decision_additional_info(driver, data_info['decision_statement']['decision_additional_info'])

