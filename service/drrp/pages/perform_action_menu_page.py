from helpers import base
from service.drrp.locators.perform_action_menu_locator import DrrpPerformActionMenuLocator


class DrrpPerformActionMenuPage(DrrpPerformActionMenuLocator):

    def click_button_perform_action(self, driver):
        base.move_to_element_and_click(driver, self.button_perform_action)

    def click_menu_edit(self, driver):
        base.move_to_element_and_click(driver, self.menu_edit)