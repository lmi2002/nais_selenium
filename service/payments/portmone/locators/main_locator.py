from selenium.webdriver.common.by import By


class PortmoneMainLocator:

    field_number_card = (By.CSS_SELECTOR, 'input[id="single_portmone_pay_card"]')
    field_exp_date_card = (By.CSS_SELECTOR, 'input[id="single_portmone_pay_exp_date"]')
    field_cvv2_card = (By.CSS_SELECTOR, 'input[id="single_portmone_pay_cvv2"]')
    field_email = (By.CSS_SELECTOR, 'input[name="emailAddress"]')
    btn_payment = (By.CSS_SELECTOR, 'button[data-action="cardPaymentInvoice"]')
    btn_payment_confirm = (By.CSS_SELECTOR, 'button[data-action="paymentConfirm"]')
    total_amount = (By.CSS_SELECTOR, 'span[id="totalAmount"]')