import json
import re

import allure
import requests
import pytest


@allure.severity(allure.severity_level.NORMAL)
class TestApiStatement:
    # path = 'https://register.test.nais.gov.ua/ubql'  # Тестовое окружение
    path = 'https://ernb.dev.nais.gov.ua/ubql'  # Дев окружение
    term_review_date = '2022-05-18T13:06:00.000Z'

    authorization = 'CERT2 19bdb204627e38e72570009a'  # Авторизируемся и берем в заголовке Authorization
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

    # Добавить @перем termReviewDate -
    def test_create_st_remove(self):
        data = [
            {
                "entity": "rrpUb_requestCard",
                "method": "insert",
                "instance": "{\"dcReqType\":\"21\",\"dcDocGiveType\":\"1\",\"dcReqRegType\":\"5\",\"RstCore_EnumCombobox-3289-inputEl\":null,\"outNum\":\"1\",\"outDate\":\"2022-05-04T00:00:00.000Z\",\"dcTermReview\":\"2880\",\"termReviewDate\":\"2022-05-14T16:42:00.000Z\",\"extEmail\":\"\",\"dcDocReceiveType\":null,\"additional\":\"\",\"employeeId\":25213,\"reqTypeExtension\":null,\"dcExtReceiveType\":\"2\",\"registrar\":{\"employeeID\":25213,\"regionID\":12091,\"organizationID\":22061},\"dzk\":[],\"paymentDocuments\":[{\"dcPayType\":\"5\",\"enum\":\"8877\",\"rpdDate\":\"2022-05-12T00:00:00.000Z\",\"summ\":\"100,00\",\"orgName\":\"банк\",\"receiptNum\":\"\",\"reportResultID\":\"\",\"dcPdKind\":\"1\",\"payType\":\"Адміністративний збір за реєстраційні дії\"}],\"subjects\":[{\"idDoc\":[{\"dcSidType\":\"1\",\"docDate\":\"2018-11-04T00:00:00.000Z\",\"validityDate\":\"1970-01-01T00:00:00.000Z\",\"passport\":\"СН123654\",\"publisher\":\"Святошинським РУ ГУ МВС України\",\"sidTypeExtension\":null}],\"dcSbjType\":1,\"dcSbjRlNameBit\":\"\\\"1\\\",\\\"2\\\"\",\"additional\":\"\",\"dcCountry\":null,\"dcSbjSort\":1,\"idEddr\":\"\",\"phone\":\"\",\"phoneNumber\":\"\",\"email\":\"\",\"sbjCode\":\"3273008655\",\"firstName\":\"Олексій\",\"surname\":\"Півоваров \",\"patronymic\":\"\",\"sbjName\":\"Півоваров  Олексій \",\"isValidated\":\"0\",\"isDmsValidated\":\"0\",\"ID\":null}],\"causeDocuments\":[{\"params\":{\"ID\":\"\",\"dcCdKind\":null,\"dcCdType\":\"9\",\"enum\":\"8877\",\"publisher\":\"дб\",\"countPages\":\"\",\"cdTypeExtension\":\"\",\"docDate\":null,\"deliveryDate\":null,\"expirationDate\":null,\"additional\":\"\",\"cdType\":\"договір іпотеки\",\"isFilterValid\":true,\"isDabiEcd\":false,\"pagesCount\":0,\"uploadedPages\":0,\"cdCdID\":null},\"pages\":[]}],\"realties\":[{\"type\":\"onm\",\"data\":{\"reSubTypeExtension\":\"\",\"sbjCode\":\"\",\"sbjName\":null,\"enum\":\"2525803980000\",\"objectIdentifier\":\"\",\"dcReType\":\"3\",\"dcReTypeOnm\":\"2\",\"description\":\"\",\"reTypeExtension\":\"\",\"dcReSubType\":null,\"sbjRegDate\":null,\"cadNums\":[],\"dcIrpSpread\":null,\"enumSPart\":\"\",\"enumSubPart\":\"\",\"reExtension\":\"\",\"enumEmph\":\"\",\"onmAddressSave\":{\"atuAtuID\":[{\"ID\":null,\"rreRreID\":52197323,\"rrpRrpID\":null,\"atuAtuID\":26,\"house\":\"7\",\"building\":null,\"objectNum\":\"56\",\"rrpRnNum\":null,\"houseHash1\":\" 7 \",\"houseHash2\":\" 7 \",\"roomHash1\":null,\"additional\":null,\"dcObjectNumType\":\"2\",\"room\":null,\"isNotFull\":null,\"dcReOwnerKind\":\"1\",\"simpleAddress\":null,\"isSimpleAddress\":\"0\",\"objectNumHash1\":\" 56 \",\"objectNumHash2\":\" 56 \",\"roomHash2\":null,\"dcHouseType\":\"1\",\"dcRoomType\":null,\"groupNum\":1,\"buildingHash2\":null,\"dcBuildingType\":null,\"buildingHash1\":null,\"addressInfo\":\"м.Київ, вулиця Далека, будинок 7, квартира 56\",\"streetAtuId\":318069,\"isFewAreaLoc\":null,\"atuID\":318069}],\"isNotFull\":false,\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"dcObjectNumType\":\"2\",\"objectNum\":\"56\",\"objectAddressInfo\":\"м.Київ, вулиця Далека, будинок 7, квартира 56\"},\"onmAddress\":{\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"simpleAddress\":\"\",\"additional\":\"\",\"addressControlValues\":[{\"street\":318069,\"dcHouseType\":\"1\",\"house\":\"7\"}],\"levelsCombobox\":null,\"ATU_ATU_ID\":26,\"IS_NOT_FULL\":false,\"displayfield-3909-inputEl\":\"\",\"OBJECT_ATU_ATU_ID\":null,\"streetName\":318069,\"dcBuildingType\":null,\"building\":\"\",\"dcObjectNumType\":\"2\",\"objectNum\":\"56\",\"dcRoomType\":null,\"room\":\"\"},\"ID\":null}}],\"body\":{\"isFilterValid\":true,\"dcIrpSortReq\":\"1\",\"enum\":\"45485269\",\"enumIrp\":\"\",\"enumPr\":\"\",\"lmTypeExtension\":\"володіння майном\",\"enumRealty\":\"\",\"cadNum\":\"\"}}",
                "operation": "{\"acName\":\"r_reg\",\"registrar\":{}}",
                "privCode": "NOTAR_REQUEST_OPERATIONS_INPUT"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert isinstance(response.json()[0].get('rnNum'), int)

    def test_create_st_bnm(self):
        data = [
            {
                "entity": "rrpUb_requestCard",
                "method": "insert",
                "instance": "{\"dcReqType\":\"6\",\"dcDocGiveType\":\"1\",\"dcReqRegType\":\"10\",\"RstCore_EnumCombobox-2025-inputEl\":null,\"outNum\":\"\",\"outDate\":null,\"dcTermReview\":\"2880\",\"termReviewDate\":\"2022-05-14T16:56:00.000Z\",\"extEmail\":\"\",\"dcDocReceiveType\":null,\"additional\":\"\",\"employeeId\":25213,\"reqTypeExtension\":null,\"dcExtReceiveType\":\"2\",\"registrar\":{\"employeeID\":25213,\"regionID\":12091,\"organizationID\":22061},\"dzk\":[],\"paymentDocuments\":[],\"subjects\":[{\"idDoc\":[{\"rsbjRsbjID\":null,\"dcSidType\":null}],\"dcSbjType\":1,\"dcSbjRlNameBit\":[\"1\",\"2\"],\"ID\":null,\"rsbjRsbjID\":null,\"reqReqID\":null,\"sbjAdPostalID\":null,\"sbjAdLocationID\":null,\"cdCdID\":null,\"rnRnID\":null,\"sbjName\":\"Іванов Іван \",\"sbjCode\":\"1234567899\",\"isState\":null,\"dcChangeType\":\"2\",\"additional\":null,\"rnNum\":null,\"rSubjectRsbjID\":null,\"dcEntityClass\":\"1\",\"reqRnNum\":null,\"dcCountry\":0,\"phone\":null,\"dcSbjAddType\":null,\"sbjPos\":null,\"idEddr\":null,\"isValidated\":\"0\",\"isDmsValidated\":\"0\",\"isNotResident\":null,\"reasonAbsentValidate\":\"dddd\",\"surname\":\"Іванов\",\"firstName\":\"Іван\",\"patronymic\":null,\"taxNumber\":null,\"phoneNumber\":null,\"email\":null,\"isLocalGovernment\":null,\"dcSbjSort\":1}],\"causeDocuments\":[{\"params\":{\"ID\":\"\",\"dcCdKind\":null,\"dcCdType\":\"74\",\"enum\":\"22\",\"publisher\":\"дб\",\"countPages\":\"\",\"cdTypeExtension\":\"\",\"docDate\":null,\"deliveryDate\":null,\"expirationDate\":null,\"additional\":\"\",\"cdType\":\"сертифікат ДАБІ\",\"isFilterValid\":true,\"isDabiEcd\":false,\"pagesCount\":0,\"uploadedPages\":0,\"cdCdID\":null},\"pages\":[]}],\"realties\":[{\"type\":\"onm\",\"data\":{\"reSubTypeExtension\":\"\",\"sbjCode\":\"\",\"sbjName\":null,\"enum\":\"666923435252\",\"objectIdentifier\":\"\",\"dcReType\":\"2\",\"dcReTypeOnm\":\"2\",\"description\":\"\",\"reTypeExtension\":\"\",\"dcReSubType\":null,\"sbjRegDate\":null,\"cadNums\":[],\"dcIrpSpread\":null,\"enumSPart\":\"\",\"enumSubPart\":\"\",\"reExtension\":\"\",\"enumEmph\":\"\",\"onmAddressSave\":{\"atuAtuID\":[{\"ID\":null,\"rreRreID\":52197310,\"rrpRrpID\":null,\"atuAtuID\":26,\"house\":\"15\",\"building\":null,\"objectNum\":null,\"rrpRnNum\":null,\"houseHash1\":\" 15 \",\"houseHash2\":\" 15 \",\"roomHash1\":null,\"additional\":null,\"dcObjectNumType\":null,\"room\":null,\"isNotFull\":null,\"dcReOwnerKind\":\"1\",\"simpleAddress\":null,\"isSimpleAddress\":\"0\",\"objectNumHash1\":null,\"objectNumHash2\":null,\"roomHash2\":null,\"dcHouseType\":\"1\",\"dcRoomType\":null,\"groupNum\":1,\"buildingHash2\":null,\"dcBuildingType\":null,\"buildingHash1\":null,\"addressInfo\":\"м.Київ, вулиця Вербова, будинок 15\",\"streetAtuId\":317747,\"isFewAreaLoc\":null,\"atuID\":317747}],\"isNotFull\":false,\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"objectAddressInfo\":\"м.Київ, вулиця Вербова, будинок 15\"},\"onmAddress\":{\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"simpleAddress\":\"\",\"additional\":\"\",\"addressControlValues\":[{\"street\":317747,\"dcHouseType\":\"1\",\"house\":\"15\"}],\"levelsCombobox\":null,\"ATU_ATU_ID\":26,\"IS_NOT_FULL\":false,\"displayfield-2645-inputEl\":\"\",\"OBJECT_ATU_ATU_ID\":null,\"streetName\":317747,\"dcBuildingType\":null,\"building\":\"\",\"dcObjectNumType\":null,\"objectNum\":\"\",\"dcRoomType\":null,\"room\":\"\"},\"ID\":null}}]}",
                "operation": "{\"acName\":\"r_reg\",\"registrar\":{}}",
                "privCode": "NOTAR_REQUEST_OPERATIONS_INPUT"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert isinstance(response.json()[0].get('rnNum'), int)

    def test_create_st_take_away(self):
        data = [
            {
                "entity": "rrpUb_requestCard",
                "method": "insert",
                "instance": "{\"dcReqType\":\"7\",\"dcDocGiveType\":\"1\",\"dcReqRegType\":\"6\",\"RstCore_EnumCombobox-3208-inputEl\":null,\"outNum\":\"\",\"outDate\":null,\"dcTermReview\":\"7200\",\"termReviewDate\":\"2022-05-17T17:03:00.000Z\",\"extEmail\":\"\",\"dcDocReceiveType\":null,\"additional\":\"\",\"employeeId\":25213,\"reqTypeExtension\":null,\"dcExtReceiveType\":\"2\",\"registrar\":{\"employeeID\":25213,\"regionID\":12091,\"organizationID\":22061},\"dzk\":[],\"paymentDocuments\":[{\"dcPayType\":\"5\",\"enum\":\"8877\",\"rpdDate\":\"2022-05-12T00:00:00.000Z\",\"summ\":\"100,00\",\"orgName\":\"банк\",\"receiptNum\":\"\",\"reportResultID\":\"\",\"dcPdKind\":\"1\",\"payType\":\"Адміністративний збір за реєстраційні дії\"}],\"subjects\":[{\"idDoc\":[{\"rsbjRsbjID\":null,\"dcSidType\":null}],\"dcSbjType\":1,\"dcSbjRlNameBit\":[\"1\",\"2\"],\"ID\":null,\"rsbjRsbjID\":null,\"reqReqID\":null,\"sbjAdPostalID\":null,\"sbjAdLocationID\":null,\"cdCdID\":null,\"rnRnID\":null,\"sbjName\":\"Іванов Іван \",\"sbjCode\":\"1234567899\",\"isState\":null,\"dcChangeType\":\"2\",\"additional\":null,\"rnNum\":null,\"rSubjectRsbjID\":null,\"dcEntityClass\":\"1\",\"reqRnNum\":null,\"dcCountry\":0,\"phone\":null,\"dcSbjAddType\":null,\"sbjPos\":null,\"idEddr\":null,\"isValidated\":\"0\",\"isDmsValidated\":\"0\",\"isNotResident\":null,\"reasonAbsentValidate\":null,\"surname\":\"Іванов\",\"firstName\":\"Іван\",\"patronymic\":null,\"taxNumber\":null,\"phoneNumber\":null,\"email\":null,\"isLocalGovernment\":null,\"dcSbjSort\":1}],\"causeDocuments\":[{\"params\":{\"ID\":\"\",\"dcCdKind\":null,\"dcCdType\":\"9\",\"enum\":\"8877\",\"publisher\":\"бт\",\"countPages\":\"\",\"cdTypeExtension\":\"\",\"docDate\":null,\"deliveryDate\":null,\"expirationDate\":null,\"additional\":\"\",\"cdType\":\"договір іпотеки\",\"isFilterValid\":true,\"isDabiEcd\":false,\"pagesCount\":0,\"uploadedPages\":0,\"cdCdID\":null},\"pages\":[]}],\"realties\":[],\"filter\":{\"subject\":{\"sbjName\":\"\",\"sbjCode\":\"\",\"seriesNum\":\"\"},\"rRegDate\":null,\"rDcReqType\":\"16\",\"rOutNum\":\"\",\"rOutDate\":null},\"body\":{\"enumReq\":\"49630940\"}}",
                "operation": "{\"acName\":\"r_reg\",\"registrar\":{}}",
                "privCode": "NOTAR_REQUEST_OPERATIONS_INPUT"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert isinstance(response.json()[0].get('rnNum'), int)

    def test_create_st_another(self):
        data = [
            {
                "entity": "rrpUb_requestCard",
                "method": "insert",
                "instance": "{\"dcReqType\":\"13\",\"dcDocGiveType\":\"1\",\"dcReqRegType\":\"11\",\"RstCore_EnumCombobox-4253-inputEl\":null,\"outNum\":\"\",\"outDate\":null,\"dcTermReview\":\"7200\",\"termReviewDate\":\"2022-05-17T17:09:00.000Z\",\"extEmail\":\"\",\"dcDocReceiveType\":null,\"additional\":\"\",\"employeeId\":25213,\"reqTypeExtension\":\"до заяви 12344\",\"dcExtReceiveType\":\"2\",\"registrar\":{\"employeeID\":25213,\"regionID\":12091,\"organizationID\":22061},\"dzk\":[],\"paymentDocuments\":[{\"dcPayType\":\"5\",\"enum\":\"8877\",\"rpdDate\":\"2022-05-12T00:00:00.000Z\",\"summ\":\"100,00\",\"orgName\":\"банк\",\"receiptNum\":\"\",\"reportResultID\":\"\",\"dcPdKind\":\"1\",\"payType\":\"Адміністративний збір за реєстраційні дії\"}],\"subjects\":[{\"idDoc\":[{\"rsbjRsbjID\":null,\"dcSidType\":null}],\"dcSbjType\":1,\"dcSbjRlNameBit\":[\"1\",\"2\"],\"ID\":null,\"rsbjRsbjID\":null,\"reqReqID\":null,\"sbjAdPostalID\":null,\"sbjAdLocationID\":null,\"cdCdID\":null,\"rnRnID\":null,\"sbjName\":\"ІВАНОВ іВАН \",\"sbjCode\":\"1234567899\",\"isState\":null,\"dcChangeType\":\"2\",\"additional\":null,\"rnNum\":null,\"rSubjectRsbjID\":null,\"dcEntityClass\":\"1\",\"reqRnNum\":null,\"dcCountry\":0,\"phone\":null,\"dcSbjAddType\":null,\"sbjPos\":null,\"idEddr\":null,\"isValidated\":\"0\",\"isDmsValidated\":\"0\",\"isNotResident\":null,\"reasonAbsentValidate\":null,\"surname\":\"ІВАНОВ\",\"firstName\":\"іВАН\",\"patronymic\":null,\"taxNumber\":null,\"phoneNumber\":null,\"email\":null,\"isLocalGovernment\":null,\"dcSbjSort\":1}],\"causeDocuments\":[{\"params\":{\"ID\":\"\",\"dcCdKind\":null,\"dcCdType\":\"74\",\"enum\":\"8877\",\"publisher\":\"дб\",\"countPages\":\"\",\"cdTypeExtension\":\"\",\"docDate\":null,\"deliveryDate\":null,\"expirationDate\":null,\"additional\":\"\",\"cdType\":\"сертифікат ДАБІ\",\"isFilterValid\":true,\"isDabiEcd\":false,\"pagesCount\":0,\"uploadedPages\":0,\"cdCdID\":null},\"pages\":[]}],\"realties\":[{\"type\":\"onm\",\"data\":{\"reSubTypeExtension\":\"\",\"sbjCode\":\"\",\"sbjName\":null,\"enum\":\"\",\"objectIdentifier\":\"\",\"dcReType\":\"3\",\"dcReTypeOnm\":\"2\",\"description\":\"\",\"reTypeExtension\":\"\",\"dcReSubType\":null,\"sbjRegDate\":null,\"cadNums\":[],\"dcIrpSpread\":null,\"enumSPart\":\"\",\"enumSubPart\":\"\",\"reExtension\":\"\",\"enumEmph\":\"\",\"onmAddressSave\":{\"atuAtuID\":[{\"ID\":null,\"rreRreID\":52197296,\"rrpRrpID\":null,\"atuAtuID\":26,\"house\":\"5\",\"building\":null,\"objectNum\":null,\"rrpRnNum\":null,\"houseHash1\":\" 5 \",\"houseHash2\":\" 5 \",\"roomHash1\":null,\"additional\":null,\"dcObjectNumType\":null,\"room\":null,\"isNotFull\":null,\"dcReOwnerKind\":\"1\",\"simpleAddress\":null,\"isSimpleAddress\":\"0\",\"objectNumHash1\":null,\"objectNumHash2\":null,\"roomHash2\":null,\"dcHouseType\":\"1\",\"dcRoomType\":null,\"groupNum\":1,\"buildingHash2\":null,\"dcBuildingType\":null,\"buildingHash1\":null,\"addressInfo\":\"м.Київ, проспект Лобановського Валерія, будинок 5\",\"streetAtuId\":740683,\"isFewAreaLoc\":null,\"atuID\":740683}],\"isNotFull\":false,\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"objectAddressInfo\":\"м.Київ, проспект Лобановського Валерія, будинок 5\"},\"onmAddress\":{\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"simpleAddress\":\"\",\"additional\":\"\",\"addressControlValues\":[{\"street\":740683,\"dcHouseType\":\"1\",\"house\":\"5\"}],\"levelsCombobox\":null,\"ATU_ATU_ID\":26,\"IS_NOT_FULL\":false,\"displayfield-4873-inputEl\":\"\",\"OBJECT_ATU_ATU_ID\":null,\"streetName\":740683,\"dcBuildingType\":null,\"building\":\"\",\"dcObjectNumType\":null,\"objectNum\":\"\",\"dcRoomType\":null,\"room\":\"\"},\"ID\":null}}]}",
                "operation": "{\"acName\":\"r_reg\",\"registrar\":{}}",
                "privCode": "NOTAR_REQUEST_OPERATIONS_INPUT"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert isinstance(response.json()[0].get('rnNum'), int)

    def test_create_st_pv(self):
        data = [
            {
                "entity": "rrpUb_requestCard",
                "method": "insert",
                "instance": "{\"dcReqType\":\"19\",\"dcDocGiveType\":\"1\",\"dcReqRegType\":\"1\",\"RstCore_EnumCombobox-4938-inputEl\":null,\"outNum\":\"1\",\"outDate\":\"2022-05-02T00:00:00.000Z\",\"dcTermReview\":\"7200\",\"termReviewDate\":\"2022-05-17T17:35:00.000Z\",\"extEmail\":\"\",\"dcDocReceiveType\":null,\"additional\":\"\",\"employeeId\":25213,\"reqTypeExtension\":null,\"dcExtReceiveType\":\"2\",\"registrar\":{\"employeeID\":25213,\"regionID\":12091,\"organizationID\":22061},\"dzk\":[],\"paymentDocuments\":[{\"dcPayType\":\"5\",\"enum\":\"8877\",\"rpdDate\":\"2022-05-12T00:00:00.000Z\",\"summ\":\"100,00\",\"orgName\":\"банк\",\"receiptNum\":\"\",\"reportResultID\":\"\",\"dcPdKind\":\"1\",\"payType\":\"Адміністративний збір за реєстраційні дії\"}],\"subjects\":[{\"idDoc\":[{\"dcSidType\":\"1\",\"docDate\":\"2018-11-04T00:00:00.000Z\",\"validityDate\":\"1970-01-01T00:00:00.000Z\",\"passport\":\"БВ123654\",\"publisher\":\"Святошинським РУ ГУ МВС України\",\"sidTypeExtension\":null}],\"dcSbjType\":1,\"dcSbjRlNameBit\":\"\\\"1\\\",\\\"2\\\"\",\"additional\":\"\",\"dcCountry\":null,\"dcSbjSort\":1,\"idEddr\":\"\",\"phone\":\"\",\"phoneNumber\":\"\",\"email\":\"\",\"sbjCode\":\"3273008655\",\"firstName\":\"Олена\",\"surname\":\"Маленко\",\"patronymic\":\"Івановна\",\"sbjName\":\"Маленко Олена Івановна\",\"isValidated\":\"0\",\"isDmsValidated\":\"0\",\"ID\":null}],\"causeDocuments\":[{\"params\":{\"ID\":\"\",\"dcCdKind\":null,\"dcCdType\":\"9\",\"enum\":\"8877\",\"publisher\":\"банк\",\"countPages\":\"\",\"cdTypeExtension\":\"\",\"docDate\":null,\"deliveryDate\":null,\"expirationDate\":null,\"additional\":\"\",\"cdType\":\"договір іпотеки\",\"isFilterValid\":true,\"isDabiEcd\":false,\"pagesCount\":0,\"uploadedPages\":0,\"cdCdID\":null},\"pages\":[]}],\"realties\":[{\"type\":\"onm\",\"data\":{\"reSubTypeExtension\":\"\",\"sbjCode\":\"\",\"sbjName\":null,\"enum\":\"\",\"objectIdentifier\":\"\",\"dcReType\":\"4\",\"dcReTypeOnm\":\"2\",\"description\":\"\",\"reTypeExtension\":\"\",\"dcReSubType\":null,\"sbjRegDate\":null,\"cadNums\":[],\"dcIrpSpread\":null,\"enumSPart\":\"\",\"enumSubPart\":\"\",\"reExtension\":\"\",\"enumEmph\":\"\",\"onmAddressSave\":{\"atuAtuID\":[{\"ID\":null,\"rreRreID\":52197315,\"rrpRrpID\":null,\"atuAtuID\":26,\"house\":\"4\",\"building\":null,\"objectNum\":null,\"rrpRnNum\":null,\"houseHash1\":\" 4 \",\"houseHash2\":\" 4 \",\"roomHash1\":null,\"additional\":null,\"dcObjectNumType\":null,\"room\":null,\"isNotFull\":null,\"dcReOwnerKind\":\"1\",\"simpleAddress\":null,\"isSimpleAddress\":\"0\",\"objectNumHash1\":null,\"objectNumHash2\":null,\"roomHash2\":null,\"dcHouseType\":\"1\",\"dcRoomType\":null,\"groupNum\":1,\"buildingHash2\":null,\"dcBuildingType\":null,\"buildingHash1\":null,\"addressInfo\":\"м.Київ, бульвар Верховної Ради, будинок 4\",\"streetAtuId\":317762,\"isFewAreaLoc\":null,\"atuID\":317762}],\"isNotFull\":false,\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"objectAddressInfo\":\"м.Київ, бульвар Верховної Ради, будинок 4\"},\"onmAddress\":{\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"simpleAddress\":\"\",\"additional\":\"\",\"addressControlValues\":[{\"street\":317762,\"dcHouseType\":\"1\",\"house\":\"4\"}],\"levelsCombobox\":null,\"ATU_ATU_ID\":26,\"IS_NOT_FULL\":false,\"displayfield-5558-inputEl\":\"\",\"OBJECT_ATU_ATU_ID\":null,\"streetName\":317762,\"dcBuildingType\":null,\"building\":\"\",\"dcObjectNumType\":null,\"objectNum\":\"\",\"dcRoomType\":null,\"room\":\"\"},\"ID\":null}}],\"body\":{\"isFilterValid\":true,\"dcEntityChangeTypeBit\":\"x000001\",\"dcPrKind\":\"1\",\"dcPrCommonKind\":null,\"enum\":\"\",\"enumIrp\":\"\",\"enumPr\":\"\",\"enumRealty\":\"\",\"cadNum\":\"\"}}",
                "operation": "{\"acName\":\"r_reg\",\"registrar\":{}}",
                "privCode": "NOTAR_REQUEST_OPERATIONS_INPUT"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert isinstance(response.json()[0].get('rnNum'), int)

    def test_create_st_change(self):
        data = [
            {
                "entity": "rrpUb_requestCard",
                "method": "insert",
                "instance": "{\"dcReqType\":\"20\",\"dcDocGiveType\":\"1\",\"dcReqRegType\":\"4\",\"RstCore_EnumCombobox-3675-inputEl\":null,\"outNum\":\"200002\",\"outDate\":\"2022-05-13T00:00:00.000Z\",\"dcTermReview\":\"7200\",\"termReviewDate\":\"2022-05-18T12:23:00.000Z\",\"extEmail\":\"\",\"dcDocReceiveType\":null,\"additional\":\"РРП\",\"employeeId\":25213,\"reqTypeExtension\":null,\"dcExtReceiveType\":\"2\",\"registrar\":{\"employeeID\":25213,\"regionID\":12091,\"organizationID\":22061},\"dzk\":[],\"paymentDocuments\":[{\"dcPayType\":\"5\",\"dcPdReasonType\":\"21\",\"pdReasonTypeExtension\":\"\",\"pdType\":null,\"enum\":\"\",\"rpdDate\":null,\"orgName\":null,\"additional\":\"РРП\",\"pdReasonType\":\"Національний банк України\",\"dcPdKind\":\"2\",\"payType\":\"Адміністративний збір за реєстраційні дії\"}],\"subjects\":[{\"idDoc\":[{}],\"dcSbjType\":2,\"dcSbjRlNameBit\":\"\\\"2\\\"\",\"additional\":\"РРП\",\"dcCodeAbsenceBit\":\"x0001\",\"isState\":\"0\",\"dcSbjAddType\":\"4\",\"dcCountry\":null,\"dcSbjSort\":1,\"isNotResident\":false,\"phone\":\"\",\"phoneNumber\":\"+380505004030\",\"email\":\"test@gmail.com\",\"taxNumber\":\"\",\"sbjName\":\"РО \\\"Сяйво\\\"\",\"isLocalGovernment\":true,\"isValidated\":\"0\",\"exchEdrID\":null,\"ID\":null}],\"causeDocuments\":[{\"params\":{\"ID\":\"\",\"dcCdKind\":null,\"dcCdType\":\"42\",\"enum\":\"222\",\"publisher\":\"мвс\",\"countPages\":\"222\",\"cdTypeExtension\":\"копія\",\"docDate\":\"2022-05-13T00:00:00.000Z\",\"deliveryDate\":null,\"expirationDate\":\"2028-05-31T00:00:00.000Z\",\"additional\":\"РРП\",\"cdType\":\"наказ\",\"isFilterValid\":true,\"isDabiEcd\":false,\"pagesCount\":0,\"uploadedPages\":0,\"cdCdID\":null},\"pages\":[]}],\"realties\":[],\"body\":{\"isFilterValid\":true,\"dcErrorType\":\"1\",\"dcRecTypeLnkTo\":\"1\",\"enum\":\"1000\",\"enumIrp\":\"\",\"enumPr\":\"\",\"enumRealty\":\"\",\"cadNum\":\"\",\"rbDescription\":\"РРП зміни з вини заявника + ПВ / ПДВ\"}}",
                "operation": "{\"acName\":\"r_reg\",\"registrar\":{}}",
                "privCode": "NOTAR_REQUEST_OPERATIONS_INPUT"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert isinstance(response.json()[0].get('rnNum'), int)

    def test_create_st_info(self):
        data = [
            {
                "entity": "rrpUb_requestCard",
                "method": "insert",
                "instance": "{\"dcReqType\":\"18\",\"dcDocGiveType\":\"1\",\"dcReqRegType\":\"12\",\"RstCore_EnumCombobox-4624-inputEl\":null,\"outNum\":\"180000\",\"outDate\":\"2022-05-13T00:00:00.000Z\",\"dcTermReview\":\"7200\",\"termReviewDate\":\"2022-05-18T12:36:00.000Z\",\"extEmail\":\"\",\"dcDocReceiveType\":null,\"additional\":\"РРП - ІНФО\",\"employeeId\":25213,\"reqTypeExtension\":null,\"dcExtReceiveType\":\"2\",\"registrar\":{\"employeeID\":25213,\"regionID\":12091,\"organizationID\":22061},\"dzk\":[],\"paymentDocuments\":[{\"dcPayType\":\"5\",\"dcPdReasonType\":\"21\",\"pdReasonTypeExtension\":\"\",\"pdType\":null,\"enum\":\"\",\"rpdDate\":null,\"orgName\":null,\"additional\":\"РРП - ІНФО\",\"pdReasonType\":\"Національний банк України\",\"dcPdKind\":\"2\",\"payType\":\"Адміністративний збір за реєстраційні дії\"},{\"dcPayType\":\"6\",\"dcPdReasonType\":\"21\",\"pdReasonTypeExtension\":\"\",\"pdType\":null,\"enum\":\"\",\"rpdDate\":null,\"orgName\":null,\"additional\":\"РРП - ІНФО\",\"pdReasonType\":\"Національний банк України\",\"dcPdKind\":\"2\",\"payType\":\"Адміністративний збір за надання інформації\"}],\"subjects\":[{\"idDoc\":[{}],\"dcSbjType\":2,\"dcSbjRlNameBit\":\"\\\"27\\\",\\\"2\\\"\",\"additional\":\"РРП - ІНФО\",\"dcCodeAbsenceBit\":\"x0001\",\"isState\":\"0\",\"dcSbjAddType\":null,\"dcCountry\":null,\"dcSbjSort\":1,\"isNotResident\":false,\"phone\":\"\",\"phoneNumber\":\"+380505004030\",\"email\":\"test_11@gmail.com\",\"taxNumber\":\"\",\"sbjName\":\"ТОВ \\\"Інше\\\"\",\"isLocalGovernment\":true,\"isValidated\":\"0\",\"ID\":null}],\"causeDocuments\":[{\"params\":{\"ID\":\"\",\"dcCdKind\":\"1\",\"dcCdType\":\"6\",\"enum\":\"123\",\"publisher\":\"мвс\",\"countPages\":\"123\",\"cdTypeExtension\":\"копія\",\"docDate\":\"2022-05-13T00:00:00.000Z\",\"deliveryDate\":null,\"expirationDate\":\"2027-05-31T00:00:00.000Z\",\"additional\":\"РРП - ІНФО\",\"cdType\":\"договір дарування\",\"isFilterValid\":true,\"isDabiEcd\":false,\"pagesCount\":0,\"uploadedPages\":0,\"cdCdID\":null},\"pages\":[]}],\"realties\":[],\"filter\":{\"address\":{},\"subject\":{\"dcSbjType\":\"2\",\"sbjName\":\"КМДА\",\"sbjCode\":\"00022527\"},\"isSubjectExists\":true},\"body\":{\"dcReqDocType\":\"6\",\"dcDocTypeInfo\":\"2\",\"dcDocReqType\":\"1\",\"startDate\":null,\"finishDate\":null,\"dcReqTypeSubject\":\"2\",\"isOwner\":\"1\",\"dcEntityChangeTypeBit\":\"x0001\"}}",
                "operation": "{\"acName\":\"r_reg\",\"registrar\":{}}",
                "privCode": "NOTAR_REQUEST_OPERATIONS_INPUT"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert isinstance(response.json()[0].get('rnNum'), int)

    def test_create_st_ipr(self):
        data = [
            {
                "entity": "rrpUb_requestCard",
                "method": "insert",
                "instance": "{\"dcReqType\":\"19\",\"dcDocGiveType\":\"1\",\"dcReqRegType\":\"2\",\"RstCore_EnumCombobox-1024-inputEl\":null,\"outNum\":\"\",\"outDate\":null,\"dcTermReview\":\"7200\",\"termReviewDate\":\"2022-05-18T12:42:00.000Z\",\"extEmail\":\"\",\"dcDocReceiveType\":null,\"additional\":\"\",\"employeeId\":25213,\"reqTypeExtension\":null,\"dcExtReceiveType\":\"2\",\"registrar\":{\"employeeID\":25213,\"regionID\":12091,\"organizationID\":22061},\"dzk\":[],\"paymentDocuments\":[{\"dcPayType\":\"5\",\"enum\":\"8877\",\"rpdDate\":\"2022-05-13T00:00:00.000Z\",\"summ\":\"100,00\",\"orgName\":\"банк\",\"receiptNum\":\"\",\"reportResultID\":\"\",\"dcPdKind\":\"1\",\"payType\":\"Адміністративний збір за реєстраційні дії\"}],\"subjects\":[{\"idDoc\":[{\"dcSidType\":null,\"docDate\":null,\"validityDate\":null,\"seriesNum\":\"\",\"publisher\":null,\"sidTypeExtension\":null}],\"dcSbjType\":1,\"dcSbjRlNameBit\":\"\\\"1\\\",\\\"2\\\"\",\"additional\":\"\",\"dcCountry\":null,\"dcSbjSort\":1,\"idEddr\":\"\",\"phone\":\"\",\"phoneNumber\":\"\",\"email\":\"\",\"sbjCode\":\"3047821332\",\"firstName\":\"Сергій\",\"surname\":\"Токар\",\"patronymic\":\"Тестович\",\"sbjName\":\"Токар Сергій Тестович\",\"isValidated\":\"0\",\"isDmsValidated\":\"0\",\"exchDpsID\":null,\"exchDmsID\":null,\"ID\":null}],\"causeDocuments\":[{\"params\":{\"ID\":\"\",\"dcCdKind\":null,\"dcCdType\":\"42\",\"enum\":\"8877\",\"publisher\":\"бн\",\"countPages\":\"\",\"cdTypeExtension\":\"\",\"docDate\":null,\"deliveryDate\":null,\"expirationDate\":null,\"additional\":\"\",\"cdType\":\"наказ\",\"isFilterValid\":true,\"isDabiEcd\":false,\"pagesCount\":0,\"uploadedPages\":0,\"cdCdID\":null},\"pages\":[]}],\"realties\":[{\"type\":\"onm\",\"data\":{\"reSubTypeExtension\":\"\",\"sbjCode\":\"\",\"sbjName\":null,\"enum\":\"\",\"objectIdentifier\":\"\",\"dcReType\":\"2\",\"dcReTypeOnm\":\"2\",\"description\":\"\",\"reTypeExtension\":\"\",\"dcReSubType\":null,\"sbjRegDate\":null,\"cadNums\":[],\"dcIrpSpread\":\"1\",\"enumSPart\":\"\",\"enumSubPart\":\"\",\"reExtension\":\"\",\"enumEmph\":\"\",\"onmAddressSave\":{\"atuAtuID\":[{\"atuID\":317752,\"house\":\"10\",\"dcHouseType\":\"1\"}],\"isNotFull\":false,\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"objectAddressInfo\":\"м.Київ, бульвар Вернадського Академіка, будинок 10\"},\"onmAddress\":{\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"simpleAddress\":\"\",\"additional\":\"\",\"addressControlValues\":[{\"street\":317752,\"dcHouseType\":\"1\",\"house\":\"10\"}],\"levelsCombobox\":null,\"ATU_ATU_ID\":\"26\",\"IS_NOT_FULL\":false,\"displayfield-1879-inputEl\":\"\",\"OBJECT_ATU_ATU_ID\":null,\"streetName\":317752,\"dcBuildingType\":null,\"building\":\"\",\"dcObjectNumType\":null,\"objectNum\":\"\",\"dcRoomType\":null,\"room\":\"\"},\"ID\":null}}],\"body\":{\"isFilterValid\":true,\"dcEntityChangeTypeBit\":\"x000001\",\"dcSearchType\":\"49\",\"dcIrpSortReq\":\"4\",\"dcEasementType\":\"07.01\",\"enum\":\"\",\"enumIrp\":\"\",\"enumPr\":\"\",\"enumRealty\":\"\",\"cadNum\":\"\"}}",
                "operation": "{\"acName\":\"r_reg\",\"registrar\":{}}",
                "privCode": "NOTAR_REQUEST_OPERATIONS_INPUT"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert isinstance(response.json()[0].get('rnNum'), int)

    def test_create_st_cancel(self):
        data = [
            {
                "entity": "rrpUb_requestCard",
                "method": "insert",
                "instance": "{\"dcReqType\":\"16\",\"dcDocGiveType\":\"1\",\"dcReqRegType\":\"9\",\"RstCore_EnumCombobox-5853-inputEl\":null,\"outNum\":\"160000\",\"outDate\":\"2022-05-13T00:00:00.000Z\",\"dcTermReview\":\"7200\",\"termReviewDate\":\"2022-05-18T12:43:00.000Z\",\"extEmail\":\"\",\"dcDocReceiveType\":null,\"additional\":\"РРП - СКАСУВАННЯ\",\"employeeId\":25213,\"reqTypeExtension\":null,\"dcExtReceiveType\":\"2\",\"registrar\":{\"employeeID\":25213,\"regionID\":12091,\"organizationID\":22061},\"dzk\":[],\"paymentDocuments\":[{\"dcPayType\":\"5\",\"dcPdReasonType\":\"21\",\"pdReasonTypeExtension\":\"\",\"pdType\":null,\"enum\":\"\",\"rpdDate\":null,\"orgName\":null,\"additional\":\"РРП - СКАСУВАННЯ\",\"pdReasonType\":\"Національний банк України\",\"dcPdKind\":\"2\",\"payType\":\"Адміністративний збір за реєстраційні дії\"}],\"subjects\":[{\"idDoc\":[{}],\"dcSbjType\":2,\"dcSbjRlNameBit\":\"\\\"2\\\"\",\"additional\":\"РРП - СКАСУВАННЯ\",\"isState\":\"0\",\"dcSbjAddType\":null,\"dcCountry\":null,\"dcSbjSort\":1,\"isNotResident\":false,\"phone\":\"\",\"phoneNumber\":\"+380505004030\",\"email\":\"test@gmail.com\",\"taxNumber\":\"\",\"sbjCode\":\"23362711\",\"sbjName\":\"Публічне акціонерне товариство  \\\"Діамантбанк\\\"\",\"isLocalGovernment\":false,\"isValidated\":\"0\",\"ID\":null}],\"causeDocuments\":[{\"params\":{\"ID\":\"\",\"dcCdKind\":\"1\",\"dcCdType\":\"6\",\"enum\":\"123\",\"publisher\":\"мвс\",\"countPages\":\"123\",\"cdTypeExtension\":\"оригінал договору\",\"docDate\":\"2022-05-13T00:00:00.000Z\",\"deliveryDate\":null,\"expirationDate\":\"2029-06-05T00:00:00.000Z\",\"additional\":\"РРП - СКАСУВАННЯ\",\"cdType\":\"договір дарування\",\"isFilterValid\":true,\"isDabiEcd\":false,\"pagesCount\":0,\"uploadedPages\":0,\"cdCdID\":null},\"pages\":[]}],\"realties\":[],\"body\":{\"dcEntityChangeTypeBit\":null,\"dcCancelKind\":\"5\",\"decEnum\":\"\",\"enumRealty\":\"2525787080000\",\"recordNumber\":false,\"dcRecType\":\"1\",\"enum\":\"1000\",\"enumBrealty\":\"\",\"cadNum\":\"\",\"rbDescription\":\"\",\"additional\":\"РРП - СКАСУВАННЯ\",\"isExtractNeed\":true}}",
                "operation": "{\"acName\":\"r_reg\",\"registrar\":{}}",
                "privCode": "NOTAR_REQUEST_OPERATIONS_INPUT"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert isinstance(response.json()[0].get('rnNum'), int)

    def test_create_st_obt(self):
        data = [
            {
                "entity": "rrpUb_requestCard",
                "method": "insert",
                "instance": "{\"dcReqType\":\"19\",\"dcDocGiveType\":\"1\",\"dcReqRegType\":\"3\",\"RstCore_EnumCombobox-3906-inputEl\":null,\"outNum\":\"\",\"outDate\":null,\"dcTermReview\":\"7200\",\"termReviewDate\":\"2022-05-18T13:06:00.000Z\",\"extEmail\":\"\",\"dcDocReceiveType\":null,\"additional\":\"\",\"employeeId\":25213,\"reqTypeExtension\":null,\"dcExtReceiveType\":\"2\",\"registrar\":{\"employeeID\":25213,\"regionID\":12091,\"organizationID\":22061},\"dzk\":[],\"paymentDocuments\":[{\"dcPayType\":\"5\",\"enum\":\"22\",\"rpdDate\":\"2022-05-13T00:00:00.000Z\",\"summ\":\"100,00\",\"orgName\":\"банк\",\"receiptNum\":\"\",\"reportResultID\":\"\",\"dcPdKind\":\"1\",\"payType\":\"Адміністративний збір за реєстраційні дії\"}],\"subjects\":[{\"idDoc\":[{\"dcSidType\":null,\"docDate\":null,\"validityDate\":null,\"seriesNum\":\"\",\"publisher\":null,\"sidTypeExtension\":null}],\"dcSbjType\":1,\"dcSbjRlNameBit\":\"\\\"11\\\",\\\"1\\\"\",\"additional\":\"\",\"dcCountry\":null,\"dcSbjSort\":1,\"idEddr\":\"\",\"phone\":\"\",\"phoneNumber\":\"\",\"email\":\"\",\"sbjCode\":\"3047821332\",\"firstName\":\"Сергій\",\"surname\":\"Тестовий \",\"patronymic\":\"Тестович\",\"sbjName\":\"Тестовий  Сергій Тестович\",\"isValidated\":\"0\",\"isDmsValidated\":\"0\",\"exchDpsID\":null,\"exchDmsID\":null,\"ID\":null},{\"idDoc\":[{\"dcSidType\":null,\"docDate\":null,\"validityDate\":null,\"seriesNum\":\"\",\"publisher\":null,\"sidTypeExtension\":null}],\"dcSbjType\":1,\"dcSbjRlNameBit\":\"\\\"3\\\"\",\"additional\":\"\",\"dcCountry\":null,\"dcSbjSort\":1,\"idEddr\":\"\",\"phone\":\"\",\"phoneNumber\":\"\",\"email\":\"\",\"sbjCode\":\"3979282223\",\"firstName\":\"Тест\",\"surname\":\"Доминикано\",\"patronymic\":\"Тестович\",\"sbjName\":\"Доминикано Тест Тестович\",\"isValidated\":\"0\",\"isDmsValidated\":\"0\",\"exchDpsID\":null,\"exchDmsID\":null,\"ID\":null}],\"causeDocuments\":[{\"params\":{\"ID\":\"\",\"dcCdKind\":null,\"dcCdType\":\"42\",\"enum\":\"8877\",\"publisher\":\"бд\",\"countPages\":\"\",\"cdTypeExtension\":\"\",\"docDate\":null,\"deliveryDate\":null,\"expirationDate\":null,\"additional\":\"\",\"cdType\":\"наказ\",\"isFilterValid\":true,\"isDabiEcd\":false,\"pagesCount\":0,\"uploadedPages\":0,\"cdCdID\":null},\"pages\":[]}],\"realties\":[{\"type\":\"onm\",\"data\":{\"reSubTypeExtension\":\"\",\"sbjCode\":\"\",\"sbjName\":null,\"enum\":\"\",\"objectIdentifier\":\"\",\"dcReType\":\"2\",\"dcReTypeOnm\":\"2\",\"description\":\"\",\"reTypeExtension\":\"\",\"dcReSubType\":null,\"sbjRegDate\":null,\"cadNums\":[],\"dcIrpSpread\":null,\"enumSPart\":\"\",\"enumSubPart\":\"\",\"reExtension\":\"\",\"enumEmph\":\"\",\"onmAddressSave\":{\"atuAtuID\":[{\"atuID\":317762,\"house\":\"10\",\"dcHouseType\":\"1\"}],\"isNotFull\":false,\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"objectAddressInfo\":\"м.Київ, бульвар Верховної Ради, будинок 10\"},\"onmAddress\":{\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"simpleAddress\":\"\",\"additional\":\"\",\"addressControlValues\":[{\"street\":317762,\"dcHouseType\":\"1\",\"house\":\"10\"}],\"levelsCombobox\":null,\"ATU_ATU_ID\":\"26\",\"IS_NOT_FULL\":false,\"displayfield-4475-inputEl\":\"\",\"OBJECT_ATU_ATU_ID\":null,\"streetName\":317762,\"dcBuildingType\":null,\"building\":\"\",\"dcObjectNumType\":null,\"objectNum\":\"\",\"dcRoomType\":null,\"room\":\"\"},\"ID\":null}}],\"body\":{\"isFilterValid\":true,\"dcEntityChangeTypeBit\":\"x000001\",\"dcLmType\":\"5\",\"isPrLimited\":false,\"isUndefined\":false,\"enum\":\"\",\"enumIrp\":\"\",\"enumPr\":\"\",\"lmTypeExtension\":\"обтяж\",\"enumRealty\":\"\",\"cadNum\":\"\"}}",
                "operation": "{\"acName\":\"r_reg\",\"registrar\":{}}",
                "privCode": "NOTAR_REQUEST_OPERATIONS_INPUT"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert isinstance(response.json()[0].get('rnNum'), int)

    def test_create_st_decision_court(self):
        data = [
            {
                "entity": "rrpUb_requestCard",
                "method": "insert",
                "instance": "{\"dcReqType\":\"15\",\"dcDocGiveType\":\"1\",\"dcReqRegType\":\"8\",\"RstCore_EnumCombobox-5103-inputEl\":null,\"outNum\":\"\",\"outDate\":null,\"dcTermReview\":\"7200\",\"termReviewDate\":\"2022-05-18T13:12:00.000Z\",\"extEmail\":\"\",\"dcDocReceiveType\":null,\"additional\":\"\",\"employeeId\":25213,\"reqTypeExtension\":null,\"dcExtReceiveType\":\"2\",\"registrar\":{\"employeeID\":25213,\"regionID\":12091,\"organizationID\":22061},\"dzk\":[],\"paymentDocuments\":[],\"subjects\":[{\"idDoc\":[{\"dcSidType\":null,\"docDate\":null,\"validityDate\":null,\"seriesNum\":\"\",\"publisher\":null,\"sidTypeExtension\":null}],\"dcSbjType\":1,\"dcSbjRlNameBit\":\"\\\"1\\\",\\\"5\\\"\",\"additional\":\"\",\"dcCountry\":null,\"dcSbjSort\":1,\"idEddr\":\"\",\"phone\":\"\",\"phoneNumber\":\"\",\"email\":\"\",\"sbjCode\":\"3047821332\",\"firstName\":\"Тест\",\"surname\":\"Тестовий \",\"patronymic\":\"Тестович\",\"sbjName\":\"Тестовий  Тест Тестович\",\"isValidated\":\"0\",\"isDmsValidated\":\"0\",\"exchDpsID\":null,\"exchDmsID\":null,\"ID\":null}],\"causeDocuments\":[{\"params\":{\"ID\":\"\",\"dcCdKind\":null,\"dcCdType\":\"52\",\"enum\":\"8877\",\"publisher\":\"суд\",\"countPages\":\"\",\"cdTypeExtension\":\"\",\"docDate\":null,\"deliveryDate\":null,\"expirationDate\":null,\"additional\":\"\",\"cdType\":\"рішення суду\",\"isFilterValid\":true,\"isDabiEcd\":false,\"pagesCount\":0,\"uploadedPages\":0,\"cdCdID\":null},\"pages\":[]}],\"realties\":[{\"type\":\"onm\",\"data\":{\"reSubTypeExtension\":\"\",\"sbjCode\":\"\",\"sbjName\":null,\"enum\":\"\",\"objectIdentifier\":\"\",\"dcReType\":\"2\",\"dcReTypeOnm\":\"2\",\"description\":\"\",\"reTypeExtension\":\"\",\"dcReSubType\":null,\"sbjRegDate\":null,\"cadNums\":[],\"dcIrpSpread\":null,\"enumSPart\":\"\",\"enumSubPart\":\"\",\"reExtension\":\"\",\"enumEmph\":\"\",\"onmAddressSave\":{\"atuAtuID\":[{\"atuID\":317752,\"house\":\"10\",\"dcHouseType\":\"1\"}],\"isNotFull\":false,\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"objectAddressInfo\":\"м.Київ, бульвар Вернадського Академіка, будинок 10\"},\"onmAddress\":{\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"simpleAddress\":\"\",\"additional\":\"\",\"addressControlValues\":[{\"street\":317752,\"dcHouseType\":\"1\",\"house\":\"10\"}],\"levelsCombobox\":null,\"ATU_ATU_ID\":\"26\",\"IS_NOT_FULL\":false,\"displayfield-5672-inputEl\":\"\",\"OBJECT_ATU_ATU_ID\":null,\"streetName\":317752,\"dcBuildingType\":null,\"building\":\"\",\"dcObjectNumType\":null,\"objectNum\":\"\",\"dcRoomType\":null,\"room\":\"\"},\"ID\":null}}],\"body\":{\"dcCourtDecision\":\"1\",\"dcRecType\":null,\"enum\":\"\",\"rbDescription\":\"опис\",\"isUndefined\":false,\"descriptionLmObject\":\"\"}}",
                "operation": "{\"acName\":\"r_reg\",\"registrar\":{}}",
                "privCode": "NOTAR_REQUEST_OPERATIONS_INPUT"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert isinstance(response.json()[0].get('rnNum'), int)

    def test_create_st_forbiddance(self):
        data = [
            {
                "entity": "rrpUb_requestCard",
                "method": "insert",
                "instance": "{\"dcReqType\":\"17\",\"dcDocGiveType\":\"1\",\"dcReqRegType\":\"7\",\"RstCore_EnumCombobox-1024-inputEl\":null,\"outNum\":\"17000\",\"outDate\":\"2022-05-13T00:00:00.000Z\",\"dcTermReview\":\"7200\",\"termReviewDate\":\"2022-05-18T14:23:00.000Z\",\"extEmail\":\"\",\"dcDocReceiveType\":null,\"additional\":\"РРП - ЗАБОРОНА\",\"employeeId\":25213,\"reqTypeExtension\":null,\"dcExtReceiveType\":\"2\",\"registrar\":{\"employeeID\":25213,\"regionID\":12091,\"organizationID\":22061},\"dzk\":[],\"paymentDocuments\":[],\"subjects\":[{\"idDoc\":[{}],\"dcSbjType\":2,\"dcSbjRlNameBit\":\"\\\"2\\\"\",\"additional\":\"РРП - ЗАБОРОНА\",\"dcCodeAbsenceBit\":\"x0001\",\"isState\":\"0\",\"dcSbjAddType\":null,\"dcCountry\":null,\"dcSbjSort\":1,\"isNotResident\":false,\"phone\":\"\",\"phoneNumber\":\"+380505004030\",\"email\":\"test@gmail.com\",\"taxNumber\":\"\",\"sbjName\":\"ТОВ \\\"ІНШЕ\\\"\",\"isLocalGovernment\":true,\"isValidated\":\"0\",\"exchEdrID\":null,\"ID\":null}],\"causeDocuments\":[{\"params\":{\"ID\":\"\",\"dcCdKind\":null,\"dcCdType\":\"62\",\"enum\":\"55\",\"publisher\":\"мвс\",\"countPages\":\"55\",\"cdTypeExtension\":\"копія постанови\",\"docDate\":\"2022-05-13T00:00:00.000Z\",\"deliveryDate\":null,\"expirationDate\":\"2022-05-13T00:00:00.000Z\",\"additional\":\"РРП - ЗАБОРОНА\",\"cdType\":\"документ операції\",\"isFilterValid\":true,\"isDabiEcd\":false,\"pagesCount\":0,\"uploadedPages\":0,\"cdCdID\":null},\"pages\":[]}],\"realties\":[{\"type\":\"onm\",\"data\":{\"reSubTypeExtension\":\"\",\"sbjCode\":\"\",\"sbjName\":null,\"enum\":\"\",\"objectIdentifier\":\"\",\"dcReType\":\"2\",\"dcReTypeOnm\":\"2\",\"description\":\"РРП - ЗАБОРОНА\",\"reTypeExtension\":\"інше до типу\",\"dcReSubType\":null,\"sbjRegDate\":null,\"cadNums\":[],\"dcIrpSpread\":null,\"enumSPart\":\"\",\"enumSubPart\":\"\",\"reExtension\":\"РРП - ЗАБОРОНА\",\"enumEmph\":\"\",\"onmAddressSave\":{\"atuAtuID\":[{\"atuID\":317478,\"house\":\"55-А\",\"dcHouseType\":\"1\"}],\"isNotFull\":false,\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"additional\":\"РРП - ЗАБОРОНА\",\"objectAddressInfo\":\"м.Київ, бульвар Бикова Леоніда, будинок 55-А\"},\"onmAddress\":{\"isSimpleAddress\":false,\"isFewAreaLoc\":false,\"simpleAddress\":\"\",\"additional\":\"РРП - ЗАБОРОНА\",\"addressControlValues\":[{\"street\":317478,\"dcHouseType\":\"1\",\"house\":\"55-А\"}],\"levelsCombobox\":null,\"ATU_ATU_ID\":26,\"IS_NOT_FULL\":false,\"displayfield-1684-inputEl\":\"\",\"OBJECT_ATU_ATU_ID\":null,\"streetName\":317478,\"dcBuildingType\":null,\"building\":\"\",\"dcObjectNumType\":null,\"objectNum\":\"\",\"dcRoomType\":null,\"room\":\"\"},\"ID\":null}}]}",
                "operation": "{\"acName\":\"r_reg\",\"registrar\":{}}",
                "privCode": "NOTAR_REQUEST_OPERATIONS_INPUT"
            }
        ]

        response = self.post_response(data)
        assert response.status_code == 200
        assert isinstance(response.json()[0].get('rnNum'), int)
