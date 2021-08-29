'''
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
'''

from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = perf_counter()
unique_number = set()
repeated_number = set()
for number in src:
    if number in repeated_number:
        continue
    if number in unique_number:
        repeated_number.add(number)
        unique_number.discard(number)
        continue
    unique_number.add(number)
print([number for number in src if number in unique_number])  # Выводим данные с сохранением порядка


