import os

import pytest

from settings.setting_browser import SettingsBrowser


class OnlineMinjustAuthMethod(SettingsBrowser):
    host = 'https://online.test.nais.gov.ua/'


    @pytest.fixture
    def start_module_obu(self):
        browser = None
        try:
            browser = self.desktop_browser(self.host)
            yield browser
        except Exception:
            browser.quit()
        else:
            browser.quit()

