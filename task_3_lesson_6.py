'''
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении
данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код,
загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить
словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём
данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
'''
from sys import exit
import json

FILE_USER = 'user.csv'
FILE_HOBBY = 'hobby.csv'

prof = dict()

with open(FILE_USER, 'r', encoding='utf-8') as f_1, \
        open(FILE_HOBBY, 'r', encoding='utf-8') as f_2:
    for user in f_1:
        hobby = f_2.readline().replace('\n', '')
        user = user.replace('\n', '')
        if hobby:
            prof[user] = hobby
        else:
            prof[user] = None
    if f_2.read():
        exit(1)

print(f'Создание словаря: {prof}')

with open('profit.json', 'w', encoding='utf-8') as f:
    json.dump(prof, f, ensure_ascii=False)
with open('profit.json', 'r', encoding='utf-8') as f:
    print(f'Чтение словаря из profit.json : {f.read()}')