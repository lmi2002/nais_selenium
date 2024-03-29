import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from settings.setting_allure import SettingAllure

from exception import *

timeout = 100
delay = 1

sa = SettingAllure()


def wait(driver):
    return WebDriverWait(driver, timeout)


def get_web_element(driver, item):
    try:
        return wait(driver).until(expected_conditions.presence_of_element_located(item))
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise ElementNotFoundException(item, e)

def get_web_elements(driver, item):
    try:
        return wait(driver).until(expected_conditions.presence_of_all_elements_located(item))
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise ElementNotFoundException(item, e)


def get_visible_element(driver, item):
    try:
        return wait(driver).until(expected_conditions.visibility_of_element_located(item))
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise ElementNotFoundException(item, e)


def check_invisible_element(driver, item):
    try:
        return wait(driver).until(expected_conditions.invisibility_of_element_located(item))
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise ElementVisibleException(item, e)


def get_visible_elements(driver, item):
    try:
        return wait(driver).until(expected_conditions.visibility_of_any_elements_located(item))
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise ElementNotFoundException(item, e)


def alert_accept(driver):
    try:
        wait(driver).until(expected_conditions.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise AlertNotFoundException('Alert,', e)


def check_text_present_in_element(driver, item, text):
    try:
        wait(driver).until(expected_conditions.text_to_be_present_in_element(item, text))
        return driver.find_element(*item)
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise TextNotFoundException(item, text, e)

def check_text_present_in_element_b(driver, item, text):
    """
        Method return type bool
    """
    try:
        wait(driver).until(expected_conditions.text_to_be_present_in_element(item, text))
        return True
    except TimeoutException as e:
        return False


def check_value_present_in_element(driver, item, value):
    try:
        wait(driver).until(expected_conditions.text_to_be_present_in_element_value(item, value))
        return driver.find_element(*item)
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise ValueNotFoundException(item, value, e)


def get_clickable_element(driver, item):
    try:
        return wait(driver).until(expected_conditions.element_to_be_clickable(item))
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise ElementVisibleException(item, e)


def locate(item):
    # delay_test()
    return get_web_element(item)


def click(driver, item, delay=None):
    try:
        element = wait(driver).until(expected_conditions.element_to_be_clickable(item))
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise ElementNotFoundException(item, e)

    element.click()
    # delay_test(delay=delay)
    return element


def title_contains(driver, text):
    try:
        item = 'title'
        wait(driver).until(expected_conditions.title_contains(text))
        return driver.title
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise TextNotFoundException(item, text, e)


def title_is(driver, text):
    try:
        item = 'title'
        wait(driver).until(expected_conditions.title_is(text))
        return driver.title
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise TextNotFoundException(item, text, e)


def state_load_page(driver):
    return driver.execute_script("return document.readyState")

def create_window(driver):
    return driver.execute_script("window.open('');")

def get_windows(driver):
    return driver.window_handles

def switch_to_window(driver, index=None):
    if index is None:
        win = get_windows(driver)[0]
        driver.switch_to.window(win)
    else:
        win = get_windows(driver)[index]
        driver.switch_to.window(win)

def scroll_to_element(driver, item):
    try:
        ActionChains(driver).move_to_element(driver.find_element(*item)).perform()
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise ElementNotFoundException(item, e)


def select_value(driver, item, value):
    try:
        Select(driver).select_by_value(driver.find_element(*item)).select_by_value(value)
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise ElementNotFoundException(item, e)


def select_index(driver, item, index):
    try:
        select_element = driver.find_element(*item)
        time.sleep(2)
        Select(select_element).select_by_index(index)
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise ElementNotFoundException(item, e)


def get_element_present_text(driver, text):
    locator = (By.XPATH, '//*[text()="{text}"]'.format(text=text))
    try:
        return get_web_element(driver, locator)
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise TextNotFoundException(locator, text, e)


def get_elements_present_text(driver, text):
    locator = (By.XPATH, '//*[text()="{text}"]'.format(text=text))
    try:
        return get_web_elements(driver, locator)
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise TextNotFoundException(locator, text, e)


def get_element_containing_text(driver, text):
    locator = (By.XPATH, '//*[contains(text(), "{text}")]'.format(text=text))
    try:
        return get_web_element(driver, locator)
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise TextNotFoundException(locator, text, e)


def get_next_element_present_text(driver, text):
    locator = (By.XPATH, '//*[text()="{text}"]/following-sibling::*'.format(text=text))
    try:
        return get_web_elements(driver, locator)[0]
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise TextNotFoundException(locator, text, e)


def get_node_element_present_text(driver, text):
    locator = (By.XPATH, '//*[node()="{text}"]'.format(text=text))
    try:
        return get_web_elements(driver, locator)[0]
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise TextNotFoundException(locator, text, e)


def get_elements_containing_text(driver, text):
    locator = (By.XPATH, '//*[contains(text(), "{text}")]'.format(text=text))
    try:
        return get_web_elements(driver, locator)
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise TextNotFoundException(locator, text, e)


def get_current_url(driver):
    return driver.current_url


def move_to_element(driver, item):
    try:
        elem = get_web_element(driver, item)
        ActionChains(driver).move_to_element(elem).perform()
    except ElementNotInteractableException as e:
        sa.create_screenshot(driver)
        raise ElementNotInteractableException(item, e)


def move_to_element_and_click(driver, item, index=None):
    try:
        if index is None:
            elem = get_web_element(driver, item)
        else:
            elem = get_web_elements(driver, item)[index]
        ActionChains(driver).move_to_element(elem).click().perform()
        return elem
    except ElementNotInteractableException as e:
        sa.create_screenshot(driver)
        raise ElementNotInteractableException(item, e)


def double_click_element(driver, item):
    elem = get_web_element(driver, item)
    ActionChains(driver).double_click(elem).perform()


def get_elements_locator(driver, locator):
    locator = locator
    try:
        return get_web_elements(driver, locator)
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise TextNotFoundException(locator, e)


def get_element_locator(driver, locator):
    locator = locator
    try:
        return get_web_element(driver, locator)
    except TimeoutException as e:
        sa.create_screenshot(driver)
        raise TextNotFoundException(locator, e)


def refresh_page(driver):
    driver.refresh()


