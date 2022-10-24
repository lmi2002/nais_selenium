import json
from locust import HttpUser, task, events, SequentialTaskSet
from locust import task, FastHttpUser


class GetDoc(FastHttpUser):
    host = 'https://register.test.nais.gov.ua'
    authorization = 'UB ba53260762a379816fddf81a'  # Авторизируемся и берем в заголовке Authorization
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

    @task
    def get_infospravka_object(self):
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
        response_generate = self.client.post("/ubql", name="get_infospravka_object_method_generate",
                                             headers=self.headers, json=data_generate)
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

        self.client.post("/ubql", name="get_infospravka_object_method_select", headers=self.headers, json=data_select)

        data_get_doc_pdf = {
            "entity": "rep_reportResult",
            "attribute": "generatedDocument",
            "ID": report_result_id,
            "store": "reportsLU",
            "origName": '{report_result_id}{pdf}'.format(report_result_id=str(report_result_id),
                                                         pdf='.pdf'),
            "filename": 'rep_reportResult{report_result_id}generatedDocument'.format(
                report_result_id=str(report_result_id)),
            "_rc": 1
        }

        self.client.get("/getDocument", name="get_infospravka_object_method_generatedDocument", headers=self.headers,
                        params=data_get_doc_pdf)

    @task
    def get_infospravka_subject_pers_code(self):
        data_generate = [{
            "entity": "rrpUb_infoRrp",
            "method": "generate",
            "searchParams": {
                "isShowHistoricalNames": False,
                "searchType": "2",

                "reason": "autotest",
                "isSuspend": False,
                "dcReqtypeSubject": "4",
                "subjectSearchInfo": {
                    "sbjType": "1",
                    "sbjCode": "2529121363",
                    "dcSearchAlgorithm": "1"
                },
                "employeeId": 25213
            }
        }]

        response_generate = self.client.post("/ubql", name="get_infospravka_subject_pers_code_method_generate",
                                             headers=self.headers, json=data_generate)
        result_data = response_generate.json()[0].get('resultData')
        report_result_id = json.loads(result_data).get('reportResultID')
        group_result_id = json.loads(result_data).get('groupResult')[0].get('ID')

        data_generate_pdf = [
            {
                "entity": "rrpUb_infoRrp",
                "method": "generatePdf",
                "resultData": "null",
                "reportResultID": report_result_id,
                "groupID": group_result_id
            }
        ]

        response_generate_pdf = self.client.post("/ubql", name="get_infospravka_subject_pers_code_method_generatePdf",
                                                 headers=self.headers,
                                                 json=data_generate_pdf)

        report_result_id_generate_pdf = response_generate_pdf.json()[0].get('reportResultID')
        data_select = [{
            "entity": "rep_reportResult",
            "fieldList": [
                "generatedDocument",
                "ID",
                "mi_modifyDate",
                "erc_userID"
            ],
            "ID": report_result_id_generate_pdf,
            "method": "select"
        }]

        self.client.post("/ubql", name="get_infospravka_subject_pers_code_method_select",
                         headers=self.headers,
                         json=data_select)

        data_get_doc_pdf = {
            "entity": "rep_reportResult",
            "attribute": "generatedDocument",
            "ID": report_result_id_generate_pdf,
            "store": "reportsLU",
            "origName": '{report_result_id}{pdf}'.format(report_result_id=str(report_result_id_generate_pdf),
                                                         pdf='.pdf'),
            "filename": 'rep_reportResult{report_result_id}generatedDocument'.format(
                report_result_id=str(report_result_id_generate_pdf)),
            "_rc": 1
        }

        self.client.get("/getDocument", name="get_infospravka_subject_pers_code_method_generatedDocument",
                        headers=self.headers,
                        params=data_get_doc_pdf)

