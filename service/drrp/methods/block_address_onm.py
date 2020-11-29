import time

from service.drrp.methods.common_method import DrrpCommonMethod
from service.drrp.pages.statement_page import DrrpStatementPage
from settings.setting_person import info


class BlockAddressOnm(DrrpStatementPage, DrrpCommonMethod):

    def fill_block_address_onm(self, driver):
        self.click_block_onm_btn_add(driver)
        self.click_block_add_address_onm(driver)
        self.insert_value_address_onm_locality(driver, info['address_onm']['address_onm_locality'])
        self.select_address_onm_locality_list(driver)
        self.click_address_onm_street(driver)
        time.sleep(2)
        self.insert_value_address_onm_street(driver, info['address_onm']['address_onm_street'])
        self.select_address_onm_street_list(driver)
        self.insert_value_house_type(driver, info['address_onm']['house_type'])
        self.select_house_type_list(driver)
        self.insert_value_house_num(driver, info['address_onm']['house_num'])
        self.insert_value_building_type(driver, info['address_onm']['building_type'])
        self.select_building_type_list(driver)
        self.insert_value_building_num(driver, info['address_onm']['building_num'])
        self.insert_value_object_num_type(driver, info['address_onm']['object_num_type'])
        self.select_object_num_type_list(driver)
        self.insert_value_object_num(driver, info['address_onm']['object_num'])
        self.insert_value_addition_of_address_onm(driver, info['address_onm']['addition_of_address_onm'])
        self.click_block_address_onm_btn_OK(driver)
