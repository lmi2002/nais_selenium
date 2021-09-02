from selenium.webdriver.common.by import By


class ErkCommonLocator:
    btn_search = (By.XPATH, '//span[text()="Пошук"]/..')
    tr_ubtableview = (By.CSS_SELECTOR, 'tr[id*="ubtableview"]')
    btn_clear = (By.XPATH, '//span[text()="Очистити"]/..')
    btn_menu_add = (By.CSS_SELECTOR, '.x-btn-icon-el.u-icon-add')