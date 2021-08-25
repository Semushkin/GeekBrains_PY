'''
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

'''

text_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
count = 0

while count < len(text_list):
    search_str = text_list[count]
    number = 0
    for count2 in range(len(search_str)):  # цыкл поиска чисел в строке
        if search_str[count2].isnumeric():
            number += 1
    if number > 0:  # сли в строке есть число, добавлеяем ковычки перед и после
        text_list.insert(count, '"')
        text_list.insert(count + 2, '"')
        count += 1
    if number == 1:  # Если в строке только одна цыфра, добавляем "0"
        search_str = search_str[:-1] + '0' + search_str[-1]
        text_list[count] = search_str
    count += 1
print(text_list)  # Вывод списка
print(' '.join(text_list))  # Вывод списка  одной строкой