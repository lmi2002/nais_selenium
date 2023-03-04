import time
import os

import pytest

import allure

from helpers.func import extract_text_from_pdf
from service.auth.methods.auth_method import AuthMethod
from service.drrp.methods.block_address_onm import BlockAddressOnm
from service.drrp.methods.block_common_info import DrrpBlockCommonInfo
from service.drrp.methods.block_document import DrrpBlockDocument
from service.drrp.methods.block_onm import DrrpBlockOnm
from service.drrp.methods.block_payment import DrrpBlockPayment
from service.drrp.methods.block_person import DrrpBlockPerson
from service.drrp.methods.block_statement import DrrpBlockStatement
from service.drrp.methods.ubdocument import DrrpUbdocument
from service.drrp.pages.statement_page import DrrpFormRequestEdrsrPage
from settings.setting_data_info import data_info


@allure.severity(allure.severity_level.NORMAL)
class TestExchange(AuthMethod, DrrpBlockOnm, DrrpUbdocument, BlockAddressOnm, DrrpBlockDocument,
                   DrrpBlockPayment, DrrpBlockPerson, DrrpBlockStatement, DrrpBlockCommonInfo,
                   DrrpFormRequestEdrsrPage):

    @pytest.mark.skip
    def test_exchange_dzk(self, start_browser_with_login):
        browser = start_browser_with_login
        self.click_main_menu_statement(browser)
        self.visible_li_is_opened(browser)
        self.click_sub_menu_create_statement(browser)
        self.click_sub_sub_menu_statement(browser, 'ownership')

        self.fill_block_onm_dzk(browser)

        src = self.get_attr_src_iframe(browser)
        browser.get(src)
        file_dzk = os.path.join(self.get_download_dir_pdf(), os.path.basename(src).split('#')[0] + '.pdf')
        file_pattern_dzk = os.path.abspath('../storages/pattern_pdf/pattern_dzk.pdf')

        time.sleep(4)
        text_file_dzk = extract_text_from_pdf(file_dzk)
        text_file_pattern_dzk = extract_text_from_pdf(file_pattern_dzk)

        assert (text_file_dzk == text_file_pattern_dzk)

        self.click_close_form(browser)

    def test_exchange_dabi(self, start_browser_with_login):
        browser = start_browser_with_login
        self.click_main_menu_statement(browser)
        self.visible_li_is_opened(browser)
        self.click_sub_menu_create_statement(browser)
        self.click_sub_sub_menu_statement(browser, 'ownership')

        self.fill_block_document_dabi(browser)
        self.click_span_get_erd(browser)

        src = self.get_attr_src_iframe(browser)
        browser.get(src)
        file_dabi = os.path.join(self.get_download_dir_pdf(), os.path.basename(src).split('#')[0] + '.pdf')
        file_pattern_dabi = os.path.abspath('../storages/pattern_pdf/pattern_dabi.pdf')

        time.sleep(4)
        text_file_dabi = extract_text_from_pdf(file_dabi)
        text_file_pattern_dabi = extract_text_from_pdf(file_pattern_dabi)

        assert (text_file_dabi == text_file_pattern_dabi)

        self.click_close_form(browser)

    @pytest.mark.skip
    def test_exchange_edrsr(self, start_browser_with_login):
        browser = start_browser_with_login
        statement = 'ownership'

        self.click_main_menu_statement(browser)

        self.visible_li_is_opened(browser)
        self.click_sub_menu_create_statement(browser)
        self.click_sub_sub_menu_statement(browser, statement)

        # block common info
        self.fill_block_common_info(browser, statement)

        # block onm
        self.fill_block_onm(browser, statement)

        # block address onm
        self.fill_block_address_onm(browser)

        # block person
        self.fill_block_person(browser)

        # block payment
        self.fill_block_payment(browser)

        # block document
        self.fill_block_document_edrsr(browser)

        # block statement
        self.fill_block_statement(browser)

        self.click_statement_btn_registretion(browser)

        self.document_btn_close(browser)
        self.check_visible_statement_status(browser)
        self.click_document_tab_menu(browser)
        self.click_document_tab_menu_image_doc(browser)
        time.sleep(1.2)
        self.click_get_edrsr(browser)

        self.insert_value_form_request_edrsr_date(browser, data_info["request_edrsr"]["document_date"], 1)
        self.insert_value_form_request_edrsr_num(browser, data_info["request_edrsr"]["document_date"], 1)

