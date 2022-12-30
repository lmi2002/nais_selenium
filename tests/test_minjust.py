from selenium.webdriver import DesiredCapabilities, ActionChains

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from helpers import func
from settings.setting_project import *
from settings.setting_sreenshots import SettingsScreenshots


class SettingsBrowser(SettingsScreenshots):
    local_path_UBExtension = os.path.abspath('../extension/extension_1_3_1_9.crx')

    @staticmethod
    def get_executable_path():
        if func.get_host_name() != REMOTE_SERVER:
            executable_path = os.path.abspath('../drivers/win_local/chromedriver.exe')
        else:
            executable_path = os.path.abspath('../drivers/win_jen/chromedriver.exe')
        return executable_path

    download_dir_pdf = os.path.abspath('../storages/files_pdf')

    func.get_host_name()

    def set_chrome(self, page_load_strategy='normal', width=1920, height=1080):
        profile = {
            "download.default_directory": self.download_dir_pdf,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        }

        chrome_options = Options()
        capabilities = DesiredCapabilities.CHROME
        capabilities["pageLoadStrategy"] = page_load_strategy
        chrome_options.add_argument('--no-sandbox')
        if func.get_host_name() == REMOTE_SERVER:
            # chrome_options.add_argument('--headless')
            # chrome_options.add_extension(self.local_path_UBExtension)
            chrome_options.add_argument('ignore-certificate-errors')

        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size={width}, {height}'.format(width=width, height=height))
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_experimental_option("prefs", profile)

        return webdriver.WebDriver(options=chrome_options, desired_capabilities=capabilities,
                                   executable_path=self.get_executable_path())

    def desktop_browser(self, source):
        browser = self.set_chrome()
        if func.get_host_name() != REMOTE_SERVER:
            browser.maximize_window()
        browser.get(source)
        return browser


driver = SettingsBrowser().desktop_browser('https://test.minjust.gov.ua/commission_civil_register')
driver.implicitly_wait(1.5)
iframe = driver.find_element(By.CSS_SELECTOR, 'iframe')
driver.switch_to.frame(iframe)
zvernenja = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Шукати"]')
driver.implicitly_wait(0.5)
zvernenja.send_keys("12345")
