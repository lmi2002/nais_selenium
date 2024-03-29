import json
import allure
import requests
import pytest



@allure.severity(allure.severity_level.NORMAL)
class TestApiGetDoc:
    path = 'https://register.test.nais.gov.ua/ubql'

    authorization = 'UB db2dc90162581aad78761bc0'  # Авторизируемся и берем в заголовке Authorization
    accept = 'application/json, text/plain, */*'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    content_type = 'application/json;charset=UTF-8'
    origin = 'https://register.test.nais.gov.ua'
    accept_language = 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'

    headers = {
        'accept': accept,
        'authorization': authorization,
        'user-agent': user_agent,
        'content-type': content_type,
        'origin': origin,
        'accept-language': accept_language
    }

    def post_response(self, data):
        return requests.post(self.path, headers=self.headers, data=json.dumps(data))

    def get_response(self, url, data):
        return requests.get(url, headers=self.headers, params=data, stream=True)

    # Головне меню → Користування інформацією → Інформаційна довідка з РРП за об’єктом

    def test_get_infospravka_object(self):
        data_generate = [{
            "entity": "rrpUb_infoRrp",
            "method": "generate",
            "searchParams": {
                "isShowHistoricalNames": False,
                "searchType": "1",
                "reason": "autotest",
                "isSuspend": False,
                "dcReqtypeSubject": "4",
                "objectSearchInfo": {
                    "realtyRnNum": "565864580000"
                },
                "employeeId": 25213
            }
        }]

        response_generate = self.post_response(data_generate)
        assert response_generate.status_code == 200
        result_data = response_generate.json()[0].get('resultData')
        report_result_id = json.loads(result_data).get('reportResultID')

        data_select = [{
            "entity": "rep_reportResult",
            "fieldList": [
                "generatedDocument",
                "ID",
                "mi_modifyDate",
                "erc_userID"
            ],
            "ID": report_result_id,
            "method": "select"
        }]

        response_select = self.post_response(data_select)
        assert response_select.status_code == 200

        url = 'https://register.test.nais.gov.ua/getDocument'

        data_get_doc_pdf = {"entity": "rep_reportResult",
                            "attribute": "generatedDocument",
                            "ID": report_result_id,
                            "store": "reportsLU",
                            "origName": '{report_result_id}{pdf}'.format(report_result_id=str(report_result_id),
                                                                         pdf='.pdf'),
                            "filename": 'rep_reportResult{report_result_id}generatedDocument'.format(
                                report_result_id=str(report_result_id)),
                            "_rc": 1
                            }

        response_get_doc_pdf = self.get_response(url, data_get_doc_pdf)
        assert response_get_doc_pdf.status_code == 200
