from service.drrp.methods.common_method import DrrpCommonMethod
from service.drrp.pages.statement_page import DrrpStatementPage


class DrrpUbdocument(DrrpStatementPage, DrrpCommonMethod):

    def document_btn_sing(self, driver):
        self.visible_ubdocument(driver)
        self.click_statement_btn_sing(driver)

    def document_btn_close(self, driver, index=None):
        self.visible_ubdocument(driver)
        self.click_close_form(driver, index)



