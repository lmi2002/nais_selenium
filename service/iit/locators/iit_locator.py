from selenium.webdriver.common.by import By


class IitLocator:
    website_url = (By.ID, 'TrustedWebSiteURL')
    btn_add = (By.ID, 'AddTrustedWebSiteURL')
    btn_save = (By.ID, 'SaveTrustedSites')
    btn_set = (By.CSS_SELECTOR, 'div[aria-label="Установить"]')