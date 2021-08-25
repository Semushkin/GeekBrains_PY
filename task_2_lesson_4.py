'''
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
'''

from requests import get
from decimal import Decimal

def currency_rates(code):
    try:
        response = get('http://www.cbr.ru/scripts/XML_daily.asp')  # Проверяем соединение с интернет ресурсом
    except:
        return -1  # При остутсвии соединение, завершить выполнеие функции, и вернуть код ошибки "-1".
    content = response.content.decode(encoding=response.encoding)
    code = code.upper() #  Привидение к верхнему регистру
    content = content[content.find(code):content.find('</Value', content.find(code))]
    #  Ищем в тексте искомую валюту как точка старта среза, и конец среза, последующее вхождение '</Value'.
    if content != '':  # Проверяем не вернул ли поиск пустую строку в 'content'
        content = content.split('<Value>')[1]
        content = content.replace(',', '.')
        content = Decimal(content)
        content = float(content.quantize(Decimal('1.00')))
        return content
    else:  # Если поиск вернул пустую строку, взвращаем None
        return None

print("---------------------------")
answer = currency_rates(input('Specify the currency: '))

#  Обрабатываем результаты работы функции.
if answer == -1:  # Если нет соединения
    print('Error! Internet resource is not responding')
elif answer == None:  # Если валюта не найдена
    print(answer)
else:
    print(f'{answer}, Data type: {type(answer)}')  # Если валюта найдена, вывести результат
print("---------------------------")