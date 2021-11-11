# Check start tests from Jenkins
import pytest
import requests
from bs4 import BeautifulSoup

import allure
from settings.setting_browser import SettingsBrowser
from settings.setting_sreenshots import SettingsScreenshots


@allure.severity(allure.severity_level.NORMAL)
class TestJenkins(SettingsScreenshots):
    sb = SettingsBrowser()

    @pytest.mark.check_jenkins
    def test_check_jenkins_register(self):
        browser = self.sb.desktop_browser()
        cur_url = browser.current_url
        print('Opened ' + cur_url)
        assert browser.title == 'ІС ДП"НАІС"(SRV-42)'
        self.create_screenshot(browser)
        browser.close()

    @pytest.mark.skip
    @pytest.mark.check_jenkins
    def test_check_jenkins_ukrnet(self):
        browser = self.sb.desk_browser()
        assert browser.title == 'UKR.NET: Всі новини України, останні новини дня в Україні та Світі'
        self.create_screenshot(browser)
        browser.close()

    def test_check_jenkins_register_bs4(self):
        soup = BeautifulSoup(requests.get('https://register.test.nais.gov.ua').content, 'html.parser')
        assert soup.title.string == 'ІС ДП"НАІС"(SRV-42)'

    def test_check_jenkins_register_request(self):
        response = requests.get('https://register.test.nais.gov.ua')
        assert response.status_code == 200
