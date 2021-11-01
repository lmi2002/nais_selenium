from selenium.webdriver.common.by import By

from settings import setting_erk_data_info


class ErkCompanyLocator:
    operation_company_short_name = (By.XPATH, '//span[text()="Скорочення"]/..')
    operation_company_ext_gen = (By.CSS_SELECTOR, 'td[id*="ext-gen"]')
    operation_company_ubcombobox = (By.CSS_SELECTOR, 'input[id*=ubcombobox]')
    operation_category_name = (
        By.XPATH, '//li/span[text()="{operation_company_category}"]'.format(
            operation_company_category=setting_erk_data_info.company["operation_company_category"]))
    operation_company_name = (By.CSS_SELECTOR, 'input[name="name"]')
    operation_company_shortname = (By.CSS_SELECTOR, 'input[name="shortname"]')
    operation_company_phone = (By.CSS_SELECTOR, 'input[name="phone"]')
    operation_company_edrpou = (By.CSS_SELECTOR, 'input[name="edrpou"]')
    operation_company_asfo = (By.CSS_SELECTOR, 'input[name="asfoID"]')
    operation_company_address_index = (By.CSS_SELECTOR, 'input[name="indexCode"]')
    operation_company_address_street = (By.CSS_SELECTOR, 'input[name="adrBody"]')
    operation_company_locality = (By.XPATH, '//li//span[text()="{operation_company_locality}"]'.format(
        operation_company_locality=setting_erk_data_info.company["operation_company_locality"]))
    operation_company_region = (By.XPATH, '//li/span[text()="{operation_company_region}"]'.format(
        operation_company_region=setting_erk_data_info.company["operation_company_region"]))
    field_operation_category_name = (By.CSS_SELECTOR, 'input[name="ccID"]')
    field_operation_category_region = (By.CSS_SELECTOR, 'input[name*="Atu_regionCombobox"]')
    field_operation_category_address_address = (By.CSS_SELECTOR, 'input[name*="Atu_localityCombobox"]')
    operation_company_address_address = (By.XPATH, '//li//span[text()="{operation_company_address}"]'.format(
        operation_company_address=setting_erk_data_info.company["operation_company_address"]))
    operation_company_post = (By.XPATH, '//span[text()="Поштова адреса"]/..')
    operation_company_post_index = (By.CSS_SELECTOR, 'input[name="postIndex"]')
    field_operation_company_post_address = (By.CSS_SELECTOR, 'input[name="postIDAtu"]')
    operation_company_post_street = (By.CSS_SELECTOR, 'input[name*="postAdrBody"]')
    operation_company_post_address = (By.XPATH, '//li//span[text()="{operation_company_address}"]'.format(
        operation_company_address=setting_erk_data_info.company["operation_company_address"]))
    operation_company_subord_list = (By.XPATH, '//li/span[contains(text(), "{operation_company_subord}")]'.format(
        operation_company_subord=setting_erk_data_info.company["operation_company_subord"]))
    operation_company_subord = (By.XPATH, '//span[text()="Підпорядкованість"]/..')
    tab_service_area = (By.XPATH, '//span[text()="Сфера обслуговування"]/..')
    btn_edit_service_area = (By.CLASS_NAME, 'fa-edit')
    text_edit_service_area = (By.XPATH, '//span[text()="Редагування зон обслуговування"]')
    text_edit_rename_company = (By.XPATH, '//div/span[text()="Зміни назви"]')
    list_service_area = (By.XPATH, '//tr/td//div[text()="{operation_company_region}"]'.format(
        operation_company_region=setting_erk_data_info.company["operation_company_region"]))
    fas_fa_angle_right = (By.CSS_SELECTOR, '.fas.fa-angle-right')
    btn_company_exit_form = (By.CLASS_NAME, 'fa-sign-in-alt')
    grid_company = (By.CSS_SELECTOR, 'tr[id*="gridview"]')
    tab_rename_company = (By.XPATH, '//span[text()="Зміни назви"]/..')
    fas_fa_plus_company = (By.CSS_SELECTOR, '.fas.fa-plus')
    inputs_rename_company = (By.CSS_SELECTOR, 'input[id*="textfield"].ub-require-control-u')
    input_rename_company_date = (By.CSS_SELECTOR, 'input[id*="datefield"].ub-require-control-u')
    input_textfield_rename_company = (By.CSS_SELECTOR, 'input[id*="textfield"]')
    tab_doc_company = (By.XPATH, '//span[text()="Документи"]/..')
    text_scan_doc_company = (By.XPATH, '//span[text()="Сканкопії документів (створення)"]')
    btn_add_scan_doc = (By.XPATH, '//span/span[text()="Додати електронну копію"]')
    btn_add_file = (By.XPATH, '//span[text()="З файлу"]/..')
    input_select_file = (By.CSS_SELECTOR, 'input[readonly="readonly"].ub-require-control-u')
    tab_general_statements_company = (By.XPATH, '//span[text()="Загальні відомості"]/..')
