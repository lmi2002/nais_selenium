import time
import pytest
import allure

from helpers import func
from service.auth.methods.auth_method import AuthMethod
from service.erk.method.common_method import ErkMethodMain
from service.erk.pages.main_page import ErkMainPage
from settings.setting_project import REMOTE_SERVER


@allure.severity(allure.severity_level.NORMAL)
class TestErkUser(AuthMethod, ErkMainPage, ErkMethodMain):

    # Нет возможности создать пользователя через меню Организация>Пользователь. Ошибка 500
    @pytest.mark.skip
    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_employee
    def test_create_user(self, start_session):
        browser = start_session
        if func.get_host_name() == REMOTE_SERVER:
            self.click_u_sidebar_collapse_button(browser)

        self.click_desktop_select_button(browser)
        self.click_u_desktop_drawer_item_title(browser)
        self.visible_desktop_select_button_users(browser)
        if func.get_host_name() == REMOTE_SERVER:
            self.open_label_operations(browser)
        else:
            self.click_label_operations(browser)
            self.visible_label_search_is_opened(browser)
            self.check_invisible_v_enter_active(browser)

        self.click_sublabel_user(browser)
        self.click_btn_menu_add(browser)
