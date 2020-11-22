
from helpers import base
from service.drrp.locators.auth_locator import DrrpAuthLocator


class DrrpAuthPage(DrrpAuthLocator):

    def get_user(self, driver):
        return base.get_web_element(driver, self.user)

    def get_passw(self, driver):
        return base.get_web_elements(driver, self.passw)[1]

    def get_entry(self, driver):
        return base.get_web_element(driver, self.entry)
