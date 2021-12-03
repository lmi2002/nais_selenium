from helpers import base
from service.iit.locators.iit_locator import IitLocator


class IitPage(IitLocator):
    def insert_value_website_url(self, driver, value):
        base.get_web_element(driver, self.website_url).send_keys(value)

    def click_btn_add(self, driver):
        base.click(driver, self.btn_add)

    def click_btn_save(self, driver):
        base.click(driver, self.btn_save)

    def click_btn_set(self, driver):
        base.click(driver, self.btn_set)

    def click_alert(self, driver):
        alert = base.get_alert(driver)
        alert.dismiss()
