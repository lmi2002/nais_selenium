from selenium.webdriver.common.by import By


class DrrpStatementLocator:

    main_menu_statement = (By.XPATH, '//span[text()="Реєстрація та обробка заяв"]/..')
    sub_menu_create_statement = (By.XPATH, '//span[text()="Реєстрація заяви"]')
    sub_sub_menu_statement_ownership = (By.XPATH, '//span[text()="заява про реєстрацію права власності"]/..')
    sub_sub_menu_statement = {
        # "ownership": (By.XPATH, '//span[text()="заява про реєстрацію права власності"]/..'),
        "irp": (By.XPATH, '//span[text()="заява про реєстрацію іншого речового права"]/..'),
        # "encumbrances": (By.XPATH, '//span[text()="заява про реєстрацію обтяження"]/..'),
        # "relinquishment_of_property": (By.XPATH, '//span[text()="заява про відмову від речового права"]/..')
    }
    block_common_info = (By.XPATH, '//span[text()="Відомості"]/..')
    kind_registration = (By.CSS_SELECTOR, 'input[name$="EntityChangeTypeBit"]')
    kind_registration_list = (By.XPATH, '//ul/li[text()="виникнення"]')
    num_ownership = (By.CSS_SELECTOR, 'input[name="enum"]')
    form_ownership = (By.CSS_SELECTOR, 'input[name$="PrType"]')
    form_ownership_list = (By.XPATH, '//ul/li[text()="приватна"]')
    kind_common_ownership = (By.CSS_SELECTOR, 'input[name$="CommonKind"]')
    kind_common_ownership_list = (By.XPATH, '//ul/li[text()="спільна сумісна"]')
    block_add_onm = (By.XPATH, '//span[text()="Додати ОНМ"]/..')
    type_onm = (By.CSS_SELECTOR, 'input[name$="ReType"]')
    type_onm_list = (By.XPATH, '//ul/li[text()="квартира"]')
    addition_of_type_onm = (By.CSS_SELECTOR, 'input[name$="TypeExtension"]')
    subtype_onm = (By.CSS_SELECTOR, 'input[name$="ReSubType"]')
    subtype_onm_list = (By.XPATH, '//ul/li[text()="інше"]')
    addition_of_subtype_onm = (By.CSS_SELECTOR, 'input[name$="SubTypeExtension"]')
    description_onm = (By.CSS_SELECTOR, 'textarea[name="description"]')
    block_add_address_onm = (By.XPATH, '//span[text()="Додати адресу ОНМ"]/..')
    address_onm_locality = (By.CSS_SELECTOR, 'input[name="ATU_ATU_ID"]')
    address_onm_locality_list = (By.CSS_SELECTOR, '.combo-search-match')
    address_onm_street = (By.CSS_SELECTOR, 'input[name="streetName"]')
    address_onm_street_list = (By.XPATH, '//ul/li/span[text()="Палладіна"]')
    house_type = (By.CSS_SELECTOR, 'input[name$="HouseType"]')
    building_type = (By.CSS_SELECTOR, 'input[name$="BuildingType"]')
    house_type_list = (By.XPATH, '//ul/li/span[text()="будинок"]/..')
    house_num = (By.CSS_SELECTOR, 'input[name="house"]')
    building_type_list = (By.XPATH, '//ul/li/span[text()="корп."]')
    building_num = (By.CSS_SELECTOR, 'input[name="building"]')
    object_num_type = (By.CSS_SELECTOR, 'input[name$="ObjectNumType"]')
    object_num_type_list = (By.XPATH, '//ul/li/span[text()="квартира"]')
    object_num = (By.CSS_SELECTOR, 'input[name="objectNum"]')
    addition_of_address_onm = (By.CSS_SELECTOR, 'textarea[name="additional"]')
    person_type = (By.XPATH, '//span[text()="Фізична особа"]/..')
    person_rule = (By.CSS_SELECTOR, 'input[name$="SbjRlNameBit"]')
    person_rule_list = (By.XPATH, '//ul/li[text()="Заявник"]')
    person_name = (By.CSS_SELECTOR, 'input[name="sbjName"]')
    person_code = (By.CSS_SELECTOR, 'input[name="sbjCode"]')
    person_phone = (By.CSS_SELECTOR, 'input[name="phone"]')
    passport_series = (By.CSS_SELECTOR, 'input[name="passportSeriesNum"]')
    passport_date = (By.CSS_SELECTOR, 'input[name="docDate"]')
    passport_publisher = (By.CSS_SELECTOR, 'input[name="publisher"]')
    addition_of_person = (By.CSS_SELECTOR, 'textarea[name="additional"]')
    payment_type = (By.CSS_SELECTOR, 'input[name$="PayType"]')
    payment_type_list = (By.XPATH, '//ul/li[text()="Адміністративний збір за реєстраційні дії"]')
    payment_num = (By.CSS_SELECTOR, 'input[name="enum"]')
    payment_date = (By.CSS_SELECTOR, 'input[name$="rpdDate"]')
    payment_summ = (By.CSS_SELECTOR, 'input[name="summ"]')
    org_name = (By.CSS_SELECTOR, 'input[name="orgName"]')
    block_payment_btn_admit = (By.XPATH, '//span[text()="Застосувати"]')
    document_type = (By.CSS_SELECTOR, 'input[name$="CdType"]')
    document_type_list = (By.XPATH, '//span[text()="договір іпотеки"]')
    addition_document_type = (By.CSS_SELECTOR, 'input[name="cdTypeExtension"]')
    document_num = (By.CSS_SELECTOR, 'input[name="enum"]')
    document_date = (By.CSS_SELECTOR, 'input[name="docDate"]')
    document_publisher = (By.CSS_SELECTOR, 'input[name="publisher"]')
    document_count_page = (By.CSS_SELECTOR, 'input[name="countPages"]')
    statement_num = (By.CSS_SELECTOR, 'input[name="outNum"]')
    statement_date = (By.CSS_SELECTOR, 'input[name="outDate"]')
    statement_term_review = (By.CSS_SELECTOR, 'input[name$="TermReview"]')
    statement_term_review_list = (By.XPATH, '//ul/li[text()="2 робочі дні"]')
    statement_receive_type = (By.CSS_SELECTOR, 'input[name$="DocReceiveType"]')
    statement_receive_type_list = (By.XPATH, '//ul/li[text()="особисто"]')
    addition_of_statement = (By.CSS_SELECTOR, 'textarea[name="additional"]')
    ubdocument = (By.CSS_SELECTOR, 'div[id^="ubdocument"]')