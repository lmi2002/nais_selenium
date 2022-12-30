import json
import re
import os

import allure
import requests
import pytest

from helpers.func import get_text_from_csv, text_to_csv
from settings.setting_drrp_api_data import ac_name


@allure.severity(allure.severity_level.NORMAL)
class TestApiCheckDecisionReason:
    # path = 'https://register.test.nais.gov.ua/ubql'  # Тестовое окружение
    path = 'https://ernb.dev.nais.gov.ua/ubql'  # Дев окружение
    term_review_date = '2022-05-18T13:06:00.000Z'

    authorization = 'CERT2 83e464006283a6d2ac1e1d61'  # Авторизируемся и берем в заголовке Authorization
    accept = 'application/json, text/plain, */*'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    content_type = 'application/json;charset=UTF-8'
    accept_language = 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'

    headers = {
        'accept': accept,
        'authorization': authorization,
        'user-agent': user_agent,
        'content-type': content_type,
        'accept-language': accept_language
    }

    def post_response(self, data):
        return requests.post(self.path, headers=self.headers, data=json.dumps(data))

    def get_response(self, res):
        requests.get(res)

    csv_file = os.path.abspath('../decision.csv')
    data_from_csv = get_text_from_csv(csv_file)
    result_file = os.path.abspath('../result.csv')

    @pytest.mark.parametrize('ac_name, ac_name_ukr', ac_name.items())
    @pytest.mark.parametrize('row', data_from_csv)
    def test_check_decision_reason(self, ac_name, ac_name_ukr, row):
        result = []
        st_num, st_status, st_name, decision_num, decision_name, decision_status = row[0], row[1], row[2], row[3], row[
            4], row[5]
        data = [
            {
                "entity": "rrpUb_decisionCard",
                "method": "selectDecisionReason",
                "instance": {
                    "regNum": decision_num,
                    "acName": ac_name,
                    "entityRnNum": None,
                    "limitationID": None,
                    "options": {
                        "isBond": False
                    }
                },
                "formShortcutCode": "NOTAR_RRP_REALTY_CREATE",
                "privCode": "NOTAR_DECISION_OPERATIONS_VIEW"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        message_title = response.json()[0].get('messageTitle')
        message_text = response.json()[0].get('messageText')
        result.append([ac_name, ac_name_ukr, st_num, st_status, st_name, decision_num, decision_name, decision_status,
                       message_title, message_text])
        text_to_csv(self.result_file, result)
