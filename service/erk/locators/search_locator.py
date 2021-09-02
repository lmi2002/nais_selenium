from selenium.webdriver.common.by import By


class ErkSearchCompanyLocator:
    form_search_company = (By.CLASS_NAME, 'x-accordion-item')
    field_name_company = (By.CSS_SELECTOR, 'textarea[name="reason"]')