from service.drrp.methods.common_method import DrrpCommonMethod
from service.drrp.pages.statement_page import DrrpStatementPage
from settings.setting_data_info import data_info

class DrrpBlockCommonInfo(DrrpStatementPage, DrrpCommonMethod):

    def fill_block_common_info(self, driver, statement):

        if statement == 'relinquishment_of_property':
            self.click_type_ownership(driver)
            self.select_type_ownership_list(driver)
            self.insert_value_num_ownership(driver, data_info['common_info']['num_ownership'])
            self.click_type_another_property_right(driver)
            self.select_type_another_property_right_list(driver)
        else:
            self.click_block_common_info(driver)
            self.click_kind_registration(driver)
            self.select_kind_registration_list(driver)
            self.insert_value_num_ownership(driver, data_info['common_info']['num_ownership'])

        if statement == 'ownership':
            self.click_form_ownership(driver)
            self.select_form_ownership_list(driver)
            self.click_kind_common_ownership(driver)
            self.select_kind_common_ownership_list(driver)
        elif statement == 'irp':
            self.click_field_type_irp(driver)
            self.select_field_type_irp_list(driver)
            self.insert_value_addition_type_irp(driver, data_info['common_info']['addition_of_type'])
        elif statement == 'encumbrances':
            self.click_field_type_encumbrances(driver)
            self.select_type_encumbrances_list(driver)


