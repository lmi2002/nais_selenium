from service.drrp.pages.decision_statement_page import DrrpDecisionStatementPage


class DrrpDecisionStatementMethod(DrrpDecisionStatementPage):

    def fill_decision(self, driver):
        self.click_decision_type(driver)
        self.select_decision_type_list(driver)
        self.insert_value_decision_part_size(driver)
        self.insert_value_decision_addition_subtype(driver)
        self.insert_value_decision_additional_info(driver)

    def data_decision_block_info(self, driver):
        decision_info = []
        str_text = self.get_text_decision_block_info(driver)
        list_text = str_text.split("\n")

        for num, t in enumerate(list_text, start=1):
            if num == 4:
                decision_num = t
            elif num in (5, 8, 9, 11):
                decision_info.append(t)

        return [decision_num, decision_info]


