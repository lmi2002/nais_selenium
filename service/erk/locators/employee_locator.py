from selenium.webdriver.common.by import By

from settings import setting_erk_data_info


class ErkEmployeeLocator:
    fas_fa_plus_employee = (By.CSS_SELECTOR, '.fas.fa-plus')
    tab_employee = (By.XPATH, '//span[@class="x-tab-button"]/span[text()="Співробітники"]')
    field_category_employee = (By.CSS_SELECTOR, 'input[name="ccID"]')
    category_employee_list = (By.XPATH, '//li/span[text()="{category_employee}"]'.format(
        category_employee=setting_erk_data_info.employee["category_employee"]))
    field_position_employee = (By.CSS_SELECTOR, 'input[name="posPosID"]')
    position_employee_list = (By.XPATH, '//li/span[text()="{position_employee}"]'.format(
        position_employee=setting_erk_data_info.employee["position_employee"]))
    field_code_employee = (By.CSS_SELECTOR, 'input[name="idn"]')
    field_asfo_employee = (By.CSS_SELECTOR, 'input[name="asfoID"]')
    field_license_employee = (By.CSS_SELECTOR, 'input[name="license"]')
    field_additional_employee = (By.CSS_SELECTOR, 'input[name="additional"]')
    inputs_name_employee = (By.CSS_SELECTOR, 'input[id*="textfield"].ub-require-control-u')
    text_edit_employee = (By.XPATH, '//span[text()="Співробітник"]')
    field_phone_employee = (By.CSS_SELECTOR, 'input[name="phone"]')
    tab_attributes_employee = (By.XPATH, '//span[@class="x-tab-button"]/span[text()="Атрибути"]')
    date_start_status_attributes_employee = (By.XPATH, '//div[text()="Дата набуття статусу"]')
    operator_registrar_attributes_employee = (By.XPATH, '//div[text()="Оператор/Реєстратор"]')
    date_licence_attributes_employee = (By.XPATH, '//div[text()="Дата свідоцтва"]')
    notarius_status_attributes_employee = (By.XPATH, '//div[text()="Статус нотаріуса"]')
    notarius_position_attributes_employee = (By.XPATH, '//div[text()="Посада нотаріуса"]')
    field_value_attributes_employee = (By.CSS_SELECTOR, 'span[id*=ext-comp] input[id*=ubcombobox]')
    operator_registrar_attributes_employee_list = (
        By.XPATH, '//li/span[text()="{value_operator_registrar_attributes_employee}"]'.format(
            value_operator_registrar_attributes_employee=setting_erk_data_info.employee[
                "value_operator_registrar_attributes_employee"]))

    form_attribute_employee = (By.CSS_SELECTOR, 'div[id*=ub-wnd-erc_obj_cp_values].x-window')
    notarius_status_attributes_employee_list = (
        By.XPATH, '//li/span[text()="{value_notarius_status_attributes_employee}"]'.format(
            value_notarius_status_attributes_employee=setting_erk_data_info.employee[
                "value_notarius_status_attributes_employee"]))

    notarius_position_attributes_employee_list = (
        By.XPATH, '//li/span[text()="{value_notarius_position_attributes_employee}"]'.format(
            value_notarius_position_attributes_employee=setting_erk_data_info.employee[
                "value_notarius_position_attributes_employee"]))

    btn_save_and_close_employee = (By.CSS_SELECTOR, 'a[data-qtip="Зберегти та закрити"]')

