import time

from helpers import func
from service.drrp.methods.common_method import DrrpCommonMethod
from service.drrp.pages.statement_page import DrrpStatementPage
from settings.setting_data_info import data_info


class DrrpBlockPayment(DrrpStatementPage, DrrpCommonMethod):

    def fill_block_payment(self, driver):
        self.click_payment_block(driver)
        self.click_block_payment_btn_plus(driver)
        self.click_block_payment_btn_plus(driver)
        self.click_payment_type(driver)
        self.click_payment_type_list(driver)
        self.insert_value_payment_num(driver, data_info['payment']['payment_num'])
        self.insert_value_payment_date(driver, data_info['payment']['payment_date'])
        self.insert_value_payment_summ(driver, data_info['payment']['payment_summ'])
        self.insert_value_org_name(driver, "ощадбанк_{num}".format(num=str(func.get_generate_num())))
        self.click_btn_admit(driver)
