import pytest

from settings.setting_rule_user import users


@pytest.fixture(scope='session')
def get_user():
    for k in users.keys():
        yield users[k]['login'], users[k]['passw']
