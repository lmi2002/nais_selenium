import json
import re

import allure
import requests
import pytest


@allure.severity(allure.severity_level.NORMAL)
class TestApi:
    path = 'https://register.test.nais.gov.ua/ubql'

    authorization = 'UB a9bd012064ad42260e85a40f'  # Авторизируемся и берем в заголовке Authorization
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

    def get_response(self, res):
        requests.get(res)

    # Головне меню → Реєстрація та обробка заяв → Пошук заяв

    def test_search_statement_date(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "r_fnd",
            "searchParams": {
                "regStartDate": "2020-11-01T00:00:00.000Z",
                "regFinishDate": "2020-11-30T00:00:00.000Z"
            },
            "privCode": "NOTAR_REQUEST_SEARCH_SIMPLE_SEARCH",
            "privPrefix": "NOTAR"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    def test_search_statement_num(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "r_fnd",
            "searchParams": {
                "regNum": "42456295"
            },
            "privCode": "NOTAR_REQUEST_SEARCH_SIMPLE_SEARCH",
            "privPrefix": "NOTAR"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    def test_search_statement_date_type_st(self):
        data = [
            {
                "entity": "rrpUb_requestSearchQuery",
                "method": "search",
                "acName": "r_fnd",
                "searchParams": {
                    "regStartDate": "2020-11-01T00:00:00.000Z",
                    "regFinishDate": "2020-11-05T00:00:00.000Z",
                    "dcReqTypes": "1"
                },
                "privCode": "NOTAR_REQUEST_SEARCH_SIMPLE_SEARCH",
                "privPrefix": "NOTAR"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    def test_search_statement_date_state_st(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "r_fnd",
            "searchParams": {
                "regStartDate": "2020-11-01T00:00:00.000Z",
                "regFinishDate": "2020-11-05T00:00:00.000Z",
                "dcReqStates": "8"
            },
            "privCode": "NOTAR_REQUEST_SEARCH_SIMPLE_SEARCH",
            "privPrefix": "NOTAR"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    def test_search_statement_date_kind_sta_nt(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "r_fnd",
            "searchParams": {
                "regStartDate": "2020-11-01T00:00:00.000Z",
                "regFinishDate": "2020-11-05T00:00:00.000Z",
                "dcReqSorts": "2"
            },
            "privCode": "NOTAR_REQUEST_SEARCH_SIMPLE_SEARCH",
            "privPrefix": "NOTAR"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    def test_search_statement_address(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "r_efnd",
            "searchParams": {
                "realty": {
                    "realtyAddressInfo": {
                        "atuID": 335059,
                        "dcHouseType": "1",
                        "house": "6а",
                        "dcObjectNumType": "2",
                        "objectNum": "80"
                    }
                }
            },
            "privCode": "NOTAR_REQUEST_SEARCH_ADV_SEARCH",
            "privPrefix": "NOTAR"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    def test_search_statement_onm(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "r_efnd",
            "searchParams": {
                "realty": {
                    "realtyRegNum": "2220446532224"
                }
            },
            "privCode": "NOTAR_REQUEST_SEARCH_ADV_SEARCH",
            "privPrefix": "NOTAR"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    def test_search_statement_cad_num(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "r_efnd",
            "searchParams": {
                "realty": {
                    "cadNum": "8000000000:75:114:0010"
                }
            },
            "privCode": "NOTAR_REQUEST_SEARCH_ADV_SEARCH",
            "privPrefix": "NOTAR"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    def test_search_statement_person_params_date_person_name(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "r_efnd",
            "searchParams": {
                "regStartDate": "2015-01-29T00:00:00.000Z",
                "regFinishDate": "2015-01-29T00:00:00.000Z",
                "subject": {
                    "dcSbjTypes": "1",
                    "sbjName": "Боклан Юлія Петрівна"
                }
            },
            "privCode": "NOTAR_REQUEST_SEARCH_ADV_SEARCH",
            "privPrefix": "NOTAR"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    def test_search_statement_person_params_date_person_code(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "r_efnd",
            "searchParams": {
                "regStartDate": "2015-01-29T00:00:00.000Z",
                "regFinishDate": "2015-01-29T00:00:00.000Z",
                "subject": {
                    "sbjCode": "2529121363"
                }
            },
            "privCode": "NOTAR_REQUEST_SEARCH_ADV_SEARCH",
            "privPrefix": "NOTAR"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    def test_search_statement_company_params_date_company_name(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "r_efnd",
            "searchParams": {
                "regStartDate": "2020-07-20T00:00:00.000Z",
                "regFinishDate": "2020-07-20T00:00:00.000Z",
                "subject": {
                    "dcSbjTypes": "2",
                    "sbjName": 'КОРНИНСЬКИЙ ЗДО "ДИВОСВІТ"'
                }
            },
            "privCode": "NOTAR_REQUEST_SEARCH_ADV_SEARCH",
            "privPrefix": "NOTAR"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_statement_company_params_date_company_code(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "r_efnd",
            "searchParams": {
                "regStartDate": "2020-07-20T00:00:00.000Z",
                "regFinishDate": "2020-07-20T00:00:00.000Z",
                "subject": {
                    "dcSbjTypes": "2",
                    "sbjCode": "25315590"
                }
            },
            "privCode": "NOTAR_REQUEST_SEARCH_ADV_SEARCH",
            "privPrefix": "NOTAR"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    # Головне меню → Реєстрація та обробка заяв → Пошук заяв в БД про реєстрацію заяв та запитів
    # При обновлении тестовой БД, для этого блока тестов данные нужно подготавливать.


    def test_search_statement_from_DB_params_cad_num(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "doc_frequest",
            "reason": "",
            "searchParams": {
                "realty": {
                    "cadNum": "5625410100:01:028:0008"
                }
            },
            "privCode": "NOTAR_REQUEST_SEARCH_REG_EMPLOYEE"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_statement_from_DB_params_address(self):
        data = [
            {
                "entity": "rrpUb_requestSearchQuery",
                "method": "search",
                "acName": "doc_frequest",
                "reason": "",
                "searchParams": {
                    "realty": {
                        "isReAndRepAddressOnly": True,
                        "isNotFull": False,
                        "realtyAddressInfo": {
                            "atuID": 317478,
                            "houseType": "1",
                            "house": "12",
                            "objectNumType": "2",
                            "objectNum": "123"
                        }
                    }
                },
                "privCode": "NOTAR_REQUEST_SEARCH_REG_EMPLOYEE"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_statement_from_DB_params_id_st(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "search",
            "acName": "doc_frequest",
            "reason": "",
            "searchParams": {
                "realty": {
                },
                "regNum": "43375647",
                "regDate": "2021-07-14T10:35:23Z"
            },
            "privCode": "NOTAR_REQUEST_SEARCH_REG_EMPLOYEE"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    # Головне меню → Реєстрація та обробка заяв → Пошук рішень


    def test_search_decision_params_num(self):
        data_1 = [{
            "entity": "rrpUb_decisionCard",
            "method": "search",
            "acName": "d_fnd",
            "searchParams": {
                "regNum": "55064997",
                "holderObjID": True
            },
            "privCode": "NOTAR_DECISION_OPERATIONS_SEARCH"
        }]

        response_1 = self.post_response(data_1)
        assert response_1.status_code == 200
        sel_id = response_1.json()[0].get('selID')

        data_2 = [
            {
                "entity": "rrpUb_decisionCard",
                "method": "searchResult",
                "searchParams": {
                    "selID": sel_id,
                    "total": 1
                },
                "options": {
                    "start": 0,
                    "limit": 1,
                    "pages": 1
                },
                "fieldList": [
                    "regNum",
                    "regDate",
                    "dcDsType",
                    "dcDsState",
                    "holderName",
                    "reqRnNum",
                    "holderObjID"
                ]
            }
        ]

        response_2 = self.post_response(data_2)
        assert response_2.status_code == 200
        assert bool(response_2.json()[0].get('searchResult')) == True


    def test_search_decision_params_date(self):
        data = [{
            "entity": "rrpUb_decisionCard",
            "method": "search",
            "acName": "d_fnd",
            "searchParams": {
                "regStartDate": "2021-02-01T00:00:00.000Z",
                "regFinishDate": "2021-03-01T00:59:59.999Z",
                "holderObjID": True
            },
            "privCode": "NOTAR_DECISION_OPERATIONS_SEARCH"
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('searchResult')) == True


    def test_search_decision_params_statement_num(self):
        data_1 = [{
            "entity": "rrpUb_decisionCard",
            "method": "search",
            "acName": "d_fnd",
            "searchParams": {
                "reqRnNum": "42456295",
                "holderObjID": True
            },
            "privCode": "NOTAR_DECISION_OPERATIONS_SEARCH"
        }]

        response_1 = self.post_response(data_1)
        assert response_1.status_code == 200
        sel_id = response_1.json()[0].get('selID')

        data_2 = [
            {
                "entity": "rrpUb_decisionCard",
                "method": "searchResult",
                "searchParams": {
                    "selID": sel_id,
                    "total": 1
                },
                "options": {
                    "start": 0,
                    "limit": 1,
                    "pages": 1
                },
                "fieldList": [
                    "regNum",
                    "regDate",
                    "dcDsType",
                    "dcDsState",
                    "holderName",
                    "reqRnNum",
                    "holderObjID"
                ]
            }
        ]

        response_2 = self.post_response(data_2)
        assert response_2.status_code == 200
        assert bool(response_2.json()[0].get('searchResult')) == True


    def test_search_decision_params_date_type_decision(self):
        data = [
            {
                "entity": "rrpUb_decisionCard",
                "method": "search",
                "acName": "d_fnd",
                "searchParams": {
                    "regStartDate": "2020-11-10T00:00:00.000Z",
                    "regFinishDate": "2020-11-17T00:59:59.999Z",
                    "dcDsTypes": "24",
                    "holderObjID": True
                },
                "privCode": "NOTAR_DECISION_OPERATIONS_SEARCH"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('searchResult')) == True


    def test_search_decision_params_date_state_decision(self):
        data = [
            {
                "entity": "rrpUb_decisionCard",
                "method": "search",
                "acName": "d_fnd",
                "searchParams": {
                    "regStartDate": "2020-11-10T00:00:00.000Z",
                    "regFinishDate": "2020-11-17T00:59:59.999Z",
                    "dcDsStates": "801",
                    "holderObjID": False
                },
                "privCode": "NOTAR_DECISION_OPERATIONS_SEARCH"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('searchResult')) == True


    def test_search_decision_params_date_unlimited_company(self):
        data = [
            {
                "entity": "rrpUb_decisionCard",
                "method": "search",
                "acName": "d_fnd",
                "searchParams": {
                    "regStartDate": "2020-11-10T00:00:00.000Z",
                    "regFinishDate": "2020-11-17T00:59:59.999Z",
                    "holderObjID": True
                },
                "privCode": "NOTAR_DECISION_OPERATIONS_SEARCH"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('searchResult')) == True

    # Головне меню → Реєстрація та обробка заяв → Черга заяв

    # Когда статус кода будет приходить 200 написать дополнительную проверку

    def test_prepare_queue(self):
        data = [{
            "entity": "rrpUb_requestSearchQuery",
            "method": "prepareQueue",
            "privPrefix": "NOTAR"
        }]

        response = self.post_response(data)
        assert response.status_code == 200

    # Головне меню → Реєстрація та обробка розділів → Пошук → Розділи


    def test_search_section_realty_params_onm(self):
        data = [{
            "entity": "rrpSec_search",
            "method": "searchRealty",
            "privPrefix": "NOTAR",
            "searchParams": {
                "regNum": "565864580000",
                "isSimpleSearch": True
            }
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_realty_params_cad_num(self):
        data = [{
            "entity": "rrpSec_search",
            "method": "searchRealty",
            "privPrefix": "NOTAR",
            "searchParams": {
                "cadNum": "5625410100:01:028:0008",
                "isSimpleSearch": True
            }
        }]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_realty_params_owner_num(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchRealty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "dcRegNumType": "1",
                    "prNum": "8606729",
                    "isSimpleSearch": True
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_realty_params_irp_num(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchRealty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "dcRegNumType": "2",
                    "prNum": "39931528",
                    "isSimpleSearch": True
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_realty_params_mortgage_num(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchRealty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "dcRegNumType": "3",
                    "prNum": "39931526",
                    "isSimpleSearch": True
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_realty_params_limitation_num(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchRealty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "dcRegNumType": "4",
                    "prNum": "39931525",
                    "isSimpleSearch": True
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_realty_params_statement_num(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchRealty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "requestRegNum": "9980337",
                    "reSearchType": "isReAndRepAddressOnly",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_realty_params_date_created_realty(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchRealty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "regStartDate": "2015-01-29T00:00:00.000Z",
                    "regFinishDate": "2015-01-29T00:00:00.000Z",
                    "reSearchType": "isReAndRepAddressOnly",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_realty_params_address_realty(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchRealty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "reSearchType": "isReAndRepAddressOnly",
                    "localityAtuId": "26",
                    "streetAtuId": 335059,
                    "houseType": "1",
                    "house": "6А",
                    "objectNumType": "2",
                    "objectNum": "80",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_realty_params_ext_option_cad_num(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchRealty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "reSearchType": "isReAndRepAddressOnly",
                    "cadNum": "5625410100:01:028:0008",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    # Головне меню → Реєстрація та обробка розділів → Пошук → Права власності


    def test_search_section_property_params_onm(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "regNum": "565864580000",
                    "isSimpleSearch": True
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_property_params_cad_num(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "cadNum": "5625410100:01:028:0008",
                    "isSimpleSearch": True
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_property_params_owner_num(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "prNum": "8606729",
                    "isSimpleSearch": True
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_property_params_statement_num(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "reasonReqRnNum": "9980337",
                    "dcSbjTypes": "1,2",
                    "reSearchType": "isReAndRepAddressOnly",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    @pytest.mark.skip

    def test_search_section_property_params_date_created_property(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "regStartDate": "2015-01-29T00:00:00.000Z",
                    "regFinishDate": "2015-01-29T00:00:00.000Z",
                    "dcSbjTypes": "1,2",
                    "reSearchType": "isReAndRepAddressOnly",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        # assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_property_params_decision_num(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "reasonDsRnNum": "19084776",
                    "dcSbjTypes": "1,2",
                    "reSearchType": "isReAndRepAddressOnly",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_property_params_search_person_and_company_name(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "dcSbjTypes": "1,2",
                    "sbjNameTxt": "Боклан Юлія Петрівна",
                    "reSearchType": "isReAndRepAddressOnly",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_property_params_search_person_and_company_code(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "dcSbjTypes": "1,2",
                    "sbjCodeTxt": "33261467",
                    "reSearchType": "isReAndRepAddressOnly",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_property_params_search_person_name(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "dcSbjTypes": "1",
                    "sbjNameTxt": "Боклан Юлія Петрівна",
                    "reSearchType": "isReAndRepAddressOnly",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_property_params_search_person_code(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "dcSbjTypes": "1",
                    "sbjCodeTxt": "2529121363",
                    "reSearchType": "isReAndRepAddressOnly",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_property_params_search_company_name(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "dcSbjTypes": "2",
                    "sbjNameTxt": 'Товариство з обмеженою відповідальністю "БК БУДІНВЕСТГРУП"',
                    "reSearchType": "isReAndRepAddressOnly",
                    "isSimpleSearch": False,
                    "isAllDcPrType": True
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_property_params_search_company_code(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "dcSbjTypes": "2",
                    "sbjCodeTxt": "33261467",
                    "reSearchType": "isReAndRepAddressOnly",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_property_params_address_property(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "dcSbjTypes": "2",
                    "reSearchType": "isReAndRepAddressOnly",
                    "localityAtuId": "26",
                    "streetAtuId": 335059,
                    "houseType": "1",
                    "house": "6А",
                    "objectNumType": "2",
                    "objectNum": "80",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True


    def test_search_section_property_params_ext_option_cad_num(self):
        data = [
            {
                "entity": "rrpSec_search",
                "method": "searchProperty",
                "privPrefix": "NOTAR",
                "searchParams": {
                    "dcSbjTypes": "2",
                    "reSearchType": "isReAndRepAddressOnly",
                    "cadNum": "5625410100:01:028:0008",
                    "isSimpleSearch": False
                }
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert bool(response.json()[0].get('resultData')) == True

    # def test_exemple(self):
    #     data_1 = [
    #         {
    #             "entity": "rrpUb_infoRrp",
    #             "method": "generate",
    #             "searchParams": {
    #                 "isShowHistoricalNames": False,
    #                 "searchType": "1",
    #                 "reason": "gsd",
    #                 "isSuspend": False,
    #                 "dcReqtypeSubject": "4",
    #                 "objectSearchInfo": {
    #                     "realtyRnNum": "2236824980000"
    #                 },
    #                 "employeeId": 25213
    #             }
    #         }
    #     ]
    #
    #     response = self.post_response(data_1)
    #     assert response.status_code == 200
    #     assert bool(response.json()[0].get('resultData')) == True
    #     result_data = json.loads(response.json()[0].get('resultData'))
    #     report_result_id = result_data.get('reportResultID')
    #
    #     data_2 = [{
    #         "entity": "rep_reportResult",
    #         "fieldList": [
    #             "generatedDocument",
    #             "ID",
    #             "mi_modifyDate",
    #             "erc_userID"
    #         ],
    #         "ID": report_result_id,
    #         "method": "select"
    #     }]
    #
    #     response_2 = self.post_response(data_2)
    #     assert response_2.status_code == 200
    #     assert bool(response_2.json()[0].get('resultData')) == True
    #     m = response_2.json()[0].get('resultData')
    #     s = json.loads(m.get('data')[0][0])
    #
    #     file = self.get_response(
    #         'https://register.test.nais.gov.ua/getDocument?entity=rep_reportResult&attribute=generatedDocument&ID="{report_result_id}"&store=reportsLU&origName="{orig_name}"&filename=rep_reportResult"{report_result_id}"generatedDocument&_rc=1'.format(
    #             report_result_id="report_result_id", orig_name=s.get('origName')))
    #
    #     d = 1
