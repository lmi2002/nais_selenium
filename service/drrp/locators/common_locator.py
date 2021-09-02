from selenium.webdriver.common.by import By

from settings.setting_project import *


class DrrpCommonLocator:
    btn_add = (By.XPATH, '//span[text()="Додати"]/..')
    btn_OK = (By.XPATH, '//span[text()="ОК"]/..')
    btn_plus = (By.XPATH, '//span[text()=""]/..')
    btn_registretion = (By.XPATH, '//span[text()="Зареєструвати"]/..')
    btn_sing = (By.XPATH, '//span[text()="Підписати ЕЦП"]/..')
    user_code = (By.XPATH, '//span[text()="{user_code}"]/..'.format(
        user_code=project_rule[PROJECT][RULE]['login']))
    exit = (By.XPATH, '//span[contains(text(), "Вихід")]')
    user_menu_cash = (By.XPATH, '//span[text()="Дані, що збережено"]/../..')
    clear_local_store = (By.XPATH, '//span[text()="Очистити локальне сховище"]/../..')
    close_form = (By.CLASS_NAME, 'x-tool-close')
    clear_local_form = (By.XPATH, '//span[text()="Очистити сховище форм"]/../..')
    close_tab = (By.CSS_SELECTOR, 'span[title="Закрити вкладку"]')
    person_tab_menu = (By.XPATH, '//span[text()="Суб’єкти"]/..')
    document_tab_menu = (By.XPATH, '//span[text()="Супровідні документи"]/..')
    document_tab_menu_image_doc = (By.CLASS_NAME, 'fa-file-alt')
    onm_tab_menu = (By.XPATH, '//span[text()="ОНМ"]/..')
    line_address_onm = (By.XPATH, '//*[text()="Адреса ОНМ"]/ancestor::legend/following::label')
    main_menu_statement = (By.XPATH, '//span[text()="Реєстрація та обробка заяв"]/..')
    button_search = (By.XPATH, '//span[text()="Пошук"]')
    gridview = (By.CSS_SELECTOR, 'tr[id^="gridview"]')
    button_continue = (By.XPATH, '//span[text()="Продовжити"]')
    btn_admit = (By.XPATH, '//span[text()="Застосувати"]')
    message_btn_OK = (By.XPATH, '//span[text()="OK"]/..')
    messagebox = (By.CLASS_NAME, 'x-message-box')
    el_dialog_footer = (By.CLASS_NAME, 'el-dialog__footer')
    el_dialog_footer_button = (By.CSS_SELECTOR, '.el-dialog__footer button')
    loader = (By.CLASS_NAME, '.x-mask-msg')
    message_btn_Так = (By.XPATH, '//span[text()="Так"]/..')
    close_tab_ub64 = (By.CLASS_NAME, 'u-navbar__tab-close-button')
    u_navbar_dropdown = (By.CLASS_NAME, 'u-navbar__dropdown')
    iframe = (By.TAG_NAME, 'iframe')



