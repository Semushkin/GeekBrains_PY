'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class MyOwnError(Exception):
    pass


def devision(value_1, value_2):
    try:
        if value_2 == 0:
            raise MyOwnError('Деление на ноль')
        result = value_1 / value_2
        return print(result)
    except MyOwnError as err:
        print('MyOwnError!!! Деление на ноль')


devision(4, 1)
devision(4, 0)
