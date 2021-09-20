'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''

import re


class Data:

    def __init__(self, data):
        self.data = self.transformation(self.validation(data))

    @classmethod
    def transformation(cls, data):
        data['day'] = int(data['day'])
        data['month'] = int(data['month'])
        data['year'] = int(data['year'])
        return data

    @staticmethod
    def validation(data):
        if not isinstance(data, str):
            raise TypeError(f'Неверный тип данных, должна быть строка. Получено {type(data)}')
        pattern = re.compile(r'(?P<day>\d{1,2}).(?P<month>\d{1,2}).(?P<year>\d{4})').finditer(data)
        if not pattern:
            raise ValueError(f'Неверный формат даты. Должно быть 00.00.0000. Получено {data}')
        for i in pattern:
            i_1 = i.groupdict()
            if int(i_1['day']) > 31:
                raise ValueError(f'Не верно указан день месяца, больше 31. Указано: {i_1["day"]}')
            if int(i_1['month']) > 12:
                raise ValueError(f'Не верно указан месяцб больше 12. Указано: {i_1["month"]}')
            return i_1


result = Data('31.12.2021')
print(f'day = {result.data["day"]}, data type :{type(result.data["day"])}')
print(f'month = {result.data["month"]}, data type :{type(result.data["month"])}')
print(f'year = {result.data["year"]}, data type :{type(result.data["year"])}')

