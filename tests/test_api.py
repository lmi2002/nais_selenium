import hashlib
import json
import os
import time
import requests


authorization = 'UB 5636f2bc60f5da227f60bca6'
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


def sss():
    data = [{"entity":"rrpUb_infoRrp","method":"generate","searchParams":{"isShowHistoricalNames":False,"searchType":"1","reason":"пів","isSuspend":False,"dcReqtypeSubject":"4","objectSearchInfo":{"realtyAddressInfo":{"atuID":336288,"houseType":"1","house":"5","objectNumType":"2","objectNum":"61"}},"employeeId":25213}}]
    response = requests.post('https://register.test.nais.gov.ua/ubql', headers=headers, data=json.dumps(data))
    print(response.status_code)
    print(response.json())


def search_statement_date():
    data = [{
                "entity":"rrpUb_requestSearchQuery",
                "method":"search",
                "acName":"r_fnd",
                "searchParams":{
                    "regStartDate":"2020-11-01T00:00:00.000Z",
                    "regFinishDate":"2020-11-10T00:00:00.000Z"
                },
                "privCode":"NOTAR_REQUEST_SEARCH_SIMPLE_SEARCH",
                "privPrefix":"NOTAR"
            }]
    response = requests.post('https://register.test.nais.gov.ua/ubql', headers=headers, data=json.dumps(data))
    assert response.status_code == 400
    assert bool(response.json()[0].get('resultData')) == True


if __name__ == '__main__':
    search_statement_date()
