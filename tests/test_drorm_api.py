import json
import pytest

import allure
import requests

from api.drorm.response_template import response_searchExtract, response_getLimitation
from settings.setting_api import SettingDrormApi
from settings.setting_drorm_api_data import searchExtract, sort_searchParams, getLimitation


@allure.severity(allure.severity_level.NORMAL)
class TestDrormApi(SettingDrormApi):

    def post_response(self, data):
        return requests.post(SettingDrormApi.path, headers=SettingDrormApi.headers, data=json.dumps(data))

    def get_response(self, res):
        requests.get(res)

    @pytest.mark.api
    @pytest.mark.parametrize('name, data', searchExtract.items())
    def test_searchExtract(self, name, data):
        data = data

        # import pdb;
        # pdb.set_trace()

        response = self.post_response(data)
        assert response.status_code == 200
        if name in sort_searchParams:
            if name != 'sbjCode_19390819':
                jsn = json.loads(response.json()[0].get('resultData'))
                jsn.sort(key=lambda x: x['opOpID'])

                jsn_template = json.loads(response_searchExtract[name])
                jsn_template.sort(key=lambda x: x['opOpID'])

                assert json.dumps(jsn) == json.dumps(jsn_template)

        else:
            assert response.json()[0].get('resultData') == response_searchExtract[name]

    @pytest.mark.api
    @pytest.mark.parametrize('name, data', getLimitation.items())
    def test_getLimitation(self, name, data):
        data = data

        response = self.post_response(data)
        assert response.status_code == 200
        assert response.json()[0].get('resultData') == response_getLimitation[name]
