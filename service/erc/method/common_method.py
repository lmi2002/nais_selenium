from service.erc.pages.common_page import ErcCommonPage


class ErcMethodMain(ErcCommonPage):

    def filter_form(self, driver, value, index=None):
        self.click_btn_filter(driver)
        self.visible_x_menu(driver)
        self.select_search_param(driver, index)
        self.insert_input_textfield(driver, value)
        self.click_btn_loupe(driver)