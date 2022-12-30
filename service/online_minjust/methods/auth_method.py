import os

import pytest

from settings.setting_browser import SettingsBrowser


class OnlineMinjustAuthMethod(SettingsBrowser):
    # host = 'https://online-test.minjust.gov.ua/'
    host = 'https://online.test.nais.gov.ua/'


    @pytest.fixture
    def start_session(self):
        browser = None
        try:
            browser = self.desktop_browser(self.host)
            yield browser
        except Exception:
            browser.quit()
        else:
            browser.quit()

