
'''
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

#>>> a = calc_cube(5)
125
#>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
'''


from functools import wraps

result = dict()


def val_checker(callback):
    def checker(func):
        @wraps(func)
        def wrapper(*args):
            if not callback(*args):
                raise ValueError(f'wrong val {args[0]}')
            return func(*args)
        return wrapper
    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(3))
print(calc_cube(-3))
