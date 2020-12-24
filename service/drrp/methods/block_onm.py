from service.drrp.methods.common_method import DrrpCommonMethod
from service.drrp.pages.statement_page import DrrpStatementPage
from settings.setting_data_info import data_info


class DrrpBlockOnm(DrrpStatementPage, DrrpCommonMethod):

    def fill_block_onm(self, driver, statement):
        self.click_block_onm(driver)
        self.click_block_onm_btn_add(driver)
        self.click_block_add_onm(driver)
        self.insert_value_block_onm_num_ownership(driver, data_info['onm']['onm_num_ownership'])
        self.click_type_onm(driver)
        self.select_type_onm_list(driver)
        self.insert_value_addition_of_type_onm(driver, data_info['onm']['addition_of_type_onm'])
        self.click_subtype_onm(driver)

        if statement == 'encumbrances':
            self.select_subtype_onm_list_encumbrances(driver)
        else:
            self.select_subtype_onm_list(driver)

        self.insert_value_addition_of_subtype_onm(driver, data_info['onm']['addition_of_subtype_onm'])
        self.insert_value_description_onm(driver, data_info['onm']['description_onm'])
        self.click_block_onm_btn_OK(driver)
