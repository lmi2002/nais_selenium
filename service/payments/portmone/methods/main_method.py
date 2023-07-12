import time

from service.payments.portmone.pages.main_page import PortmoneMainPage


class PortmoneMainMethod:
    def payment_on_site(self, browser, number=None):
        PortmoneMainPage().check_title_portmone(browser)
        PortmoneMainPage().insert_field_number_card(browser)
        PortmoneMainPage().insert_field_exp_date_card(browser)
        PortmoneMainPage().insert_field_cvv2_card(browser)
        PortmoneMainPage().insert_field_email(browser)
        PortmoneMainPage().click_btn_payment(browser)
        time.sleep(1)
        # PortmoneMainPage().check_text_present_in_total_amount(browser, '33.00')
        PortmoneMainPage().click_btn_payment_confirm(browser)
        # PortmoneMainPage().check_current_url(browser, number)