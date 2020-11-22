import time

from service.drrp.pages.common_page import DrrpCommonPage


class DrrpCommonMethod(DrrpCommonPage):

    def clear_cash_in_local_store(self, driver):
        self.click_user_code(driver)
        self.move_user_menu_cash(driver)
        self.click_clear_local_store(driver)
        time.sleep(2)
        self.click_close_form(driver)

    def clear_cash_in_local_form(self, driver):
        self.click_user_code(driver)
        self.move_user_menu_cash(driver)
        self.click_clear_local_form(driver)
        time.sleep(2)
        self.click_close_form(driver)

