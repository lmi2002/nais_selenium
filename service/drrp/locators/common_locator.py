from selenium.webdriver.common.by import By

from settings.setting_rule_user import users, project, rule


class DrrpCommonLocator:
    btn_add = (By.XPATH, '//span[text()="Додати"]/..')
    btn_OK = (By.XPATH, '//span[text()="ОК"]/..')
    btn_plus = (By.XPATH, '//span[text()=""]/..')
    btn_registretion = (By.XPATH, '//span[text()="Зареєструвати"]/..')
    btn_sing = (By.XPATH, '//span[text()="Підписати ЕЦП"]/..')
    user_code = (By.XPATH, '//span[text()="{user_code}"]/..'.format(
        user_code=users[project][rule]['login']))
    exit = (By.XPATH, '//span[text()="Вихід"]/..')
    user_menu_cash = (By.XPATH, '//span[text()="Дані, що збережено"]/../..')
    clear_local_store = (By.XPATH, '//span[text()="Очистити локальне сховище"]/../..')
    close_form = (By.CLASS_NAME, 'x-tool-close')
    clear_local_form = (By.XPATH, '//span[text()="Очистити сховище форм"]/../..')

