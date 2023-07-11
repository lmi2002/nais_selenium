from service.erc.locators.main_locator import ErcMainLocator
from helpers import base


class ErcMainPage(ErcMainLocator):
    def click_desktop_select_button(self, driver):
        base.move_to_element_and_click(driver, self.desktop_select_button)

    def click_u_desktop_drawer_item_title(self, driver):
        base.move_to_element_and_click(driver, self.u_desktop_drawer_item_title, index=4)

    def click_label_search(self, driver):
        base.move_to_element_and_click(driver, self.label_search)

    def visible_label_search_is_opened(self, driver):
        base.get_visible_element(driver, self.label_search_is_opened)

    def click_sublabel_company(self, driver):
        base.move_to_element_and_click(driver, self.sublabel_company, index=1)

    def visible_desktop_select_button_users(self, driver):
        base.get_visible_element(driver, self.desktop_select_button_users)

    def click_sublabel_employee(self, driver):
        base.move_to_element_and_click(driver, self.sublabel_employee, index=0)

    def click_search_sublabel_employee(self, driver):
        base.move_to_element_and_click(driver, self.sublabel_employee, index=1)

    def click_sublabel_user(self, driver, index=None):
        base.move_to_element_and_click(driver, self.sublabel_user, index=index)

    def click_sublabel_search_statement(self, driver):
        base.move_to_element_and_click(driver, self.sublabel_search_statement, index=0)

    def click_close_tab_admin_first(self, driver):
        base.click(driver, self.close_tab_admin)

    def click_label_operations(self, driver):
        base.move_to_element_and_click(driver, self.label_operations)

    def click_sublabel_operation_company(self, driver):
        base.move_to_element_and_click(driver, self.sublabel_company)

    def check_invisible_v_enter_active(self, driver):
        base.check_invisible_element(driver, self.v_enter_active)

    def click_u_sidebar_collapse_button(self, driver):
        base.move_to_element_and_click(driver, self.u_sidebar_collapse_button)

    def open_label_operations(self, driver):
        driver.execute_script('document.querySelector(".el-submenu ul").style.display = null;')
