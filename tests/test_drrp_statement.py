import time

import pytest

from service.drrp.locators.statement_locator import DrrpStatementLocator
from service.drrp.methods.auth_method import DrrpAuthMethod
from service.drrp.methods.block_address_onm import BlockAddressOnm
from service.drrp.methods.block_common_info import DrrpBlockCommonInfo
from service.drrp.methods.block_document import DrrpBlockDocument
from service.drrp.methods.block_onm import DrrpBlockOnm
from service.drrp.methods.block_payment import DrrpBlockPayment
from service.drrp.methods.block_person import DrrpBlockPerson
from service.drrp.methods.block_statement import DrrpBlockStatement
from service.drrp.methods.ubdocument import DrrpUbdocument


class TestDrrpStatement(DrrpAuthMethod, BlockAddressOnm, DrrpBlockDocument, DrrpBlockOnm,
                        DrrpBlockPayment, DrrpBlockPerson, DrrpBlockStatement, DrrpUbdocument, DrrpBlockCommonInfo):

    data_dict = {}

    @pytest.mark.smoke
    @pytest.mark.parametrize("statement", DrrpStatementLocator.sub_sub_menu_statement.keys())
    def test_drrp_create_statement(self, start_session, statement):
        browser = start_session

        if statement == 'ownership':
            self.click_main_menu_statement(browser)

        self.click_sub_menu_create_statement(browser)
        self.click_sub_sub_menu_statement(browser, statement)

        # block common info
        self.fill_block_common_info(browser, statement)

        # block onm
        self.fill_block_onm(browser)

        # block address onm
        self.fill_block_address_onm(browser)

        # block person
        self.fill_block_person(browser)

        # block payment
        self.fill_block_payment(browser)

        # block document
        self.fill_block_document(browser)

        # block statement
        self.fill_block_statement(browser)

        self.click_statement_btn_registretion(browser)

        self.click_close_form(browser)

        # self.click_close_tab(browser)
        print(self.get_text_list(browser))
        print(self.get_text_of_node_list(browser))
        time.sleep(300)
