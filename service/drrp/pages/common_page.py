from service.drrp.locators.auth_locator import DrrpAuthLocator
from service.drrp.locators.common_locator import DrrpCommonLocator
from helpers import base


class DrrpCommonPage(DrrpAuthLocator, DrrpCommonLocator):

    def click_user_code(self, driver):
        base.move_to_element_and_click(driver, self.user_code)

    def click_user_exit(self, driver):
        base.move_to_element_and_click(driver, self.exit)

    def visible_client_login_form(self, driver):
        base.get_visible_element(driver, self.client_login_form)

    def move_user_menu_cash(self, driver):
        base.move_to_element(driver, self.user_menu_cash)

    def click_clear_local_store(self, driver):
        base.move_to_element_and_click(driver, self.clear_local_store)

    def click_close_form(self, driver):
        base.move_to_element_and_click(driver, self.close_form)

    def click_clear_local_form(self, driver):
        base.move_to_element_and_click(driver, self.clear_local_form)
