import re
import datetime
import time


def left_only_digits(string):
    return int(re.sub('\\D', '', string))


def replace_all_sym(string, sym):
    return re.sub('\\W', sym, string)


def replace_sym(string, lst):
    """
        Изменяет символы на необходимые символы по очередности.
        lst = содержит элементы типа tuple. В tuple содержится 2 элемента:
        Первый елемент - символ который необходимо изменить. Второй элемент - символ на который нужно заменить.
    """
    for el in lst:
        string = string.replace(el[0], el[1])

    return string


def get_data_today():
    today = datetime.datetime.today()
    return today.strftime("%d.%m.%Y")


def get_generate_num():
    return int(round(time.time() * 1000))
