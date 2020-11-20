import time
import pytest

from servive.drrp.locators.statement_locator import StatementLocator
from servive.drrp.pages.statement_page import StatementPage
from settings.setting_browser import SettingsBrowser
from settings.setting_person import info


class TestStatement(SettingsBrowser, StatementPage):

    @pytest.mark.smoke
    @pytest.mark.parametrize("statement, elem", StatementLocator.sub_sub_menu_statement.items())
    def test_create_statement(self, get_user, statement, elem):
        get_user
        #browser = desktop_browser

        # if statement == "ownership":
        # self.click_main_menu_statement(browser)
        #
        # self.click_sub_menu_create_statement(browser)
        # self.click_sub_sub_menu_statement(browser, elem)
        #
        # # block common info
        # self.click_block_common_info(browser)
        # self.click_kind_registration(browser)
        # self.select_kind_registration_list(browser)
        # self.insert_value_num_ownership(browser, info['common info']['num_ownership'])
        # self.click_form_ownership(browser)
        # self.select_form_ownership_list(browser)
        # self.click_kind_common_ownership(browser)
        # self.select_kind_common_ownership_list(browser)
        #
        # # block onm
        # self.click_block_onm_btn_add(browser)
        # self.click_block_onm_btn_add(browser)
        # self.click_block_add_onm(browser)
        # self.insert_value_block_onm_num_ownership(browser, info['onm']['onm_num_ownership'])
        # self.click_type_onm(browser)
        # self.select_type_onm_list(browser)
        # self.insert_value_addition_of_type_onm(browser, info['onm']['addition_of_type_onm'])
        # self.click_subtype_onm(browser)
        # self.select_subtype_onm_list(browser)
        # self.insert_value_addition_of_subtype_onm(browser, info['onm']['addition_of_subtype_onm'])
        # self.insert_value_description_onm(browser, info['onm']['description_onm'])
        # self.click_block_onm_btn_OK(browser)
        # self.click_block_onm_btn_add(browser)
        #
        # # block address onm
        # self.click_block_add_address_onm(browser)
        # self.insert_value_address_onm_locality(browser, info['address_onm']['address_onm_locality'])
        # self.select_address_onm_locality_list(browser)
        # self.click_address_onm_street(browser)
        # time.sleep(2)
        # self.insert_value_address_onm_street(browser, info['address_onm']['address_onm_street'])
        # self.select_address_onm_street_list(browser)
        # self.insert_value_house_type(browser, info['address_onm']['house_type'])
        # self.select_house_type_list(browser)
        # self.insert_value_house_num(browser, info['address_onm']['house_num'])
        # self.insert_value_building_type(browser, info['address_onm']['building_type'])
        # self.select_building_type_list(browser)
        # self.insert_value_building_num(browser, info['address_onm']['building_num'])
        # self.insert_value_object_num_type(browser, info['address_onm']['object_num_type'])
        # self.select_object_num_type_list(browser)
        # self.insert_value_object_num(browser, info['address_onm']['object_num'])
        # self.insert_value_addition_of_address_onm(browser, info['address_onm']['addition_of_address_onm'])
        # self.click_block_address_onm_btn_OK(browser)
        #
        # # block person
        # self.click_block_person_btn_add(browser)
        # self.click_block_person_btn_add(browser)
        # self.click_person_type(browser)
        # self.click_person_rule(browser)
        # self.click_person_rule_list(browser)
        # self.insert_value_person_name(browser, info['person']['person_name'])
        # self.insert_value_person_code(browser, info['person']['person_code'])
        # self.insert_value_person_phone(browser, info['person']['person_phone'])
        # self.insert_value_passport_series(browser, info['person']['passport_series'])
        # self.insert_value_passport_date(browser, info['person']['passport_date'])
        # self.insert_value_passport_publisher(browser, info['person']['passport_publisher'])
        # self.insert_value_addition_of_person(browser, info['person']['addition_of_person'])
        # self.click_block_person_btn_OK(browser)
        #
        # # block payment
        # self.click_block_payment_btn_plus(browser)
        # self.click_block_payment_btn_plus(browser)
        # self.click_payment_type(browser)
        # self.click_payment_type_list(browser)
        # self.insert_value_payment_num(browser, info['payment']['payment_num'])
        # f = info['payment']['payment_date']
        # self.insert_value_payment_date(browser, info['payment']['payment_date'])
        # self.insert_value_payment_summ(browser, info['payment']['payment_summ'])
        # self.insert_value_org_name(browser, info['payment']['org_name'])
        # self.click_block_payment_btn_admit(browser)
        #
        # # block document
        # self.click_block_document_btn_add(browser)
        # self.click_block_document_btn_add(browser)
        # self.insert_value_document_type(browser, info['document']['document_type'])
        # self.click_document_type_list(browser)
        # self.insert_value_addition_document_type(browser, info['document']['addition_document'])
        # self.insert_value_document_num(browser, info['document']['document_num'])
        # self.insert_value_document_date(browser, info['document']['document_date'])
        # self.insert_value_document_publisher(browser, info['document']['document_publisher'])
        # self.insert_value_document_count_page(browser, info['document']['document_count_page'])
        #
        # # block statement
        # self.insert_value_statement_num(browser, info['statement']['statement_num'])
        # self.insert_value_statement_date(browser, info['statement']['statement_date'])
        # self.click_statement_term_review(browser)
        # self.click_statement_term_review_list(browser)
        # self.click_statement_receive_type(browser)
        # self.click_statement_receive_type_list(browser)
        # self.insert_value_addition_of_statement(browser, info['statement']['addition_of_statement'])
        #
        # self.click_statement_btn_registretion(browser)
        # self.visible_ubdocument(browser)
        # self.click_statement_btn_sing(browser)
        #
        # time.sleep(25)

    # @pytest.mark.smoke
    # def test_create_statemant_1(self, desktop_browser):
    #     browser = desktop_browser
    #     self.click_main_menu_statement(browser)
    #     self.click_sub_menu_create_statement(browser)
    #     self.sub_sub_menu_statement_encumbrances(browser)

