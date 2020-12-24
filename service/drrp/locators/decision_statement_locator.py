from selenium.webdriver.common.by import By
from settings.setting_data_info import data_info


class DrrpDecisionStatementLocator:
    decision_type_list = (
        By.XPATH,
        '//ul/li[text()="{decision_type}"]'.format(decision_type=data_info['decision_statement']['decision_type']))

    decision_type = (By.CSS_SELECTOR, 'input[name="dsType"]')
    decision_addition_subtype = (By.XPATH, '//*[text()="Доповнення до підстави"]/../following-sibling::*')
    decision_additional_info = (By.CSS_SELECTOR, 'input[name="additionalInfo"]')
