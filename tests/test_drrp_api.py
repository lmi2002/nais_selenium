import json

import pytest

import allure
import requests

from api.drrp.response_template import response_rrpExch_external, exceptions_rrpExch_external
from settings.setting_api import SettingDrrpmApi
from settings.setting_drrp_api_data import rrpExch_external


@allure.severity(allure.severity_level.NORMAL)
class TestDrrpmApi(SettingDrrpmApi):

    def post_response(self, data):
        return requests.post(self.path, headers=SettingDrrpmApi.headers, data=json.dumps(data))

    def get_response(self, res):
        requests.get(res)

    @pytest.mark.api
    @pytest.mark.parametrize('name, data', rrpExch_external.items())
    def test_rrpExch_external(self, name, data):
        data = json.loads(data)

        response = self.post_response(data)
        assert response.status_code == 200

        if name != 'cad_num_limit_SpR':
            if name in exceptions_rrpExch_external:
                if type(response_rrpExch_external[name]) == 'list':
                    for resp_snap in response_rrpExch_external[name]:
                        assert resp_snap in response.json()[0].get('resultData')
            elif name == 'getActualAtuID':
                assert response.json() == json.loads(response_rrpExch_external[name])
            else:
                assert response.json()[0].get('resultData') == response_rrpExch_external[name]
