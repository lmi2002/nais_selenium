from selenium.webdriver.common.by import By


class DrrpPerformActionMenuLocator:
    button_perform_action = (By.XPATH, '//span[text()="Виконати дію"]')
    menu_edit = (By.XPATH, '//span[text()="Редагувати"]')