from selenium.webdriver.common.by import By


class CommonLocator:
    btn_add = (By.XPATH, '//span[text()="Додати"]/..')
    btn_OK = (By.XPATH, '//span[text()="ОК"]/..')
    btn_plus = (By.XPATH, '//span[text()=""]/..')
    btn_registretion = (By.XPATH, '//span[text()="Зареєструвати"]/..')
    btn_sing = (By.XPATH, '//span[text()="Підписати ЕЦП"]/..')
