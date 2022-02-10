from selenium.webdriver.common.by import By


class AuthLocator:

    user = (By.TAG_NAME, 'input')
    passw = (By.TAG_NAME, 'input')
    entry = (By.XPATH, '//span[text()="Продовжити"]/..')
    input_type_key = (By.CSS_SELECTOR, 'input[placeholder="Оберіть тип носія"]')
    type_key_list = (By.CLASS_NAME, 'el-select-dropdown__item')
    input_select_file = (By.CSS_SELECTOR, 'input[type="file"]')
    input_passw = (By.CSS_SELECTOR, 'input[type="password"]')
    btn_load = (By.XPATH, '//button/span[text()="Завантажити"]/..')
    button_is_disabled = (By.CSS_SELECTOR, 'button.is-disabled')
    v_modal = (By.CLASS_NAME, "v-modal")
    div_is_focus = (By.CLASS_NAME, "is-focus")
    li_hover = (By.CLASS_NAME, "hover")
    el_popup_parent_hidden = (By.CLASS_NAME,'el-popup-parent--hidden')
    ub_dialog_break_word = (By.CLASS_NAME,'ub-dialog_break-word')
    client_login_form = (By.CLASS_NAME, 'auth-page__container')
    el_form_item_error = (By.CLASS_NAME, 'el-form-item__error')
    el_select_dropdown_empty = (By.CLASS_NAME, 'el-select-dropdown__empty')
    type_key_list_1 = (By.CSS_SELECTOR, '.el-scrollbar__view.el-select-dropdown__list')
    btn_OK_install = (By.XPATH, '//*[contains(text(),"Ок")]/..')
    form_select_certificate = (By.XPATH, '//span[text()="Оберіть АЦСК"]/..')
    input_selected_acsk = (By.CSS_SELECTOR, 'input[placeholder="Оберіть АЦСК"]')
    form_select_certificate_file = (By.XPATH, '//span[text()="Виберіть файли сертифікатів"]/..')
