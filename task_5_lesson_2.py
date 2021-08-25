'''
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
'''

prices = [38.48, 47.98, 74, 50.9, 46.47, 2.9, 25, 74.11, 23.59, 5.82, 48.58, 0, 60.51, 56.73, 69.49, 14.63, 7.3, 28.26, 82.15, 20.31]
print('-------------------------')
print('Изначальный список, id (', id(prices), '):')
print(prices)

print('---------------------------')

for count in range(len(prices)):
    if type(prices[count]) == int:  #----------------------------Отсекаем целые числа, где не нужно работать со знаками после запятой. Переводим в string
        prices[count] = str(prices[count]) + ' руб 00 коп'
        continue
    if int(round(prices[count] % 1, 2) * 100) % 10 == 0: #-------Цыкл отбора копеек требующих добавления "0". Переводим в string
        kop = str(round(prices[count] % 1 / 10, 2))
        price = str(int(prices[count])), 'руб', kop[2:], 'коп'
        prices[count] = ' '.join(price)
    else:  #-----------------------------------------------------Цыкл перевода остальных элементов списка в string.
        price = str(prices[count])
        price = str(int(prices[count])) + ' руб ' + str(price[-2:]) + ' коп'
        prices[count] = price
print('Результат 1, вывод на эран одной строкой в виде <r> руб <kk> коп , id(', id(prices), '):')
print(', '.join(prices))

for count in range(len(prices)):  #------------------------------Блок перевода элемента списка в float
    price = prices[count]
    price = price.replace('руб', '.')
    price = price.replace('коп', '')
    price = price.replace(' ', '')
    prices[count] = float(price)

prices.sort() #---------------------------------------------------Сортируем по возростанию

for count in range(len(prices)):  #-------------------------------Цыкл перевода эллемента списка в string
    if prices[count] - int(prices[count]) == 0:
        price = str(prices[count])
        price = price.replace('.', ' руб 0') + ' коп'
        prices[count] = price
    else:
        price = str(prices[count])
        price = price.replace('.', ' руб ') + ' коп'
        prices[count] = price
print('-------------------------')
print('Результат 2, сортировка по возрастанию, id(', id(prices),'):')
print(', '.join(prices))

for count in range(len(prices)):  #------------------------------Блок перевода элемента списка в float
    price = prices[count]
    price = price.replace('руб', '.')
    price = price.replace('коп', '')
    price = price.replace(' ', '')
    prices[count] = float(price)

prices_2 = reversed(prices)
prices_2 = list(prices_2) #--------------------------------------Распаковка перевернутого нового списка

for count in range(len(prices_2)): #-----------------------------Цыкл перевода эллемента списка в string
    if prices_2[count] - int(prices_2[count]) == 0:
        price = str(prices_2[count])
        price = price.replace('.', ' руб 0') + ' коп'
        prices_2[count] = price
    else:
        price = str(prices_2[count])
        price = price.replace('.', ' руб ') + ' коп'
        prices_2[count] = price

print('-------------------------')
print('Результат 3, сортировка по убыванию, новый список, id(', id(prices_2),'):')
print(', '.join(prices_2))

print('-------------------------')
print('Результат 4, вывод на экран пяти самых дорогих товаров, id(', id(prices_2), '):')
print(', '.join(prices_2[:5]))