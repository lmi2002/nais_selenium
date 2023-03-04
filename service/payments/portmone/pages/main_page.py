import datetime
import time

from helpers import base
from service.online_minjust.methods.auth_method import OnlineMinjustAuthMethod
from service.payments.portmone.locators.main_locator import PortmoneMainLocator


class PortmoneMainPage(PortmoneMainLocator):

    def insert_field_number_card(self, driver):
        base.get_web_element(driver, self.field_number_card).send_keys("4444333322221111")

    def insert_field_exp_date_card(self, driver):
        base.get_web_element(driver, self.field_exp_date_card).send_keys(datetime.datetime.now().strftime("%m-%yy"))

    def insert_field_cvv2_card(self, driver):
        base.get_web_element(driver, self.field_cvv2_card).send_keys('111')

    def insert_field_email(self, driver):
        base.get_web_element(driver, self.field_email).send_keys('1@ukr.net')

    def click_btn_payment(self, driver):
        base.move_to_element_and_click(driver, self.btn_payment)

    def click_btn_payment_confirm(self, driver):
        base.move_to_element_and_click(driver, self.btn_payment_confirm)

    def check_current_url(self, driver, number):
        url = OnlineMinjustAuthMethod.host + 'managers/services/extract/id/' + number
        time.sleep(2)
        assert base.get_current_url(driver) == url

    def check_text_present_in_total_amount(self, driver, text):
        base.check_text_present_in_element(driver, self.total_amount, text)
