'''
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
'''


class Car:

    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    def go(self):
        return f'{self.name} Go'

    def stop(self):
        return f'{self.name} Stop'

    def turn(self, direction):
        return f'{self.name} turned {direction}'

    def show_speed(self):
        return f'Speed: {self.speed}.'


class TownCar(Car):

    is_police = False

    def show_speed(self):
        return f'Speed: {self.speed}. excess of speed!' if self.speed > 60 else f'Speed: {self.speed}.'


class SportCar(Car):

    is_police = False


class WorkCar(Car):

    is_police = False

    def show_speed(self):
        return f'Speed: {self.speed}. excess of speed!' if self.speed > 60 else f'Speed: {self.speed}.'


class PoliceCar(Car):

    is_police = True


def is_police(car):
    return f'{car.name} is police' if car.is_police else f'{car.name} is not police'


def check(car, direction):
    print(is_police(car))
    print(car.go())
    print(car.show_speed())
    print(car.turn(direction))
    print(car.stop())
    print('-----------------')


result_1 = TownCar('Porcshe', 45, 'yellow')
result_2 = PoliceCar('Ford', 73, 'black')
result_3 = WorkCar('Lada', 50, 'green')

check(result_1, 'left')
check(result_2, 'right')
check(result_3, 'left')