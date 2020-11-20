from selenium.webdriver.common.by import By


class AuthLocator:

    user = (By.TAG_NAME, 'input')
    passw = (By.TAG_NAME, 'input')
    entry = (By.XPATH, '//span[text()="Увійти"]/..')
