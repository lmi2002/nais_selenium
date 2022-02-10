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
    text_edit_operation_employee = (By.XPATH, '//span[contains(@class,"x-header-text") and text()="Співробітник"]')
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

    # form_attribute_employee = (By.CSS_SELECTOR, 'div[id*=ub-wnd-erc_obj_cp_values].x-window')
    form_attribute_employee = (By.XPATH, '//span[contains(@class,"x-header-text") and text()="Атрибут"]')
    notarius_status_attributes_employee_list = (
        By.XPATH, '//li/span[text()="{value_notarius_status_attributes_employee}"]'.format(
            value_notarius_status_attributes_employee=setting_erk_data_info.employee[
                "value_notarius_status_attributes_employee"]))

    notarius_position_attributes_employee_list = (
        By.XPATH, '//li/span[text()="{value_notarius_position_attributes_employee}"]'.format(
            value_notarius_position_attributes_employee=setting_erk_data_info.employee[
                "value_notarius_position_attributes_employee"]))

    btn_save_and_close_employee = (By.CSS_SELECTOR, 'a[data-qtip="Зберегти та закрити"]')
    operation_employee_company = (By.CSS_SELECTOR, 'input[name="objObjID"]')
    operation_employee_company_list = (By.XPATH, '//li//span[text()="{operation_employee_company}"]'.format(
        operation_employee_company=setting_erk_data_info.employee["operation_employee_company"]))
    operation_employee_category_list = (By.XPATH, '//li/span[text()="{operation_employee_category}"]'.format(
        operation_employee_category=setting_erk_data_info.employee["operation_employee_category"]))
    operation_employee_position_list = (By.XPATH, '//li/span[text()="{operation_employee_position}"]'.format(
        operation_employee_position=setting_erk_data_info.employee["operation_employee_position"]))
    operation_employee_notarius_position = (By.XPATH, '//li/span[text()="{position_employee}"]'.format(
        position_employee=setting_erk_data_info.employee["position_employee"]))
    date_open_attributes_operation_employee = (By.XPATH, '//div[text()="Дата відкриття"]')
    region_attributes_operation_employee = (By.XPATH, '//div[text()="Регіон"]')
    region_attributes_operation_employee_list = (By.XPATH, '//li/span[text()="{operation_employee_region}"]'.format(
        operation_employee_region=setting_erk_data_info.employee["operation_employee_region"]))
    operation_employee_x_form_trigger_first = (By.CLASS_NAME, 'x-form-trigger-first')
    x_grid_data_row_employee = (By.CLASS_NAME, 'x-grid-data-row')
    x_grid_cell_last = (By.CLASS_NAME, 'x-grid-cell-last')
    tab_substitution_employee = (By.XPATH, '//span[@class="x-tab-button"]/span[text()="Заміщення"]')
    form_substitution_employee = (By.XPATH, '//span[text()="Заміщення співробітника"]')
    field_substitution_employee = (By.CSS_SELECTOR, 'input[id*=ubcombobox]')
    substitution_employee_category_list = (By.XPATH, '//li//span[text()="{substitution_employee_category}"]'.format(
        substitution_employee_category=setting_erk_data_info.employee["substitution_employee_category"]))
    substitution_employee_company_list = (
        By.XPATH, '//li//span[contains(text(),"{substitution_employee_cut_company}")]'.format(
            substitution_employee_cut_company=setting_erk_data_info.employee["substitution_employee_cut_company"]))
    substitution_employee_region = (By.CSS_SELECTOR, 'input[name="cmpRegion"]')
    substitution_employee_region_list = (By.XPATH, '//li//span[text()="{substitution_employee_region}"]'.format(
        substitution_employee_region=setting_erk_data_info.employee["substitution_employee_region"]))
    substitution_employee_type = (By.CSS_SELECTOR, 'input[id*="RstCore_EnumCombobox-"]')
    substitution_employee_type_list = (By.XPATH, '//li//span[text()="{substitution_employee_type}"]'.format(
        substitution_employee_type=setting_erk_data_info.employee["substitution_employee_type"]))
    tab_active_employee = (By.XPATH, "//a[contains(@class, 'x-tab-active') and not(contains(@class, 'x-closable'))]")
    form_passed_employee = (By.XPATH, '//span[text()="Перехід співробітника"]')
    passed_employee_region_list = (By.XPATH, '//li//span[text()="{passed_employee_new_region}"]'.format(
        passed_employee_new_region=setting_erk_data_info.employee["passed_employee_new_region"]))

    passed_employee_category_company_list = (
        By.XPATH, '//li//span[text()="{passed_employee_new_category_company}"]'.format(
            passed_employee_new_category_company=setting_erk_data_info.employee[
                "passed_employee_new_category_company"]))

    passed_employee_company_list = (
        By.XPATH, '//li//span[contains(text(),"{passed_employee_cut_new_company}")]'.format(
            passed_employee_cut_new_company=setting_erk_data_info.employee[
                "passed_employee_cut_new_company"]))

    passed_employee_category_list = (
        By.XPATH, '//li//span[text()="{passed_employee_new_category_employee}"]'.format(
            passed_employee_new_category_employee=setting_erk_data_info.employee[
                "passed_employee_new_category_employee"]))

    btn_continue_and_close_employee = (By.CSS_SELECTOR, 'a[data-qtip="Продовжити"]')
    form_fio_employee_dublicated = (
        By.XPATH, '//span[text()="В Системі знайдено співробітників з ПІБ, аналогічним вказаному"]')
