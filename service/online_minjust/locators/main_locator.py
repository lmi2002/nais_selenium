from selenium.webdriver.common.by import By

from settings.setting_online_minjust_data_info import address


class OnlineMinjustMainLocator:
    modal_content = (By.CSS_SELECTOR, '.modal-content')
    btn_pass_to_rrp = (By.XPATH, '//a[@href="/rrp/"]')
    btn_pass_to_info_rrp = (By.XPATH, '//a[contains(@href,"/managers/services/extract")]')
    btn_pass_to_zaborona_rrp = (By.XPATH, '//a[contains(@href,"/managers/services/zaborona")]')
    cas_servers_select = (By.ID, 'CAsServersSelect')
    pkey_file_input = (By.ID, 'PKeyFileInput')
    pkey_password = (By.ID, 'PKeyPassword')
    submit_ecp = (By.ID, 'submit-ecp')
    btn_service = (By.XPATH, '//a[contains(@href,"/managers/services/home")]')
    gradea_even_td = (By.CSS_SELECTOR, '.gradeA.even td')
    extract_option = (By.CSS_SELECTOR, 'input[name="extractOption"]')
    btn_next = (By.CSS_SELECTOR, '.btn.btn-success')
    field_onm = (By.CSS_SELECTOR, 'input[name="number"]')
    field_cad_num = (By.CSS_SELECTOR, 'input[name="kadastr"]')
    form_group_title = (By.CLASS_NAME, 'form-group-title')
    gradea_even_td_a = (By.CSS_SELECTOR, '.gradeA.even td a')
    gradea_even_td_a = (By.CSS_SELECTOR, '.gradeA.even td a')
    btn_payment_type_portmone = (By.CSS_SELECTOR, 'button[name="payment_type"]')
    btn_payment_confirm = (By.CSS_SELECTOR, 'button[name="payment_confirm"]')
    panel_body = (By.CLASS_NAME, 'panel-body')
    select2_selection_single = (By.CSS_SELECTOR, '.select2-selection.select2-selection--single')
    dropdown_list = (By.CSS_SELECTOR, '.select2-results ul li')
    select_street_dropdown = (By.XPATH, '//span[@class="select2-results"]/ul/li[contains(text(), "{street}")]'.format(
        street=address.get('street')))
    house_type = (By.CSS_SELECTOR, '.col-md-6 select#houseType')
    object_num_type = (By.CSS_SELECTOR, '.col-md-6 select#objectNumType')
    input_field_num_house = (By.CSS_SELECTOR, 'input[name="house"]')
    input_field_num_appart = (By.CSS_SELECTOR, 'input[name="objectNum"]')
    input_field_persone_code = (By.CSS_SELECTOR, 'input[name="code"]')
    input_field_persone_name = (By.CSS_SELECTOR, 'input[name="name"]')
    collapse_in_div_p = (By.CSS_SELECTOR, '.collapse.in div p')
    actions_text_center = (By.CSS_SELECTOR, '.actions.text-center')


