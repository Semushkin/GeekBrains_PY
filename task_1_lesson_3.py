'''
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#>>> num_translate("one")
"один"
#>>> num_translate("eight")
"восемь"
'''

number_s = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'tree': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(number):
    translate = f'Перевод: {number_s.get(number)}'
    return translate


number = input('Напишите число: ')
print(num_translate(number))
