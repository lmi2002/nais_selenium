from selenium.webdriver.common.by import By

from settings import setting_erk_data_info


class ErkCompanyLocator:
    operation_company_short_name = (By.XPATH, '//span[text()="Скорочення"]/..')
    operation_company_ext_gen = (By.CSS_SELECTOR, 'td[id*="ext-gen"]')
    operation_company_ubcombobox = (By.CSS_SELECTOR, 'input[id*=ubcombobox]')
    operation_category_name = (
        By.XPATH, '//li[text()="{operation_company_category}"]'.format(
            operation_company_category=setting_erk_data_info.company["operation_company_category"]))
    operation_company_name = (By.CSS_SELECTOR, 'input[name="name"]')
    operation_company_shortname = (By.CSS_SELECTOR, 'input[name="shortname"]')
    operation_company_phone = (By.CSS_SELECTOR, 'input[name="phone"]')
    operation_company_edrpou = (By.CSS_SELECTOR, 'input[name="edrpou"]')
    operation_company_asfo = (By.CSS_SELECTOR, 'input[name="asfoID"]')
    operation_company_post_index = (By.CSS_SELECTOR, 'input[name="postIndex"]')
    operation_company_post_street = (By.CSS_SELECTOR, 'input[name="postAdrBody"]')
    operation_company_post_address_index = (By.CSS_SELECTOR, 'input[name="indexCode"]')
    operation_company_address_street = (By.CSS_SELECTOR, 'input[name="adrBody"]')
    operation_company_locality = (By.XPATH, '//li[text()="{operation_company_locality}"]'.format(
        operation_company_locality=setting_erk_data_info.company["operation_company_locality"]))
    operation_company_region = (By.XPATH, '//li[text()="{operation_company_region}"]'.format(
        operation_company_region=setting_erk_data_info.company["operation_company_region"]))
