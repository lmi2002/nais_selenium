from selenium.webdriver.common.by import By
from settings.setting_data_info import data_info


class DrrpDecisionStatementLocator:
    decision_type_list = (
        By.XPATH,
        '//ul/li[text()="{decision_type}"]'.format(decision_type=data_info['decision_statement']['decision_type']))

    decision_part_size = (By.CSS_SELECTOR, 'input[name="partSize"]')
    decision_type = (By.CSS_SELECTOR, 'input[name="dsType"]')
    decision_addition_subtype = (By.CSS_SELECTOR, 'input[name="opReasonTypeExtension"]')
    decision_additional_info = (By.CSS_SELECTOR, 'textarea[name="additionalInfo"]')
    decision_block_info = (By.XPATH, '//*[text()="Рішення №:"]/ancestor::div')
