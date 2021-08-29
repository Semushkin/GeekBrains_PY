'''
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
'''
MAX_NUM = 29

nums = (num for num in range(1, MAX_NUM + 1, 2))

for num in nums:
    print(num)
