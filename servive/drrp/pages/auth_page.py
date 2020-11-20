from servive.drrp.locators.auth_locator import AuthLocator
from servive.drrp.pages import base


class AuthPage(AuthLocator):

    def get_user(self, driver):
        return base.get_web_element(driver, self.user)

    def get_passw(self, driver):
        return base.get_web_elements(driver, self.passw)[1]

    def get_entry(self, driver):
        return base.get_web_element(driver, self.entry)
