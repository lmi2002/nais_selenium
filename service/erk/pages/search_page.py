from helpers import base
from service.erk.locators.search_company_locator import ErkSearchCompanyLocator


class ErkSearchCompanyPage(ErkSearchCompanyLocator):

    def visible_form_search_company(self, driver):
        return base.get_web_elements(driver, self.form_search_company)[1]