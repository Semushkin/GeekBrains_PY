'''
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):

    def draw(self):
        return f'{self.title}: отрисовки Запуск'


class Pencil(Stationery):

    def draw(self):
        return f'{self.title}: отрисовки отрисовки'


class Handle(Stationery):

    def draw(self):
        return f'{self.title}: Запуск Запуск'


result_1 = Pen('title_1')
result_2 = Pencil('title_2')
result_3 = Handle('title_3')

print(result_1.draw())
print(result_2.draw())
print(result_3.draw())
