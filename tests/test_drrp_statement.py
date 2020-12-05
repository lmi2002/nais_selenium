import time

import pytest
from helpers.func import get_data_today
from service.drrp.list_data_validation import onm_validation, statement_validation_second, person_validation
from service.drrp.locators.statement_locator import DrrpStatementLocator
from settings.setting_project import project_rule, PROJECT, RULE
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

    statement_name = {
        "ownership": "заява про державну реєстрацію права власності",
        "irp": "заява про державну реєстрацію іншого речового права",
        "encumbrances": "заява про державну реєстрацію обтяження",
        "relinquishment_of_property": "заява про відмову від права власності, іншого речового права"
    }

    @pytest.mark.smoke
    @pytest.mark.parametrize("statement", DrrpStatementLocator.sub_sub_menu_statement.keys())
    def test_drrp_create_statement(self, start_session, statement):
        statement_validation_first = (
            'зареєстровано', self.statement_name[statement], get_data_today(), project_rule[PROJECT][RULE]['name_user'])

        browser = start_session

        if statement == 'ownership':
            self.click_main_menu_statement(browser)

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
        self.fill_block_document(browser)

        # block statement
        self.fill_block_statement(browser)

        self.click_statement_btn_registretion(browser)

        self.click_close_form(browser)
        self.check_visible_statement_status(browser)

        self.data_dict[statement] = self.get_text_statement_list(browser)[0]

        # validated data statement
        for num, v in enumerate(self.get_text_statement_list(browser)):
            assert statement_validation_first[num] in v

        for num, v in enumerate(self.get_text_statement_of_node_list(browser)):
            assert statement_validation_second[num] in v

        # validated data person
        self.click_person_tab_menu(browser)

        for num, v in enumerate(self.get_text_person_of_node_list(browser)):
            assert v == person_validation[num]

        # validated data onm
        self.click_onm_tab_menu(browser)

        for num, v in enumerate(self.get_text_onm_of_node_list(browser, statement)):
            assert onm_validation[statement][num] == v

        self.click_close_tab(browser)
