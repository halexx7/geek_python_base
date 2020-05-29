__author__ = "Alexey_Khlybov"

import time

"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: 
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, 
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно 
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и 
вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении 
выводить соответствующее сообщение и завершать скрипт.
"""


class TrafficLight:
    # методы класса
    def running(self):
        while True:
            print('Красный')
            time.sleep(7)
            print('Желтый')
            time.sleep(2)
            print('Зеленый')
            time.sleep(10)


a = TrafficLight()
a.running()



"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных 
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета 
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта 
для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:

    def __init__(self, length, width, mass: int = 40, depth: int = 10):
        self._length = length
        self._width = width
        self.mass = mass
        self.depth = depth

    def asphalt_mass(self):
        return self._length * self._width * self.mass * self.depth


a = Road(2000, 8)
print(f'Масса асфальта: {a.asphalt_mass()} кг')


"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), 
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, 
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position 
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения 
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник: {self.surname} {self.name}')

    def get_total_income(self):
        print(f'Доход: {self._income["wage"] + self._income["bonus"]}')


a = Position('Иван', 'Петров', 'НПУ', {'wage': 10000, 'bonus': 5000})
a.get_full_name()
a.get_total_income()

"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, 
is_police (булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, 
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте 
в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar 
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о 
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police: bool, us_turn='налево'):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.us_turn = us_turn

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self):
        if self.us_turn == 'налево':
            print('Повернули налево!')
        else:
            print('Повернули направо!')

    def show_speed(self):
        print(f'Ваша текущая скорость: {self.speed} км/ч')


# TownCar, SportCar, WorkCar, PoliceCar
class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'ВНИМАНИЕ! {self.color} {self.name} Понизьте скорость!\nВы превышаете скорость на {self.speed - 60} км/ч.')
        else:
            print(f'Ваша текущая скорость: {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'ВНИМАНИЕ! {self.color} {self.name} Понизьте скорость!\nВы превышаете скорость на {self.speed - 60} км/ч.')
        else:
            print(f'Ваша текущая скорость: {self.speed} км/ч')


class PoliceCar(Car):
    pass


tcar = TownCar(80, 'White', 'Volvo', False)
tcar.show_speed()

scar = SportCar(80, 'Black', 'Lamborghini', False, 'направо')
scar.turn()
scar.show_speed()





"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и 
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), 
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из 
классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный 
метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Начинается отрисовка ручкой {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'Начинается отрисовка карандашом {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'Начинается отрисовка маркером {self.title}.')


black_pen = Pen('Parker')
black_pen.draw()

pen = Pencil('Конструктор')
pen.draw()

Hand = Handle('Attache')
Hand.draw()

