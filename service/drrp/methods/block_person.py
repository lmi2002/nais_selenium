from service.drrp.methods.common_method import DrrpCommonMethod
from service.drrp.pages.statement_page import DrrpStatementPage
from settings.setting_person import info


class DrrpBlockPerson(DrrpStatementPage, DrrpCommonMethod):

    def fill_block_person(self, driver):
        self.click_block_person_btn_add(driver)
        self.click_block_person_btn_add(driver)
        self.click_person_type(driver)
        self.click_person_rule(driver)
        self.click_person_rule_list(driver)
        self.insert_value_person_name(driver, info['person']['person_name'])
        self.insert_value_person_code(driver, info['person']['person_code'])
        self.insert_value_person_phone(driver, info['person']['person_phone'])
        self.insert_value_passport_series(driver, info['person']['passport_series'])
        self.insert_value_passport_date(driver, info['person']['passport_date'])
        self.insert_value_passport_publisher(driver, info['person']['passport_publisher'])
        self.insert_value_addition_of_person(driver, info['person']['addition_of_person'])
        self.click_block_person_btn_OK(driver)
