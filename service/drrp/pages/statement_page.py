from service.drrp import list_text_line
from service.drrp.locators.common_locator import DrrpCommonLocator
from service.drrp.locators.statement_locator import DrrpStatementLocator
from helpers import base


class DrrpStatementPage(DrrpStatementLocator, DrrpCommonLocator):

    def click_sub_menu_create_statement(self, driver):
        base.move_to_element_and_click(driver, self.sub_menu_create_statement)

    def click_sub_sub_menu_statement(self, driver, statement):
        base.move_to_element_and_click(driver, self.sub_sub_menu_statement[statement])

    def click_block_common_info(self, driver):
        base.move_to_element(driver, self.block_common_info)

    def click_kind_registration(self, driver):
        base.move_to_element_and_click(driver, self.kind_registration)

    def select_kind_registration_list(self, driver):
        base.move_to_element_and_click(driver, self.kind_registration_list)

    def insert_value_num_ownership(self, driver, value):
        base.get_web_element(driver, self.num_ownership).send_keys(value)

    def insert_value_block_onm_num_ownership(self, driver, value):
        base.get_web_elements(driver, self.num_ownership)[3].send_keys(value)

    def click_form_ownership(self, driver):
        base.move_to_element_and_click(driver, self.form_ownership)

    def select_form_ownership_list(self, driver):
        base.move_to_element_and_click(driver, self.form_ownership_list)

    def click_kind_common_ownership(self, driver):
        base.move_to_element_and_click(driver, self.kind_common_ownership)

    def select_kind_common_ownership_list(self, driver):
        base.move_to_element_and_click(driver, self.kind_common_ownership_list)

    def select_kind_common_ownership_list_edit(self, driver):
        base.move_to_element_and_click(driver, self.kind_common_ownership_list_edit)

    def click_type_onm(self, driver):
        base.move_to_element_and_click(driver, self.type_onm)

    def click_block_add_onm(self, driver):
        base.move_to_element_and_click(driver, self.block_add_onm)

    def click_block_onm(self, driver):
        base.move_to_element_and_click(driver, self.block_onm)

    def select_type_onm_list(self, driver):
        base.move_to_element_and_click(driver, self.type_onm_list)

    def insert_value_addition_of_type_onm(self, driver, value):
        base.get_web_elements(driver, self.addition_of_type_onm)[3].send_keys(value)

    def click_subtype_onm(self, driver):
        base.move_to_element_and_click(driver, self.subtype_onm)

    def select_subtype_onm_list(self, driver):
        base.move_to_element_and_click(driver, self.subtype_onm_list, index=1)

    def select_subtype_onm_list_encumbrances(self, driver):
        base.move_to_element_and_click(driver, self.subtype_onm_list, index=2)

    def insert_value_addition_of_subtype_onm(self, driver, value):
        base.get_web_element(driver, self.addition_of_subtype_onm).send_keys(value)

    def insert_value_description_onm(self, driver, value):
        base.get_web_element(driver, self.description_onm).send_keys(value)

    def click_block_onm_btn_add(self, driver):
        base.move_to_element_and_click(driver, self.btn_add)

    def click_block_onm_btn_OK(self, driver):
        base.move_to_element_and_click(driver, self.btn_OK)

    def click_block_person_btn_add(self, driver):
        base.move_to_element_and_click(driver, self.btn_add, index=1)

    def click_block_add_address_onm(self, driver):
        base.move_to_element_and_click(driver, self.block_add_address_onm)

    def insert_value_address_onm_locality(self, driver, value):
        base.get_web_element(driver, self.address_onm_locality).send_keys(value)

    def select_address_onm_locality_list(self, driver):
        base.move_to_element_and_click(driver, self.address_onm_locality_list)

    def click_address_onm_street(self, driver):
        base.move_to_element_and_click(driver, self.address_onm_street)

    def insert_value_address_onm_street(self, driver, value):
        base.get_web_element(driver, self.address_onm_street).send_keys(value)

    def select_address_onm_street_list(self, driver):
        base.move_to_element_and_click(driver, self.address_onm_street_list)

    def insert_value_house_type(self, driver, value):
        base.get_web_elements(driver, self.house_type)[1].send_keys(value)

    def select_house_type_list(self, driver):
        base.move_to_element_and_click(driver, self.house_type_list)

    def insert_value_house_num(self, driver, value):
        base.get_web_elements(driver, self.house_num)[2].send_keys(value)

    def insert_value_building_type(self, driver, value):
        base.get_web_elements(driver, self.building_type)[1].send_keys(value)

    def select_building_type_list(self, driver):
        base.move_to_element_and_click(driver, self.building_type_list)

    def insert_value_building_num(self, driver, value):
        base.get_web_elements(driver, self.building_num)[2].send_keys(value)

    def insert_value_object_num_type(self, driver, value):
        base.get_web_elements(driver, self.object_num_type)[1].send_keys(value)

    def select_object_num_type_list(self, driver):
        base.move_to_element_and_click(driver, self.object_num_type_list)

    def insert_value_object_num(self, driver, value):
        base.get_web_elements(driver, self.object_num)[2].send_keys(value)

    def insert_value_addition_of_address_onm(self, driver, value):
        base.get_web_element(driver, self.addition_of_address_onm).send_keys(value)

    def click_block_address_onm_btn_OK(self, driver):
        base.move_to_element_and_click(driver, self.btn_OK, index=1)

    def click_person_type(self, driver):
        base.move_to_element_and_click(driver, self.person_type)

    def click_person_rule(self, driver):
        base.move_to_element_and_click(driver, self.person_rule)

    def click_person_rule_list(self, driver):
        base.move_to_element_and_click(driver, self.person_rule_list)

    def insert_value_person_name(self, driver, value):
        base.get_web_elements(driver, self.person_name)[5].send_keys(value)

    def insert_value_person_code(self, driver, value):
        base.get_web_elements(driver, self.person_code)[5].send_keys(value)

    def insert_value_person_phone(self, driver, value):
        base.get_web_element(driver, self.person_phone).send_keys(value)

    def insert_value_passport_series(self, driver, value):
        base.get_web_element(driver, self.passport_series).send_keys(value)

    def insert_value_passport_date(self, driver, value):
        base.get_web_element(driver, self.passport_date).send_keys(value)

    def insert_value_passport_publisher(self, driver, value):
        base.get_web_element(driver, self.passport_publisher).send_keys(value)

    def insert_value_addition_of_person(self, driver, value):
        base.get_web_elements(driver, self.addition_of_person)[2].send_keys(value)

    def click_block_person_btn_OK(self, driver):
        base.move_to_element_and_click(driver, self.btn_OK, index=2)

    def click_block_payment_btn_plus(self, driver):
        base.move_to_element_and_click(driver, self.payment_btn_plus)

    def click_payment_type(self, driver):
        base.move_to_element_and_click(driver, self.payment_type)

    def click_payment_type_list(self, driver):
        base.move_to_element_and_click(driver, self.payment_type_list)

    def insert_value_payment_num(self, driver, value):
        base.get_web_elements(driver, self.payment_num)[6].send_keys(value)

    def insert_value_payment_date(self, driver, value):
        base.get_web_element(driver, self.payment_date).send_keys(value)

    def insert_value_payment_summ(self, driver, value):
        base.get_web_element(driver, self.payment_summ).send_keys(value)

    def insert_value_org_name(self, driver, value):
        base.get_web_element(driver, self.org_name).send_keys(value)

    def click_block_document_btn_add(self, driver):
        base.move_to_element_and_click(driver, self.btn_add, index=2)

    def insert_value_statement_num(self, driver, value):
        base.get_web_element(driver, self.statement_num).send_keys(value)

    def insert_value_statement_date(self, driver, value):
        base.get_web_element(driver, self.statement_date).send_keys(value)

    def click_statement_term_review(self, driver):
        base.move_to_element_and_click(driver, self.statement_term_review)

    def click_statement_term_review_list(self, driver):
        base.move_to_element_and_click(driver, self.statement_term_review_list)

    def click_statement_receive_type(self, driver):
        base.move_to_element_and_click(driver, self.statement_receive_type)

    def click_statement_receive_type_list(self, driver):
        base.move_to_element_and_click(driver, self.statement_receive_type_list)

    def insert_value_addition_of_statement(self, driver, value):
        base.get_web_elements(driver, self.addition_of_statement)[5].send_keys(value)

    def insert_value_document_type(self, driver, value):
        base.get_web_element(driver, self.document_type).send_keys(value)

    def click_document_type_list(self, driver):
        base.move_to_element_and_click(driver, self.document_type_list)

    def insert_value_addition_document_type(self, driver, value):
        base.get_web_element(driver, self.addition_document_type).send_keys(value)

    def insert_value_document_num(self, driver, value):
        base.get_web_elements(driver, self.document_num)[8].send_keys(value)

    def insert_value_document_date(self, driver, value):
        base.get_web_elements(driver, self.document_date)[1].send_keys(value)

    def insert_value_document_publisher(self, driver, value):
        base.get_web_elements(driver, self.document_publisher)[1].send_keys(value)

    def insert_value_document_count_page(self, driver, value):
        base.get_web_element(driver, self.document_count_page).send_keys(value)

    def click_statement_btn_registretion(self, driver):
        base.move_to_element_and_click(driver, self.btn_registretion)

    def click_statement_btn_sing(self, driver):
        base.move_to_element_and_click(driver, self.btn_sing)

    def visible_ubdocument(self, driver):
        base.get_visible_element(driver, self.ubdocument)

    def click_field_type_irp(self, driver):
        base.move_to_element_and_click(driver, self.field_type_irp)

    def select_field_type_irp_list(self, driver):
        base.move_to_element_and_click(driver, self.field_type_irp_list)

    def insert_value_addition_type_irp(self, driver, value):
        base.get_web_element(driver, self.addition_type_irp).send_keys(value)

    def click_field_type_encumbrances(self, driver):
        base.move_to_element_and_click(driver, self.field_type_encumbrances)

    def select_type_encumbrances_list(self, driver):
        base.move_to_element_and_click(driver, self.type_encumbrances_list)

    def click_type_ownership(self, driver):
        base.move_to_element_and_click(driver, self.type_ownership)

    def select_type_ownership_list(self, driver):
        base.move_to_element_and_click(driver, self.type_ownership_list)

    def click_type_another_property_right(self, driver):
        base.move_to_element_and_click(driver, self.type_another_property_right)

    def select_type_another_property_right_list(self, driver):
        base.move_to_element_and_click(driver, self.type_another_property_right_list)

    def check_visible_statement_status(self, driver):
        base.get_web_element(driver, self.statement_status)

    @staticmethod
    def get_text_statement_list(driver):
        return [base.get_next_element_present_text(driver, word).text for word in
                list_text_line.statement_registration_status]

    @staticmethod
    def get_text_statement_num(driver):
        return base.get_next_element_present_text(driver, list_text_line.statement_num[0]).text

    @staticmethod
    def get_text_statement_of_node_list(driver):
        return [base.get_node_element_present_text(driver, word).text for word in
                list_text_line.statement_registration_info]

    def insert_value_form_edit_statement_field_reason(self, driver, value):
        base.get_web_element(driver, self.form_edit_statement_field_reason).send_keys(value)

    def click_form_edit_statement_button_edit(self, driver):
        base.move_to_element_and_click(driver, self.form_edit_statement_button_edit, index=1)

    def get_text_kind_common_ownership(self, driver):
        return base.get_node_element_present_text(driver, "вид спільної власності:").text

    def click_operations_tab_menu(self, driver):
        base.move_to_element_and_click(driver, self.operations_tab_menu)

    def click_form_edit_statement_undo_last_action(self, driver):
        base.move_to_element_and_click(driver, self.form_edit_statement_undo_last_action)

    def click_form_edit_statement_button_undo_last_action(self, driver):
        base.move_to_element_and_click(driver, self.form_edit_statement_button_undo_last_action, index=1)

    def check_visible_data_qtip_undo_last_action(self, driver):
        base.get_visible_element(driver, self.data_qtip_undo_last_action)

    def move_to_form_edit_statement_decision(self, driver):
        base.move_to_element(driver, self.form_edit_statement_decision)

    def click_decision_sub_menu_make_decision(self, driver):
        base.move_to_element_and_click(driver, self.decision_sub_menu_make_decision)

    def click_payment_block(self, driver):
        base.move_to_element_and_click(driver, self.payment_block)

