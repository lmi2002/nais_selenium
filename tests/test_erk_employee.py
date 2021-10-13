import time
import pytest
import allure

from service.auth.methods.auth_method import AuthMethod
from service.erk.pages.main_page import ErkMainPage


@allure.severity(allure.severity_level.NORMAL)
class TestErkEmployee(AuthMethod, ErkMainPage):
    dict_employee = {}

    # dict_employee['company_name'] = setting_erk_data_info.company['operation_company_name']

    @pytest.mark.skip
    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_company
    def test_create_company(self, start_session):
        browser = start_session
        self.click_sublabel_employee(browser)
        self.click_btn_add_emloyee(browser)

