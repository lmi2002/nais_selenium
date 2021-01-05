from selenium.webdriver.common.by import By


class DrrpSearchStatementLocator:
    sub_menu_search_statement = (By.XPATH, '//span[text()="Пошук заяв"]')
    num_statement = (By.CSS_SELECTOR, 'input[name="regNum"]')
