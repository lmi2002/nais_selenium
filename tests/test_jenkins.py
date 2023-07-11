# Check start tests from Jenkins
import os
import time

import pytest
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import allure
from helpers import base
from service.auth.pages.auth_page import AuthPage
from service.drrp.pages.common_page import DrrpCommonPage
from settings import setting_project
from settings.setting_browser import SettingsBrowser
from settings.setting_project import project_rule, PROJECT, RULE
from settings.setting_allure import SettingAllure


@allure.severity(allure.severity_level.NORMAL)
class TestJenkins(SettingsBrowser, AuthPage, DrrpCommonPage, SettingAllure):

    @pytest.mark.skip
    @pytest.mark.check_jenkins
    def test_check_jenkins_register(self):
        browser = self.desktop_browser(setting_project.URL)
        cur_url = browser.current_url
        print('Opened ' + cur_url)
        print('title = ' + browser.title)
        print(self.remote_server)
        self.create_screenshot(browser)
        browser.close()

    # @pytest.mark.skip
    @pytest.mark.check_jenkins
    def test_check_jenkins_beebom(self):
        browser = self.desk_browser()
        assert browser.title == 'Beebom - Tech That Matters'
        self.create_screenshot(browser)
        browser.close()

    @pytest.mark.skip
    def test_check_jenkins_register_bs4(self):
        soup = BeautifulSoup(requests.get('https://register.test.nais.gov.ua').content, 'html.parser')
        assert soup.title.string == 'ІС ДП"НАІС"(SRV-42)'

    @pytest.mark.skip
    def test_check_jenkins_register_request(self):
        response = requests.get('https://register.test.nais.gov.ua')
        assert response.status_code == 200

