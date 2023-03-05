import datetime
import time

from exception import NotFoundElementException, TextNotFoundException
from helpers import base
from service.online_minjust.locators.main_locator import OnlineMinjustMainLocator
from service.online_minjust.methods.auth_method import OnlineMinjustAuthMethod
from settings.setting_project import project_rule, PROJECT, RULE


class OnlineMinjustMainPage(OnlineMinjustMainLocator):

    def click_btn_pass_to_rrp(self, driver):
        base.move_to_element_and_click(driver, self.btn_pass_to_rrp, index=1)

    def click_btn_pass_to_info_rrp(self, driver):
        base.move_to_element_and_click(driver, self.btn_pass_to_info_rrp)

    def click_btn_pass_to_zaborona_rrp(self, driver):
        base.move_to_element_and_click(driver, self.btn_pass_to_zaborona_rrp)

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

    def get_first_number_payment(self, driver, index=None):
        if index is None:
            return base.get_web_element(driver, self.gradea_even_td_a)
        else:
            return base.get_web_elements(driver, self.gradea_even_td_a)[index]

    def click_first_number_payment(self, driver, number):
        elem = self.check_visible_new_first_number_payment(driver, number)
        elem.click()

    def click_checkbox_address(self, driver):
        base.move_to_element_and_click(driver, self.extract_option)

    def click_checkbox_onm(self, driver):
        base.move_to_element_and_click(driver, self.extract_option, index=1)

    def click_checkbox_cad_num(self, driver):
        base.move_to_element_and_click(driver, self.extract_option, index=2)

    def click_btn_next(self, driver):
        base.move_to_element_and_click(driver, self.btn_next)

    def click_btn_get_obj(self, driver):
        base.move_to_element_and_click(driver, self.btn_next)

    def insert_input_field_onm(self, driver, value):
        base.get_web_element(driver, self.field_onm).send_keys(value)

    def insert_input_field_cad_num(self, driver, value):
        base.get_web_element(driver, self.field_cad_num).send_keys(value)

    def check_visible_form_group_title(self, driver):
        base.get_visible_element(driver, self.form_group_title)

    def check_visible_new_first_number(self, driver, number):
        timeout = 120
        poll = 0.5
        end_time = time.time() + timeout
        while True:
            base.refresh_page(driver)
            new_number = self.get_text_first_number(driver)
            if (new_number != number):
                # print(new_number)
                return new_number
            time.sleep(poll)
            if time.time() > end_time:
                break
        base.ssc.create_screenshot(driver)
        raise NotFoundElementException('new ' + number)

    def check_visible_new_first_number_payment(self, driver, number):
        timeout = 300
        poll = 0.5
        end_time = time.time() + timeout
        while True:
            base.refresh_page(driver)
            elem = self.get_first_number_payment(driver)
            href = elem.get_attribute('href')
            if number in href:
                # print(number)
                return elem
            time.sleep(poll)
            if time.time() > end_time:
                break
        base.ssc.create_screenshot(driver)
        raise NotFoundElementException('btn new payment ' + number)

    def check_visible_new_first_number_select_obj(self, driver, number):
        path = OnlineMinjustAuthMethod().host + 'managers/services/extract#collapse' + number
        timeout = 120
        poll = 0.5
        end_time = time.time() + timeout
        while True:
            base.refresh_page(driver)
            elem = self.get_first_number_payment(driver)
            href = elem.get_attribute('href')
            if path == href:
                return elem
            time.sleep(poll)
            if time.time() > end_time:
                break
        base.ssc.create_screenshot(driver)
        raise NotFoundElementException('btn select obj ' + number)

    def click_new_first_number_select_obj(self, driver, number):
        elem = self.check_visible_new_first_number_select_obj(driver, number)
        elem.click()

    def check_visible_new_first_number_select_all_obj(self, driver, number):
        path = OnlineMinjustAuthMethod().host + 'managers/services/extract/p/' + number
        # print('path: ' + path)
        timeout = 120
        poll = 0.5
        end_time = time.time() + timeout
        while True:
            base.refresh_page(driver)
            elem = self.get_first_number_payment(driver, index=1)
            href = elem.get_attribute('href')
            # print('href: ' + href)
            if path in href:
                return elem
            time.sleep(poll)
            if time.time() > end_time:
                break
        base.ssc.create_screenshot(driver)
        raise NotFoundElementException('btn select all obj ' + number)

    def click_new_first_number_select_all_obj(self, driver, number):
        elem = self.check_visible_new_first_number_select_all_obj(driver, number)
        elem.click()

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
        base.switch_to_window(driver, 1)

    def switch_to_tab_online_minjust(self, driver):
        base.switch_to_window(driver, 0)

    def close_tab_portmone(self, driver):
        driver.close()

    def check_visible_new_first_loaded_payment(self, driver, number):
        path = OnlineMinjustAuthMethod().host + 'managers/services/get-extract/file/' + number
        timeout = 360
        poll = 20
        end_time = time.time() + timeout
        while True:
            base.refresh_page(driver)
            elem = self.get_first_number_payment(driver)
            href = elem.get_attribute('href')
            if path == href:
                return elem
            time.sleep(poll)
            if time.time() > end_time:
                break
        base.ssc.create_screenshot(driver)
        raise NotFoundElementException('btn loaded ' + number)

    def click_new_first_loaded_payment(self, driver, number):
        elem = self.check_visible_new_first_loaded_payment(driver, number)
        elem.click()

    def get_elems_in_dropdown_list(self, driver):
        return base.get_web_elements(driver, self.dropdown_list)

    def click_field_region(self, driver):
        base.move_to_element_and_click(driver, self.select2_selection_single)

    def select_region(self, driver, index):
        base.move_to_element_and_click(driver, self.dropdown_list, index=index)

    def click_field_city(self, driver, index):
        base.move_to_element_and_click(driver, self.select2_selection_single, index=index)

    def select_city(self, driver, index):
        base.move_to_element_and_click(driver, self.dropdown_list, index=index)

    def click_field_street(self, driver, index):
        base.move_to_element_and_click(driver, self.select2_selection_single, index=index)

    def select_street(self, driver):
        base.move_to_element_and_click(driver, self.select_street_dropdown)

    def select_house_type(self, driver, index):
        base.select_index(driver, self.house_type, index)

    def select_object_num_type(self, driver, index):
        base.select_index(driver, self.object_num_type, index)

    def insert_input_field_num_house(self, driver, value):
        base.get_web_element(driver, self.input_field_num_house).send_keys(value)

    def insert_input_field_num_appart(self, driver, value):
        base.get_web_element(driver, self.input_field_num_appart).send_keys(value)

    def click_checkbox_persone(self, driver):
        base.move_to_element_and_click(driver, self.extract_option, index=3)

    def click_checkbox_company(self, driver):
        base.move_to_element_and_click(driver, self.extract_option, index=4)

    def insert_input_field_persone_code(self, driver, value):
        base.get_web_element(driver, self.input_field_persone_code).send_keys(value)

    def insert_input_field_persone_name(self, driver, value):
        base.get_web_element(driver, self.input_field_persone_name).send_keys(value)

    def click_href_onm(self, driver, prop=None):
        elems = base.get_web_elements(driver, self.collapse_in_div_p)
        for elem in elems:
            if prop in elem.text:
                a = elem.find_element_by_css_selector('a')
                a.click()
                return True

    def click_href_onm_zaborona(self, driver, prop=None):
        elems = base.get_web_elements(driver, self.collapse_in_div_p)
        for elem in elems:
            if prop in elem.text:
                span = elem.find_element_by_css_selector('span')
                span.click()
                return True

    def check_visible_new_first_number_select_obj_zaborona(self, driver, number):
        path = OnlineMinjustAuthMethod().host + 'managers/services/zaborona#collapse' + number
        timeout = 120
        poll = 0.5
        end_time = time.time() + timeout
        # print(path)
        while True:
            base.refresh_page(driver)
            elem = self.get_first_number_payment(driver)
            href = elem.get_attribute('href')
            if path == href:
                return elem
            time.sleep(poll)
            if time.time() > end_time:
                break
        base.ssc.create_screenshot(driver)
        raise NotFoundElementException('btn select obj ' + number)

    def click_new_first_number_select_obj_zaborona(self, driver, number):
        elem = self.check_visible_new_first_number_select_obj_zaborona(driver, number)
        elem.click()

    def switch_to_tab(self, driver, index=None):
        base.switch_to_window(driver, index)

    def create_new_tab(self, driver):
        base.create_window(driver)

    def check_invisible_modal_content(self, driver):
        base.check_invisible_element(driver, self.modal_content)


    def check_visible_text_actions_text_center(self, driver, text):
        base.timeout = 2
        item = self.actions_text_center
        timeout = 300
        poll = 1
        end_time = time.time() + timeout
        while True:
            base.refresh_page(driver)
            base.get_web_element(driver, item)
            if base.check_text_present_in_element_b(driver, item, text):
                return True
            time.sleep(poll)
            if time.time() > end_time:
                break
        base.ssc.create_screenshot(driver)
        raise TextNotFoundException(item, text)
