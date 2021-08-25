'''
### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
Примеры:
duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности, будет ли тут полезен список?
'''
duration = int(input('Введите значение: '))
print('-----------Результат--------------')
print('duration = ', duration)

if duration < 60:
    print(duration, 'сек')
else:
    seconds = duration % 60
    minutes = duration // 60
    if minutes < 60:
        print('{} мин {} сек'.format(minutes, seconds))
    else:
        hours = minutes // 60
        minutes = minutes % 60
        if hours < 60:
            print('{} час {} мин {} сек'.format(hours, minutes, seconds))
        else:
            days = hours // 24
            hours = hours % 24
            print('{} дн {} час {} мин {} сек'.format(days, hours, minutes, seconds))