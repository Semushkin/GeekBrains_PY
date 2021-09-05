'''
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых
не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
'''
import os

TARGET = 'some_data'
file_size = dict()
DICT_MAX = 10

for s in range(DICT_MAX):
    file_size[10 ** (s + 1)] = 0

for path, folder, file_s in os.walk(TARGET):
    for file in file_s:
        for s in file_size:
            if os.stat(os.path.join(TARGET, file)).st_size > s:
                continue
            else:
                file_size[s] += 1
                break

for i in file_size:
    print(f'{i} : {file_size[i]}')