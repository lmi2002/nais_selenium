from selenium.webdriver.common.by import By


class ErkCommonLocator:
    btn_search = (By.XPATH, '//span[text()="Пошук"]/..')
    tr_ubtableview = (By.CSS_SELECTOR, 'tr[id*="ubtableview"]')
    btn_clear = (By.XPATH, '//span[text()="Очистити"]/..')
    btn_menu_add = (By.CSS_SELECTOR, '.x-btn-icon-el.u-icon-add')
    btn_save = (By.CSS_SELECTOR, 'a[data-qtip="Зберегти"]')
    btn_admit_employee = (By.CSS_SELECTOR, 'a[data-qtip="Застосувати"]')
    btn_loupe = (By.CLASS_NAME, 'u-icon-search')
    mask_msg = (By.CLASS_NAME, 'x-mask-msg')
    btn_filter = (By.CLASS_NAME, 'u-icon-filter')
    x_menu = (By.CLASS_NAME, 'x-menu')
    search_param = (By.CSS_SELECTOR, '.x-box-target .x-menu-item')
    input_textfield = (By.CSS_SELECTOR, 'input[id*="textfield"]')
    btn_change_company = (By.CSS_SELECTOR, 'a[data-qtip="Перехід до іншої організації"]')
    li = (By.TAG_NAME, 'li')
