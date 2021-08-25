'''
5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
> python task_4_5.py USD
75.18, 2020-09-05
'''

from requests import get
from decimal import Decimal
import datetime
import sys


def currency_rates(code):
    try:
        response = get('http://www.cbr.ru/scripts/XML_daily.asp')  # Проверяем соединение с интернет ресурсом
    except:
        return -1  # При остутсвии соединение, завершить выполнеие функции, и вернуть код ошибки "-1".
    content = response.content.decode(encoding=response.encoding)
    code = code.upper() #  Привидение к верхнему регистру
    content_currency = content[content.find(code):content.find('</Value', content.find(code))]  #  Выризаем строку искомой валюты вместе с ее стоимостью.
    content_date = content[content.find('Date="') + 6:content.find('"', content.find('Date="') + 6)]  #  Выризаем дату из ответа сервера
    content_date = datetime.datetime.strptime(content_date, '%d.%m.%Y')  #  Приводим дату к формату datetime
    #  Ищем в тексте искомую валюту как точка старта среза, и конец среза, последующее вхождение '</Value'.
    if content_currency != '':  # Проверяем не вернул ли поиск пустую строку в 'content_currency'
        content_currency = Decimal(content_currency.split('<Value>')[1].replace(',', '.'))  #  Отрезаем все лишнее и приводим к типу Decimal
        content_currency = content_currency.quantize(Decimal('1.00'))  #  Округляем до двух знаков после запятой. Проще было бы float, и округлить до двух знаков после запятой.
        return content_currency, content_date  #  Возвращаем кортеж с двумя переменными
    else:  # Если поиск вернул пустую строку, взвращаем None
        return None


req = sys.argv  #  Принимаем аргумент из командной строки
answer = currency_rates(req[1])
print("---------------------------")
#  Обрабатываем результаты работы функции.
if answer == -1:  # Если нет соединения, сообщение об ошибке.
    print('Error! Internet resource is not responding')
elif answer == None:  # Если валюта не найдена, None
    print(answer)
else:
    currency_date = answer[1].date()
    print(f'Currency {req[1].upper()}: {answer[0]}, Date: {currency_date} (type of date time: {type(currency_date)})')  # Если валюта найдена, вывести результат
print("---------------------------")