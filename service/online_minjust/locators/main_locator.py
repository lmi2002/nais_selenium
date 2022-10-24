from selenium.webdriver.common.by import By

from settings.setting_project import *


class OnlineMinjustMainLocator:
    btn_pass_to_rrp = (By.XPATH, '//a[@href="/rrp/"]')
    btn_pass_to_auth_page = (By.XPATH, '//a[contains(@href,"/managers/services/extract")]')
    cas_servers_select = (By.ID, 'CAsServersSelect')
    pkey_file_input = (By.ID, 'PKeyFileInput')
    pkey_password = (By.ID, 'PKeyPassword')
    submit_ecp = (By.ID, 'submit-ecp')
    btn_service = (By.XPATH, '//a[contains(@href,"/managers/services/home")]')
    gradea_even_td = (By.CSS_SELECTOR, '.gradeA.even td')
    extract_option = (By.CSS_SELECTOR, 'input[name="extractOption"]')
    btn_next = (By.CSS_SELECTOR, '.btn.btn-success')
    field_onm = (By.CSS_SELECTOR, 'input[name="number"]')
    form_group_title = (By.CLASS_NAME, 'form-group-title')
    gradea_even_td_a = (By.CSS_SELECTOR, '.gradeA.even td a')
    btn_payment_type_portmone = (By.CSS_SELECTOR, 'button[name="payment_type"]')
    btn_payment_confirm = (By.CSS_SELECTOR, 'button[name="payment_confirm"]')
    panel_body = (By.CLASS_NAME, 'panel-body')



