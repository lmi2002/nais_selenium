import time
import pytest
import allure

from service.auth.methods.auth_method import AuthMethod
from service.erk.pages.common_page import ErkCommonPage
from service.erk.pages.company_page import ErkCompanyPage
from service.erk.pages.main_page import ErkMainPage
from settings import setting_erk_data_info


@allure.severity(allure.severity_level.NORMAL)
class TestErkCompany(AuthMethod, ErkMainPage, ErkCompanyPage, ErkCommonPage):

    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_company
    def test_open_page_company(self, start_session):
        browser = start_session
        self.click_desktop_select_button(browser)
        self.click_u_desktop_drawer_item_title(browser)
        self.visible_desktop_select_button_users(browser)
        self.click_label_operations(browser)
        self.visible_label_search_is_opened(browser)
        self.click_sublabel_operation_company(browser)
        self.visible_short_name(browser)
        self.click_btn_menu_add(browser)
        import pdb;
        pdb.set_trace()
        self.click_field_operation_company_category(browser)
        self.insert_value_operation_company_category(browser, setting_erk_data_info.company['operation_company_category'])
        self.select_operation_category_name(browser)
        self.insert_value_operation_company_name(browser, setting_erk_data_info.company['operation_company_name'])
        self.insert_value_operation_company_shortname(browser,
                                                      setting_erk_data_info.company['operation_company_name'])
        self.insert_value_operation_company_phone(browser, setting_erk_data_info.company['operation_company_phone'])
        self.insert_value_operation_company_edrpou(browser, setting_erk_data_info.company['operation_company_edrpou'])
        self.insert_value_operation_company_asfo(browser, setting_erk_data_info.company['operation_company_asfo'])
        self.click_operation_company_locality(browser)
        self.insert_value_operation_company_locality(browser,
                                                     setting_erk_data_info.company['operation_company_locality'])
        self.select_operation_company_locality(browser)
        self.click_operation_company_region(browser)
        self.select_peration_company_region(browser)
        self.insert_value_operation_company_post_index(browser,
                                                       setting_erk_data_info.company['operation_company_post_index'])
        self.insert_value_operation_company_asfo(browser, setting_erk_data_info.company['operation_company_asfo'])
        self.insert_value_insert_value_operation_company_post_address(browser, setting_erk_data_info.company[
            'operation_company_post_address'])
        self.insert_value_operation_company_post_street(browser,
                                                        setting_erk_data_info.company['operation_company_post_street'])

        self.click_operation_company_locality(browser)
        self.select_operation_company_locality(browser)
        self.click_operation_company_region(browser)
        self.select_peration_company_region(browser)
