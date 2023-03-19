import time
import pytest
import allure

from helpers import func
from service.auth.methods.auth_method import AuthMethod
from service.erk.method.common_method import ErkMethodMain
from service.erk.pages.main_page import ErkMainPage
from settings import setting_project


@allure.severity(allure.severity_level.NORMAL)
class TestErkUser(AuthMethod, ErkMainPage, ErkMethodMain):

    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_user
    def test_auth(self, start_session):
        browser = start_session(setting_project.URL)
        data_admin = setting_project.project_rule.get('erk').get('admin')
        AuthMethod().login(browser, data_admin.get('username'), data_admin.get('passw'),
                            data_admin.get('key_path'), data_admin.get('passw_key'),
                            data_admin.get('certificate'))

    # Нет возможности создать пользователя через меню Организация>Пользователь. Ошибка 500
    @pytest.mark.skip
    @pytest.mark.erk
    @pytest.mark.admin
    @pytest.mark.erk_user
    def test_create_user(self, start_session):
        browser = start_session(setting_project.URL)
        if func.get_host_name() == setting_project.REMOTE_SERVER:
            self.click_u_sidebar_collapse_button(browser)

        self.click_desktop_select_button(browser)
        self.click_u_desktop_drawer_item_title(browser)
        self.visible_desktop_select_button_users(browser)
        if func.get_host_name() == setting_project.REMOTE_SERVER:
            self.open_label_operations(browser)
        else:
            self.click_label_operations(browser)
            self.visible_label_search_is_opened(browser)
            self.check_invisible_v_enter_active(browser)

        self.click_sublabel_user(browser)
        self.click_btn_menu_add(browser)
        import pdb;
        pdb.set_trace()
