import time

import allure
import pytest

from helpers.func import get_data_today
from service.drrp.list_data_validation import onm_validation, statement_validation_second, person_validation, \
    address_onm_validation
from settings.setting_data_info import data_info
from service.drrp.locators.statement_locator import DrrpStatementLocator
from settings.setting_project import project_rule, PROJECT, RULE
from service.auth.methods.auth_method import AuthMethod
from service.drrp.methods.block_address_onm import BlockAddressOnm
from service.drrp.methods.block_common_info import DrrpBlockCommonInfo
from service.drrp.methods.block_document import DrrpBlockDocument
from service.drrp.methods.block_onm import DrrpBlockOnm
from service.drrp.methods.block_payment import DrrpBlockPayment
from service.drrp.methods.block_person import DrrpBlockPerson
from service.drrp.methods.block_statement import DrrpBlockStatement
from service.drrp.methods.decision_statement_method import DrrpDecisionStatementMethod
from service.drrp.methods.ubdocument import DrrpUbdocument
from service.drrp.pages.perform_action_menu_page import DrrpPerformActionMenuPage
from service.drrp.pages.search_statement_page import DrrpSearchStatementPage


@allure.severity(allure.severity_level.NORMAL)
class TestDrrpStatement(AuthMethod, BlockAddressOnm, DrrpBlockDocument, DrrpBlockOnm,
                        DrrpBlockPayment, DrrpBlockPerson, DrrpBlockStatement, DrrpUbdocument, DrrpBlockCommonInfo,
                        DrrpSearchStatementPage, DrrpPerformActionMenuPage, DrrpDecisionStatementMethod):
    data_dict = {}
    statement_name = {
        "ownership": "заява про державну реєстрацію права власності",
        "irp": "заява про державну реєстрацію іншого речового права",
        "encumbrances": "заява про державну реєстрацію обтяження",
        "relinquishment_of_property": "заява про відмову від права власності, іншого речового права"
    }

    @pytest.mark.smoke
    @pytest.mark.notarius
    @pytest.mark.first
    @pytest.mark.parametrize("statement", DrrpStatementLocator.sub_sub_menu_statement.keys())
    def test_create_statement(self, start_session, statement):

        data_list = []
        browser = start_session

        statement_validation_first = (
            'зареєстровано', self.statement_name[statement], get_data_today(), project_rule[PROJECT][RULE]['name_user'])

        if statement == 'ownership':
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
        self.fill_block_document(browser)

        # block statement
        self.fill_block_statement(browser)

        self.click_statement_btn_registretion(browser)

        self.document_btn_close(browser)
        self.check_visible_statement_status(browser)

        data_list.append(self.get_text_statement_num(browser))
        data_list.append(self.get_text_statement_list(browser))
        self.data_dict[statement] = data_list

        # validated data statement
        for num, v in enumerate(self.get_text_statement_list(browser)):
            assert statement_validation_first[num] in v

        for num, v in enumerate(self.get_text_statement_of_node_list(browser)):
            assert statement_validation_second[num] in v

        self.click_person_tab_menu(browser)

        # validated data person
        for num, v in enumerate(self.get_text_person_of_node_list(browser)):
            assert v == person_validation[num]

        self.click_onm_tab_menu(browser)

        # validated data onm
        for num, v in enumerate(self.get_text_onm_of_node_list(browser, statement)):
            assert onm_validation[statement][num] == v

        # validated data address_onm
        assert (self.get_text_line_address_onm(browser)[0],
                self.get_text_line_address_onm(browser)[1]) == address_onm_validation

        self.click_close_tab_ub64(browser)

    @pytest.mark.smoke
    @pytest.mark.notarius
    def test_search_statement(self, start_session):
        browser = start_session
        statement_num = self.data_dict.get('ownership')[0]
        # self.click_main_menu_statement(browser)
        self.click_sub_menu_search_statement(browser)
        self.insert_value_num_statement(browser, statement_num)
        self.click_button_search_ub64(browser)
        self.double_click_gridview(browser)
        self.click_close_tab_ub64(browser)
        self.click_button_continue(browser)
        self.check_visible_statement_status(browser)
        assert self.get_text_statement_num(browser) == statement_num

    @pytest.mark.smoke
    @pytest.mark.notarius
    def test_edit_statement(self, start_session):
        browser = start_session
        self.click_button_perform_action(browser)
        self.click_menu_edit(browser)
        self.insert_value_form_edit_statement_field_reason(browser, "Помилка")
        self.click_form_edit_statement_button_edit(browser)
        self.click_kind_common_ownership(browser)
        self.select_kind_common_ownership_list_edit(browser)
        self.click_btn_admit(browser, index=1)
        self.click_onm_tab_menu(browser)
        assert data_info['onm']['kind_common_ownership_edit'] in self.get_text_kind_common_ownership(browser)

    @pytest.mark.smoke
    @pytest.mark.notarius
    def test_undo_last_action(self, start_session):
        browser = start_session
        self.click_button_perform_action(browser)
        self.click_form_edit_statement_undo_last_action(browser)
        self.insert_value_form_edit_statement_field_reason(browser, "Помилка")
        self.click_form_edit_statement_button_undo_last_action(browser)
        self.check_visible_el_dialog_footer(browser)
        self.click_el_dialog_footer_button(browser)
        self.check_visible_statement_status(browser)
        time.sleep(1)
        self.click_operations_tab_menu(browser)
        self.check_visible_data_qtip_undo_last_action(browser)
        self.click_onm_tab_menu(browser)
        assert data_info['onm']['kind_common_ownership'] in self.get_text_kind_common_ownership(browser)

    @pytest.mark.smoke
    @pytest.mark.notarius
    def test_decision_statement(self, start_session):
        decision_validation = (
            'зареєстровано', 'про державну реєстрацію прав та їх обтяжень', get_data_today(),
            project_rule[PROJECT][RULE]['name_user'])

        browser = start_session
        self.click_button_perform_action(browser)
        self.move_to_form_edit_statement_decision(browser)
        self.click_decision_sub_menu_make_decision(browser)
        # self.check_visible_message(browser)
        # self.click_message_btn_Так(browser)
        self.check_visible_el_dialog_footer(browser)
        self.click_el_dialog_footer_button(browser, index=1)
        self.fill_decision(browser)
        self.click_decision_btn_registration(browser)
        self.document_btn_close(browser, index=1)
        self.click_close_tab_ub64(browser)

        # validated data decision
        data_decision = self.data_decision_block_info(browser)
        self.data_dict['decision'] = data_decision
        list_decision_info = data_decision[1]

        for num, v in enumerate(decision_validation):
            assert v in list_decision_info[num]
