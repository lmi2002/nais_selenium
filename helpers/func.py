import os
import re
import datetime
import time
import io
import socket
import csv

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def left_only_digits(string):
    return int(re.sub('\\D', '', string))


def replace_all_sym(string, sym):
    return re.sub('\\W', sym, string)


def replace_symb(string, lst):
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


def get_data_tomorrow():
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    return tomorrow.strftime("%d.%m.%Y")


def get_generate_num():
    return int(round(time.time() * 1000))


def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text


def get_host_name():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


def get_text_from_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        return f.read()


def get_file_response(file_name, dir_name, project_name):
    return os.path.abspath(
        '../api/{project_name}/files/{dir_name}/{file_name}{ext_file}'.format(
            file_name=file_name, dir_name=dir_name, project_name=project_name, ext_file='.txt'))


def uni_get_file_response(file_name, dir_name, project_name):
    return os.path.abspath(
        '../api/{project_name}/files/{dir_name}/{file_name}{ext_file}'.format(
            file_name=file_name, dir_name=dir_name, project_name=project_name, ext_file='.txt'))


def get_text_from_csv(file_name):
    data = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            data.append(row)
    return data


def text_to_csv(file_name, data):
    with open(file_name, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def get_list_files(dirname):
    return os.listdir(dirname)
