from service.drrp.methods.common_method import DrrpCommonMethod
from service.drrp.pages.statement_page import DrrpStatementPage
from settings.setting_person import info


class DrrpBlockDocument(DrrpStatementPage, DrrpCommonMethod):

    def fill_block_document(self, driver):
        self.click_block_document_btn_add(driver)
        self.click_block_document_btn_add(driver)
        self.insert_value_document_type(driver, info['document']['document_type'])
        self.click_document_type_list(driver)
        self.insert_value_addition_document_type(driver, info['document']['addition_document'])
        self.insert_value_document_num(driver, info['document']['document_num'])
        self.insert_value_document_date(driver, info['document']['document_date'])
        self.insert_value_document_publisher(driver, info['document']['document_publisher'])
        self.insert_value_document_count_page(driver, info['document']['document_count_page'])
