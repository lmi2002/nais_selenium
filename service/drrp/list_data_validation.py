from settings.setting_data_info import data_info

statement_validation_second = (
    data_info['statement']['statement_num'], data_info['statement']['statement_date'],
    data_info['payment']['payment_summ'],
    data_info['payment']['payment_num']
)

person_validation = (
    'Фізична особа {person_name} код: {person_code}'.format(person_name=data_info['person']['person_name'],
                                                            person_code=data_info['person']['person_code']),
    'Громадянство: Україна паспорт громадянина України: {passport_series} {passport_date} р. ' \
    'видавник {passport_publisher}'.format(
        passport_series=data_info['person']['passport_series'],
        passport_date=data_info['person']['passport_date'],
        passport_publisher=data_info['person']['passport_publisher']),
    'Наявна уповн. особа: ні Телефон/email: {person_phone} Додаткові відомості: {addition_of_person}'.format(
        person_phone=data_info['person']['person_phone'], addition_of_person=data_info['person']['addition_of_person'])
)

onm_validation = {
    "ownership": [
        "Тип права власності: {type_ownership}".format(type_ownership=data_info['onm']['type_ownership']),
        "Вид реєстрації: {kind_registration}".format(kind_registration=data_info['onm']['kind_registration']),
        ". Номер запису про право власності: {num_ownership}".format(
            num_ownership=data_info['common_info']['num_ownership']),
        "Форма права власності: {form_ownership}".format(form_ownership=data_info['onm']['form_ownership']),
        "; вид спільної власності: {kind_common_ownership}".format(
            kind_common_ownership=data_info['onm']['kind_common_ownership']),
        "Тип ОНМ: {object_num_type}, доповнення до типу: {addition_of_type_onm} підтип ОНМ: {subtype_onm}, " \
        "доповнення до підтипу: {addition_of_subtype_onm} Реєстраційний номер ОНМ: {onm_num_ownership}".format(
            object_num_type=data_info['address_onm']['object_num_type'],
            addition_of_type_onm=data_info['onm']['addition_of_type_onm'],
            subtype_onm=data_info['onm']['subtype_onm'],
            addition_of_subtype_onm=data_info['onm']['addition_of_subtype_onm'],
            onm_num_ownership=data_info['onm']['onm_num_ownership']),
        "Опис ОНМ: {description_onm}".format(description_onm=data_info['onm']['description_onm'])
    ],
    "irp": [
        "Вид реєстрації: {kind_registration}".format(kind_registration=data_info['onm']['kind_registration']),
        ". Номер запису про інше речове право: {num_ownership}".format(
            num_ownership=data_info['common_info']['num_ownership']),
        "Вид іншого речового права: {type_irp} доповнення до виду: {addition_of_type}".format(
            type_irp=data_info['onm']['type_irp'], addition_of_type=data_info['common_info']['addition_of_type']),
        "Тип ОНМ: {object_num_type}, доповнення до типу: {addition_of_type_onm} підтип ОНМ: {subtype_onm}, " \
        "доповнення до підтипу: {addition_of_subtype_onm} Реєстраційний номер ОНМ: {onm_num_ownership}".format(
            object_num_type=data_info['address_onm']['object_num_type'],
            addition_of_type_onm=data_info['onm']['addition_of_type_onm'],
            subtype_onm=data_info['onm']['subtype_onm'],
            addition_of_subtype_onm=data_info['onm']['addition_of_subtype_onm'],
            onm_num_ownership=data_info['onm']['onm_num_ownership']),
        "Опис ОНМ: {description_onm}".format(description_onm=data_info['onm']['description_onm'])
    ],
    "encumbrances": [
        "Тип ОНМ: {object_num_type}, доповнення до типу: {addition_of_type_onm} підтип ОНМ: {subtype_onm}, " \
        "доповнення до підтипу: {addition_of_subtype_onm} Реєстраційний номер ОНМ: {onm_num_ownership}".format(
            object_num_type=data_info['address_onm']['object_num_type'],
            addition_of_type_onm=data_info['onm']['addition_of_type_onm'],
            subtype_onm=data_info['onm']['subtype_onm'],
            addition_of_subtype_onm=data_info['onm']['addition_of_subtype_onm'],
            onm_num_ownership=data_info['onm']['onm_num_ownership']),
        "Опис ОНМ: {description_onm}".format(description_onm=data_info['onm']['description_onm'])
    ],
    "relinquishment_of_property": [
        "Тип ОНМ: {object_num_type}, доповнення до типу: {addition_of_type_onm} підтип ОНМ: {subtype_onm}, " \
        "доповнення до підтипу: {addition_of_subtype_onm} Реєстраційний номер ОНМ: {onm_num_ownership}".format(
            object_num_type=data_info['address_onm']['object_num_type'],
            addition_of_type_onm=data_info['onm']['addition_of_type_onm'],
            subtype_onm=data_info['onm']['subtype_onm'],
            addition_of_subtype_onm=data_info['onm']['addition_of_subtype_onm'],
            onm_num_ownership=data_info['onm']['onm_num_ownership']),
        "Опис ОНМ: {description_onm}".format(description_onm=data_info['onm']['description_onm'])
    ]
}

address_onm_validation = (
    'м.{address_onm_locality}, вулиця {address_onm_street}, {house_type} {house_num}, {building_type} {building_num}, ' \
    '{object_num_type} {object_num}'.format(address_onm_locality=data_info['address_onm']['address_onm_locality'],
                                            address_onm_street=data_info['address_onm']['address_onm_street'],
                                            house_type=data_info['address_onm']['house_type'],
                                            house_num=data_info['address_onm']['house_num'],
                                            building_type=data_info['address_onm']['building_type'],
                                            building_num=data_info['address_onm']['building_num'],
                                            object_num_type=data_info['address_onm']['object_num_type'],
                                            object_num=data_info['address_onm']['object_num']),

    'Додаткові відомості: {addition_of_address_onm}'.format(
        addition_of_address_onm=data_info['address_onm']['addition_of_address_onm'])
)

decision_validation = [

]



