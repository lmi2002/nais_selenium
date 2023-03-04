#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class DrrpQueueStatementLocator:
    x_column_header_trigger = (By.CSS_SELECTOR, '.x-column-header-trigger')
    sort_desc = (By.XPATH, '//a/span[text()="Сортувати за спаданням"]')
    result_el_st = (By.CSS_SELECTOR, 'table tbody tr')
    col_account_number = (By.CSS_SELECTOR, 'div[data-qtip="Обліковий номер"]')
