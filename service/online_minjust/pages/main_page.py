import datetime
import time

from exception import TextNotFoundException
from helpers import base
from service.online_minjust.locators.main_locator import OnlineMinjustMainLocator
from service.online_minjust.methods.auth_method import OnlineMinjustAuthMethod
from settings.setting_project import project_rule, PROJECT, RULE
from settings.setting_online_minjust_data_info import onm


class OnlineMinjustMainPage(OnlineMinjustMainLocator):

    def click_btn_pass_to_rrp(self, driver):
        base.move_to_element_and_click(driver, self.btn_pass_to_rrp, index=1)

    def click_btn_pass_to_auth_page(self, driver):
        base.move_to_element_and_click(driver, self.btn_pass_to_auth_page)

    def select_csk(self, driver, index):
        base.select_index(driver, self.cas_servers_select, index)

    def insert_input_select_file(self, driver):
        base.get_web_element(driver, self.pkey_file_input).send_keys(project_rule[PROJECT][RULE]['key_path'])

    def insert_input_pkey_password(self, driver):
        base.get_web_element(driver, self.pkey_password).send_keys(project_rule[PROJECT][RULE]['passw_key'])

    def click_submit_ecp(self, driver):
        base.move_to_element_and_click(driver, self.submit_ecp)

    def click_btn_service(self, driver):
        base.move_to_element_and_click(driver, self.btn_service)

    def get_text_first_number(self, driver):
        return base.get_web_element(driver, self.gradea_even_td).text

    def get_first_number_payment(self, driver):
        return base.get_web_element(driver, self.gradea_even_td_a)

    def click_first_number_payment(self, driver):
        self.get_first_number_payment(driver).click()

    def click_checkbox_address(self, driver):
        base.move_to_element_and_click(driver, self.extract_option)

    def click_checkbox_onm(self, driver):
        base.move_to_element_and_click(driver, self.extract_option, index=1)

    def click_btn_next(self, driver):
        base.move_to_element_and_click(driver, self.btn_next)

    def insert_input_field_onm(self, driver):
        base.get_web_element(driver, self.field_onm).send_keys(onm)

    def check_visible_form_group_title(self, driver):
        base.get_visible_element(driver, self.form_group_title)

    def check_visible_new_first_number(self, driver, number):
        timeout = 120
        poll = 0.5
        end_time = time.time() + timeout
        while True:
            new_number = self.get_text_first_number(driver)
            if (new_number != number):
                return True
            time.sleep(poll)
            if time.time() > end_time:
                break
        base.ssc.create_screenshot(driver)
        raise ('Not found new ' + number)

    def check_visible_new_first_number_payment(self, driver, number):
        timeout = 120
        poll = 0.5
        end_time = time.time() + timeout
        while True:
            href = self.get_first_number_payment(driver).get_attribute('href')
            if (number in href):
                return True
            time.sleep(poll)
            if time.time() > end_time:
                break
        base.ssc.create_screenshot(driver)
        raise ('Not found new btn payment')

    def click_btn_payment_type_portmone(self, driver):
        base.move_to_element_and_click(driver, self.btn_payment_type_portmone)

    def check_text_name(self, driver, text):
        base.get_element_present_text(driver, text)

    def check_text_id(self, driver, text):
        base.get_element_present_text(driver, text)

    def check_text_cost(self, driver, text):
        base.get_element_present_text(driver, text)

    def check_text_data(self, driver):
        base.get_elements_containing_text(driver, datetime.datetime.now().strftime("%d.%m.%Y"))

    def click_btn_payment_confirm(self, driver):
        base.move_to_element_and_click(driver, self.btn_payment_confirm)

    def switch_to_tab_portmone(self, driver):
        driver.switch_to.window(driver.window_handles[1])

    def switch_to_tab_online_minjust(self, driver):
        driver.switch_to.window(driver.window_handles[0])

    def close_tab_portmone(self, driver):
        driver.close()

    def check_visible_new_first_loaded_payment(self, driver, number):
        path = OnlineMinjustAuthMethod().host + 'managers/services/get-extract/file/' + number
        timeout = 360
        poll = 20
        end_time = time.time() + timeout
        while True:
            base.refresh_page(driver)
            href = self.get_first_number_payment(driver).get_attribute('href')
            if (path == href):
                return True
            time.sleep(poll)
            if time.time() > end_time:
                break
        base.ssc.create_screenshot(driver)
        raise ('Not found btn loaded ' + number)

    def click_new_first_loaded_payment(self, driver):
        base.move_to_element_and_click(driver, self.btn_payment_confirm)
