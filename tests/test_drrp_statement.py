import time

import pytest
from settings.setting_data_info import data_info
from helpers.func import get_data_today
from service.drrp.list_data_validation import onm_dict
from service.drrp.locators.statement_locator import DrrpStatementLocator
from service.drrp.methods.auth_method import DrrpAuthMethod, project_rule, PROJECT, RULE
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
        tuple_statement_data_first = (
            'зареєстровано', self.statement_name[statement], get_data_today(), project_rule[PROJECT][RULE]['name_user'])

        tuple_statement_data_second = (
            data_info['statement']['statement_num'], data_info['statement']['statement_date'],
            data_info['payment']['payment_summ'],
            data_info['payment']['payment_num'])

        tuple_person_data = (
            'Фізична особа {person_name} код: {person_code}'.format(person_name=data_info['person']['person_name'],
                                                                    person_code=data_info['person']['person_code']),
            'Громадянство: Україна паспорт громадянина України: {passport_series} {passport_date} р. ' \
            'видавник {passport_publisher}'.format(
                passport_series=data_info['person']['passport_series'],
                passport_date=data_info['person']['passport_date'],
                passport_publisher=info['person']['passport_publisher']),
            'Наявна уповн. особа: ні Телефон/email: {person_phone} Додаткові відомості: {addition_of_person}'.format(
                person_phone=data_info['person']['person_phone'], addition_of_person=data_info['person']['addition_of_person'])
        )

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

        # statement
        for num, vlf in enumerate(self.get_text_statement_list(browser)):
            assert tuple_statement_data_first[num] in vlf

        for num, vls in enumerate(self.get_text_statement_of_node_list(browser)):
            assert tuple_statement_data_second[num], vls

        # person
        self.click_person_tab_menu(browser)

        for num, pd in enumerate(self.get_text_person_of_node_list(browser)):
            assert pd == tuple_person_data[num]

        # onm
        self.click_onm_tab_menu(browser)

        for num, onl in enumerate(self.get_text_onm_of_node_list(browser, statement)):
            assert onm_dict[statement][num] == onl

        self.click_close_tab(browser)
