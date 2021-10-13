from settings.setting_project import project_rule, PROJECT, RULE

passw = project_rule[PROJECT][RULE]['passw']
login = project_rule[PROJECT][RULE]['login']
key_path = project_rule[PROJECT][RULE]['key_path']
passw_key = project_rule[PROJECT][RULE]['passw_key']
message_text_invalid_cert_login_passw = 'В доступі відмовлено. Невірний сертифікат, логін або пароль'

data_auth_test = {

    "test_valid_login_passw": {
        "login": login,
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_empty_fields_login_passw": {
        "login": "",
        "passw": ""
    },
    "test_empty_login": {
        "login": "",
        "passw": passw
    },
    "test_empty_passw": {
        "login": login,
        "passw": ""
    },
    "test_invalid_login_passw": {
        "login": passw,
        "passw": login,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_empty_fields_second_level": {
        "login": login,
        "passw": passw
    },
    "test_invalid_type_device": {
        "login": login,
        "passw": passw,
        "num_elem": 8
    },
    "test_invalid_key": {
        "login": login,
        "passw": passw,
        "key_path": project_rule['drrp']['gov_reg']['key_path'],
        "passw_key": passw_key
    },
    "test_invalid_passw_key": {
        "login": login,
        "passw": passw,
        "key_path": key_path,
        "passw_key": 987654321
    },
    "test_spec_char_in_login": {
        "login": r'«»‘~!@#$%^&*()?>',
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_spec_char_in_passw": {
        "login": login,
        "passw": r'«»‘~!@#$%^&*()?>',
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_space_char_in_login": {
        "login": '    ',
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_space_char_in_passw": {
        "login": login,
        "passw": '    ',
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_space_char_in_text_login": {
        "login": '{spaces}{login}{spaces}'.format(spaces='  ', login=login),
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_space_char_in_text_passw": {
        "login": login,
        "passw": '{spaces}{passw}{spaces}'.format(spaces='  ', passw=passw),
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_xss_in_login": {
        "login": '<script>alert(123)</script>',
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_html_tags_in_login": {
        "login": '<form action=»http://live.hh.ru»><input type=»submit»></form>',
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },
    "test_sql_in_login": {
        "login": '‘ or ‘a’ = ‘a’; DROP TABLE user; SELECT * FROM blog WHERE code LIKE ‘a%’;',
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },

    "test_back_page": {
        "login": login,
        "passw": passw,
        "key_path": key_path,
        "passw_key": passw_key
    },

}