from service.erk.pages.common_page import ErkCommonPage


class ErkMethodMain(ErkCommonPage):

    def filter_form(self, driver, value, index=None):
        self.click_btn_filter(driver)
        self.visible_x_menu(driver)
        self.select_search_param(driver, index)
        self.insert_input_textfield(driver, value)
        self.click_btn_loupe(driver)