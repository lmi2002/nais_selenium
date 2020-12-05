from settings.setting_data_info import data_info

onm_dict = {
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