'''
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3
#>>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции?
Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:
#>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
'''

from functools import wraps

result = dict()


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args):
        area = callback(*args)
        for i in args:
            print(f'{i} : {type(i)}, ', end='')
        return area
    return wrapper


@type_logger
def calc_cube(*args):
    return print(f'Результат функции: {type(args)}')


calc_cube(3, 'какой-то текст', 5.435, (5, 3, 3))
