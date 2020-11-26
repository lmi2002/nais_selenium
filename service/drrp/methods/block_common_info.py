from service.drrp.methods.common_method import DrrpCommonMethod
from service.drrp.pages.statement_page import DrrpStatementPage
from settings.setting_person import info


class DrrpBlockCommonInfo(DrrpStatementPage, DrrpCommonMethod):

    def fill_block_common_info(self, driver, elem):
        self.click_block_common_info(driver)
        self.click_kind_registration(driver)
        self.select_kind_registration_list(driver)
        self.insert_value_num_ownership(driver, info['common info']['num_ownership'])
        if elem == 'ownership':
            self.click_form_ownership(driver)
            self.select_form_ownership_list(driver)
            self.click_kind_common_ownership(driver)
            self.select_kind_common_ownership_list(driver)
        elif elem == 'irp':
            self.click_field_type_irp(driver)
            self.select_field_type_irp_list(driver)
            self.insert_value_addition_type_irp(driver, info['common info']['addition_of_type'])
