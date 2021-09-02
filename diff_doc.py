import os

path_folder = r'C:\Users\v.anokhin\Desktop\api'


def get_text_from_file(file_name):
    d = os.path.join(path_folder, file_name)
    with open(os.path.join(path_folder, file_name), "rb") as f:
        text = f.read()

    text_decode = text.decode('utf-8')
    return text_decode[text_decode.find('reportResultID'):len(text_decode)]


if __name__ == "__main__":

    file_name_1 = input('Введите имя файла1:')

    file_name_2 = input('Введите имя файла2:')
    string1 = get_text_from_file(file_name_1)
    string2 = get_text_from_file(file_name_2)
    if string1 == string2:
        print('Файлы равны!!!')
    else:
        print('Файлы не равны!!!')
