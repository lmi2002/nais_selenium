from service.erk.locators.main_locator import ErkMainLocator
from helpers import base


class ErkMainPage(ErkMainLocator):
    def click_desktop_select_button(self, driver):
        base.move_to_element_and_click(driver, self.desktop_select_button)

    def click_u_desktop_drawer_item_title(self, driver):
        base.move_to_element_and_click(driver, self.u_desktop_drawer_item_title, index=3)

    def click_label_search(self, driver):
        base.move_to_element_and_click(driver, self.label_search, index=0)

    def click_sublabel_company(self, driver):
        base.move_to_element_and_click(driver, self.sublabel_company, index=1)

