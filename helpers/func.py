import re
import datetime
import time
import io

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
