'''
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.
'''

from utils import currency_rates

currencies = ['gbp', 'byn', 'eur', 'kgs', 'XDR', 'nok']

print("---------------------------")
for i in currencies:
    result = currency_rates(i)
    if result == -1:
        print('Error! Internet resource is not responding')
    elif result == None:
        print(result)
    else:
        currency_date = result[1].date()
        print(f'Currency {i.upper()}: {result[0]}, Date: {currency_date}')  # Если валюта найдена, вывести результат
    print("---------------------------")
