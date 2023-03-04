from settings.setting_project import project_rule, PROJECT, RULE

passw = project_rule.get('drrp').get('gov_reg').get('passw')
username = project_rule.get('drrp').get('gov_reg').get('username')
key_path = project_rule.get('drrp').get('gov_reg').get('key_path')
passw_key = project_rule.get('drrp').get('gov_reg').get('passw_key')
certificate = project_rule.get('drrp').get('gov_reg').get('certificate')
message_text_invalid_cert_login_passw = ['В доступі відмовлено. Невірний сертифікат, логін або пароль',
                                         'Сертифікат не знайдено']

data_auth_test = {

    "test_valid_login_passw": {
        "username": username,
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key,
        "certificate": certificate
    },
    "test_empty_fields_login_passw": {
        "username": "",
        "passw": ""
    },
    "test_empty_login": {
        "username": "",
        "passw": passw
    },
    "test_empty_passw": {
        "username": username,
        "passw": ""
    },
    "test_invalid_login_passw": {
        "username": passw,
        "passw": username,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_empty_fields_second_level": {
        "username": username,
        "passw": passw
    },
    "test_invalid_type_device": {
        "username": username,
        "passw": passw,
        "num_elem": 8
    },
    "test_invalid_key": {
        "username": username,
        "passw": passw,
        "key_path": project_rule['drrp']['gov_reg']['key_path'],
        "passw_key": passw_key
    },
    "test_invalid_passw_key": {
        "username": username,
        "passw": passw,
        "key_path": key_path,
        "passw_key": 987654321
    },
    "test_spec_char_in_login": {
        "username": r'«»‘~!@#$%^&*()?>',
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_spec_char_in_passw": {
        "username": username,
        "passw": r'«»‘~!@#$%^&*()?>',
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_space_char_in_login": {
        "username": '    ',
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_space_char_in_passw": {
        "username": username,
        "passw": '    ',
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_space_char_in_text_login": {
        "username": '{spaces}{username}{spaces}'.format(spaces='  ', username=username),
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_space_char_in_text_passw": {
        "username": username,
        "passw": '{spaces}{passw}{spaces}'.format(spaces='  ', passw=passw),
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_xss_in_login": {
        "username": '<script>alert(123)</script>',
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_html_tags_in_login": {
        "username": '<form action=»http://live.hh.ru»><input type=»submit»></form>',
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_sql_in_login": {
        "username": '‘ or ‘a’ = ‘a’; DROP TABLE user; SELECT * FROM blog WHERE code LIKE ‘a%’;',
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },

    "test_back_page": {
        "username": username,
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_user_session_mode_singleton": {
        "username": username,
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key,
        "host": 'https://ub-srv-51.test.nais.gov.ua/',
        "certificate": certificate
    },
    "test_user_session_mode_displacing": {
        "username": username,
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key,
        "host": 'https://ub-srv-52.test.nais.gov.ua/',
        "certificate": certificate
    },

}
