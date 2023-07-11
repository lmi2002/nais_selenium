from service.iit.pages.iit_page import IitPage


class IitMethod(IitPage):
    path_settings_iit = 'chrome-extension://jffafkigfgmjafhpkoibhfefeaebmccg/views/settings/settings.html'

    path_UBExtension = 'https://chrome.google.com/webstore/detail/ііт-користувач-цск-1-бібл/' \
                       'jffafkigfgmjafhpkoibhfefeaebmccg/'

    def setting_extension_iit(self, driver, url_project):
        driver.get(self.path_settings_iit)
        self.insert_value_website_url(driver, url_project)
        self.click_btn_add(driver)
        self.click_btn_save(driver)
        self.click_alert(driver)

    def load_extension_iit(self, driver):
        driver.get(self.path_UBExtension)
        self.click_btn_set(driver)
