import pytest

from pages.auth_page import AuthPage
from settings.setting_rule_user import users


class AuthMethod(AuthPage):
    # @pytest.fixture()
    # @pytest.mark.parametrize("rule", users.keys())
    def login(self, driver):
        self.get_user(driver).send_keys(users["notarius"]['login'])
        self.get_passw(driver).send_keys(users["notarius"]['passw'])
        self.get_entry(driver).click()
