import pytest

from settings.setting_browser import SettingsBrowser
from settings.setting_allure import SettingAllure


class OnlineMinjustAuthMethod:
    host = 'https://online.test.nais.gov.ua/'

    @pytest.fixture
    def host_obu(self):
        return self.host


    @pytest.fixture
    def start_browser_obu(self, host_obu):
        browser = SettingsBrowser().desktop_browser(host_obu)
        try:
            yield browser
            SettingAllure().create_screenshot(browser)
            browser.quit()
        except Exception:
            SettingAllure().create_screenshot(browser)
            browser.quit()

