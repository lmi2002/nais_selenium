from selenium.webdriver.common.by import By


class ErkMainLocator:
    desktop_select_button = (By.CLASS_NAME, 'desktop-select-button')
    desktop_select_button_users = (
        By.XPATH,
        '//div[contains(@class, "desktop-select-button")]//span[contains(text(), "Реєстр користувачів")]')
    u_desktop_drawer_item_title = (By.CLASS_NAME, 'u-desktop-drawer__item__title')
    label_search = (By.XPATH, '//span[text()="Пошук"]/..')
    label_search_is_opened = (By.CSS_SELECTOR, '.el-submenu.is-opened')
    sublabel_company = (By.XPATH, '//ul/li[contains(@role,"menuitem")]/span[text()="Організації"]')
    label_operations = (By.XPATH, '//ul/li[contains(@role,"menuitem")]//span[text()="Операції"]')
    sublabel_employee = (By.XPATH, '//ul/li[contains(@role,"menuitem")]/span[text()="Співробітники"]')
    sublabel_user = (By.XPATH, '//ul/li[contains(@role,"menuitem")]/span[text()="Користувачі"]')
    sublabel_search_statement = (By.XPATH, '//ul/li[contains(@role,"menuitem")]/span[text()="Заявки"]')
    close_tab_admin = (By.CSS_SELECTOR, '.u-navbar__tab-close-button')