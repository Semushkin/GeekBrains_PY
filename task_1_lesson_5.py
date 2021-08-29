'''
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...
'''

MAX_NUM = 29


def odd_nums():
    for num in range(1, MAX_NUM + 1, 2):
        yield num


nums = odd_nums()
for num in range(1, MAX_NUM + 3, 2): #  Работа до ошибки ...StopIteration... включительно
    print(next(nums))
