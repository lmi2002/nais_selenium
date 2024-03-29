from selenium.webdriver.common.keys import Keys

from helpers import base
from service.auth.locators.auth_locator import AuthLocator
from settings.setting_allure import SettingAllure


class AuthPage(AuthLocator):

    def get_user(self, driver):
        return base.get_web_element(driver, self.user)

    def check_visible_field_user(self, driver):
        base.get_visible_element(driver, self.user)

    def get_passw(self, driver):
        return base.get_web_elements(driver, self.passw)[1]

    def get_entry(self, driver, index=None):
        if index is None:
            return base.get_web_element(driver, self.entry)
        else:
            return base.get_web_elements(driver, self.entry)[index]

    def insert_input_select_file(self, driver, value, index=None):
        if index is None:
            base.get_web_element(driver, self.input_select_file).send_keys(value)
        else:
            base.get_web_elements(driver, self.input_select_file)[index].send_keys(value)

    def insert_input_passw(self, driver, value):
        base.get_web_elements(driver, self.input_passw)[1].send_keys(value)

    def click_btn_load(self, driver):
        base.move_to_element_and_click(driver, self.btn_load)

    def check_invisible_button_is_disabled(self, driver):
        base.check_invisible_element(driver, self.button_is_disabled)

    def visible_v_modal(self, driver):
        base.get_visible_element(driver, self.v_modal)

    def visible_div_is_focus(self, driver):
        base.get_visible_element(driver, self.div_is_focus)

    @staticmethod
    def set_attr_hover_first_element(driver, num):
        driver.execute_script(
            "document.querySelectorAll('div[x-placement=\"bottom-start\"] li span')[{num}].setAttribute('class', 'hover')".format(
                num=num))

    @staticmethod
    def set_attr_selected_first_element(driver, num):
        driver.execute_script(
            "document.querySelectorAll('div[x-placement=\"bottom-start\"] li span')[{num}].setAttribute('class', 'selected')".format(
                num=num))

    @staticmethod
    def select_type_key_list_first_element(driver, num):
        driver.execute_script(
            "document.querySelectorAll('div[x-placement=\"bottom-start\"] li span')[{num}].click()".format(
                num=num))

    def visible_el_popup_parent_hidden(self, driver):
        base.get_visible_element(driver, self.el_popup_parent_hidden)

    def click_input_type_key(self, driver):
        driver.execute_script("document.getElementsByTagName('input')[2].click()")

    def check_text_in_ub_dialog_break_word(self, driver):
        return base.get_web_element(driver, self.ub_dialog_break_word).text

    def check_text_required_field_login(self, driver):
        base.check_text_present_in_element(driver, self.el_form_item_error, "Це поле є обов’язковим для заповнення")

    def check_text_required_field_passw(self, driver):
        base.get_element_containing_text(driver, "Вкажіть поточний пароль")

    def get_attr_btn_load(self, driver):
        return base.get_web_element(driver, self.btn_load).get_attribute('disabled')

    def click_field_select_device(self, driver):
        driver.execute_script("document.getElementsByTagName('input')[3].click()")

    def visible_el_select_dropdown_empty(self, driver):
        base.get_visible_element(driver, self.el_select_dropdown_empty)

    def check_text_message_invalid_passw_of_key(self, driver):
        base.check_text_present_in_element(driver, self.ub_dialog_break_word,
                                           "Виникла помилка при відкритті особистого ключа (невірний пароль чи ключ пошкоджений)")

    def visible_entry(self, driver):
        base.get_visible_element(driver, self.entry)

    def click_btn_OK_install(self, driver):
        base.move_to_element_and_click(driver, self.btn_OK_install)

    def visible_form_select_certificate(self, driver):
        base.get_visible_element(driver, self.form_select_certificate)

    def click_input_selected_acsk(self, driver):
        base.move_to_element_and_click(driver, self.input_selected_acsk)

    def click_select_dropdown(self, driver):
        driver.execute_script("document.querySelectorAll('.el-scrollbar__view.el-select-dropdown__list')[1] \
        .querySelectorAll('.el-select-dropdown__item')[1].click()")

    def visible_form_select_certificate_file(self, driver):
        base.get_visible_element(driver, self.form_select_certificate_file)

    def check_text_message_session_mode_singleton(self, driver, text):
        base.check_text_present_in_element(driver, self.ub_dialog_break_word, text)

    def clear_text_user_field(self, driver):
        base.get_web_element(driver, self.user).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
