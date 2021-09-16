'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Clothes(ABC):

    count = 0

    @abstractmethod
    def expence(self):
        pass


class Coat(Clothes):

    def __init__(self, name, size):
        self.name = name
        self.size = size
        Coat.count += self.expence

    def __str__(self):
        return f'Coat "{self.name}": expence {self.expence}, total expence {round(Coat.count, 2)}'

    @property
    def expence(self):
        exp = self.size / 6.5 + 0.5
        return round(exp, 2)


class Suit(Clothes):

    def __init__(self, name, size):
        self.name = name
        self.size = size
        Suit.count += self.expence

    def __str__(self):
        return f'Suit "{self.name}": expence {self.expence}, total expence {round(Suit.count, 2)}'

    @property
    def expence(self):
        exp = 2 * self.size + 0.3
        return round(exp, 2)



clothes_1 = Coat('clothes_1', 5)
print(clothes_1)
clothes_2 = Coat('clothes_2', 34)
print(clothes_2)
clothes_3 = Suit('clothes_3', 67)
print(clothes_3)
clothes_4 = Suit('clothes_4', 23)
print(clothes_4)
