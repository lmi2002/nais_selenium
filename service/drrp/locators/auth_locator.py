from selenium.webdriver.common.by import By


class DrrpAuthLocator:

    user = (By.TAG_NAME, 'input')
    passw = (By.TAG_NAME, 'input')
    entry = (By.XPATH, '//span[text()="Продовжити"]/..')
    client_login_form = (By.ID, 'extClientLoginForm-body')
    input_type_key = (By.CSS_SELECTOR, 'input[placeholder="Оберіть тип носія"]')
    type_key_block = (By.CLASS_NAME,  'el-scrollbar__view, el-select-dropdown__list')
    type_key_list = (By.CLASS_NAME, 'el-select-dropdown__item')
    input_select_file = (By.CSS_SELECTOR, 'input[type="file"]')
    input_passw = (By.CSS_SELECTOR, 'input[type="password"]')
    btn_load = (By.XPATH, '//button/span[text()="Завантажити"]/..')
    button_is_disabled = (By.CSS_SELECTOR, 'button.is-disabled')
    v_modal = (By.CLASS_NAME, "v-modal")
    div_is_focus = (By.CLASS_NAME, "is-focus")
    li_hover = (By.CLASS_NAME, "hover")

