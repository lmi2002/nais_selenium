from selenium.webdriver.common.by import By


class DrrpAuthLocator:

    user = (By.TAG_NAME, 'input')
    passw = (By.TAG_NAME, 'input')
    entry = (By.XPATH, '//span[text()="Продовжити"]/..')
    client_login_form = (By.ID, 'extClientLoginForm-body')
