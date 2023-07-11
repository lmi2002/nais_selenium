from selenium.webdriver.common.by import By
from settings import setting_erc_data_info


class ErcSearchLocator:
    field_name = (By.CSS_SELECTOR, 'input[name="cmpName"]')
    field_code = (By.CSS_SELECTOR, 'input[name="cmpEdrpou"]')
    ext_gen = (By.CSS_SELECTOR, 'td[id*="ext-gen"]')
    x_list_plain = (By.CSS_SELECTOR, '.x-list-plain li')
    field_rk = (By.CSS_SELECTOR, 'input[name="cmpRk"]')
    field_asfo = (By.CSS_SELECTOR, 'input[name="cmpAsfo"]')
    field_index = (By.CSS_SELECTOR, 'input[name="cmpIndex"]')
    field_street = (By.CSS_SELECTOR, 'input[name="cmpAdrBoby"]')
    field_address = (By.CSS_SELECTOR, 'input[name="cmpAddress"]')
    field_subord = (By.CSS_SELECTOR, 'input[name="cmpSubord"]')
    field_employee_first_name = (By.CSS_SELECTOR, 'input[name="cmpFName"]')
    field_employee_father_name = (By.CSS_SELECTOR, 'input[name="cmpSName"]')
    found_employees = (By.XPATH, '//div[text()="Знайдені співробітники"]')
    found_users = (By.XPATH, '//div[text()="Знайдені користувачі"]')
    found_companyes = (By.XPATH, '//div[text()="Знайдені організації"]')
    field_employee_license = (By.CSS_SELECTOR, 'input[name="cmpLicense"]')
    field_employee_code = (By.CSS_SELECTOR, 'input[name="cmpIdn"]')
    company_state_is_active = (By.XPATH, '//li[text()="{state}"]'.format(state=setting_erc_data_info.company["state"]))
    category_lawyers = (
        By.XPATH, '//li[text()="{category}"]'.format(category=setting_erc_data_info.company["category"]))
    region_kiev = (By.XPATH, '//li[text()="{region}"]'.format(region=setting_erc_data_info.company["region"]))
    employee_state_is_active = (
        By.XPATH, '//li[text()="{state}"]'.format(state=setting_erc_data_info.employee["state"]))
    employee_category_gov_notar = (
        By.XPATH, '//li[text()="{category}"]'.format(category=setting_erc_data_info.employee["category"]))
    employee_position_engineer = (
        By.XPATH, '//li[text()="{position}"]'.format(position=setting_erc_data_info.employee["position"]))
    company_address = (
        By.XPATH,
        '//li//span[text()="{address_list}"]'.format(address_list=setting_erc_data_info.company["address_list"]))
    user_state = (By.XPATH, '//li[text()="{state}"]'.format(state=setting_erc_data_info.user["state"]))
    user_user_web = (By.XPATH, '//li[text()="{user_web}"]'.format(user_web=setting_erc_data_info.user["user_web"]))
    user_category_gov_notar = (
    By.XPATH, '//li[text()="{category}"]'.format(category=setting_erc_data_info.user["category"]))
    user_role_rk = (By.XPATH, '//li[text()="{role_rk}"]'.format(role_rk=setting_erc_data_info.user["role_rk"]))
    user_role_web = (By.XPATH, '//li[text()="{role_web}"]'.format(role_web=setting_erc_data_info.user["role_web"]))
    field_statement_num = (By.CSS_SELECTOR, 'input[name="cmpNumber"]')
    field_statement_employee = (By.CSS_SELECTOR, 'input[name="cmpEmployees"]')
    statement_employee_list = (
        By.XPATH,
        '//li//span[text()="{employee}"]'.format(employee=setting_erc_data_info.statement["employee"]))
    field_statement_user = (By.CSS_SELECTOR, 'input[name="cmpUser"]')
    statement_user_list = (
        By.XPATH,
        '//li//span[text()="{user}"]'.format(user=setting_erc_data_info.statement["user"]))
    field_statement_start_date = (By.CSS_SELECTOR, 'input[name="cmpBDate"]')
    field_statement_end_date = (By.CSS_SELECTOR, 'input[name="cmpEDate"]')
    statement_state = (By.XPATH, '//li[text()="{state}"]'.format(state=setting_erc_data_info.statement["state"]))
    statement_progress = (
        By.XPATH, '//li[text()="{progress}"]'.format(progress=setting_erc_data_info.statement["progress"]))
    statement_blocked = (
        By.XPATH, '//li[text()="{bloсked}"]'.format(bloсked=setting_erc_data_info.statement["bloсked"]))
