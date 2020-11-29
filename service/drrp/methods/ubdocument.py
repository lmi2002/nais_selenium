from service.drrp.methods.common_method import DrrpCommonMethod
from service.drrp.pages.statement_page import DrrpStatementPage


class DrrpUbdocument(DrrpStatementPage, DrrpCommonMethod):

    def document_btn_sing(self, driver):
        self.visible_ubdocument(driver)
        self.click_statement_btn_sing(driver)
