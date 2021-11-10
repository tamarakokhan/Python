# задача 1
from time import sleep

print("Задача 1")


class TrafficLight:
    __color = "цвет"

    def running(self):
        for _ in range(5):
            print("Горит красный сигнал светофора - движение запрещенно!")
            sleep(7)
            print("Горит желтый сигнал светофора - подготовьтесь начать движение!")
            sleep(2)
            print("Горит зеленый сигнал светофора - движение разрешено!")
            sleep(10)
            print("Горит желтый сигнал светофора - необходимо закончить движение!")
            sleep(2)


trafficLight = TrafficLight()
trafficLight.running()

print("Задача 2")


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self, weight=25, thickness=5):
        total_weight = int(self._length) * int(self._width) * weight * thickness / 1000
        print(f"{total_weight} тонн")


road = Road(2000, 50)
road.calculation()

print("Задача 3")


class Worker:
    def __init__(self, n, s, p, wage, bonus):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Имя сотрудника {self.name} {self.surname}, {self.position}")

    def get_total_income(self):
        print(f"Доход с учетом премии {sum(self._income.values())}")


employee_1 = Position("Tamara", "Kokhan", "HR", 10000, 1000)
employee_1.get_full_name()
employee_1.get_total_income()

print("Задача 4")


class Car:
    def __init__(self, s, c, n, d, p=False):
        self.speed = s
        self.color = c
        self.name = n
        self.direction = d
        self.is_police = p
        print(f"Машина {self.name}, цвет - {self.color}. Она полицейская? {self.is_police}")

    def go(self):
        return f"Машина {self.name} поехала."

    def stop(self):
        return f"Машина {self.name} остановилась."

    def turn(self):
        return f"Машина {self.name} повернула на {self.direction}."

    def show_speed(self):
        return f"Скорость машины {self.name} {self.speed} км/ч."


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Скорость машины {self.name} {self.speed} км/ч. Скорость превышена!"
        else:
            return super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Скорость машины {self.name} {self.speed} км/ч. Скорость превышена!"
        else:
            return super().show_speed()


class PoliceCar(Car):
    pass


auto_1 = TownCar(59, "серебристый", "Ford Fusion", "север")
print(auto_1.go(), auto_1.stop(), auto_1.turn(), auto_1.show_speed())

auto_2 = SportCar(150, "красный", "Audi Sport", "юг")
print(auto_2.go(), auto_2.stop(), auto_2.turn(), auto_2.show_speed())

auto_3 = WorkCar(43, "черный", "Volvo BL71", "северо-восток")
print(auto_3.go(), auto_3.stop(), auto_3.turn(), auto_3.show_speed())

auto_4 = PoliceCar(70, "бело-синяя", "Chevrolet Impala", "запад", True)
print(auto_4.go(), auto_4.stop(), auto_4.turn(), auto_4.show_speed())

print("Задача 5")


class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        return "Запуск отрисовки."


class Pen(Stationery):
    def draw(self):
        return f"Пишем ручкой {self.title}."


class Pencil(Stationery):
    def draw(self):
        return f"Штрихуем карандашом {self.title}."


class Handl(Stationery):
    def draw(self):
        return f"Выделяем маркером {self.title}."


ex_1 = Pen("Parker")
print(ex_1.draw())
ex_2 = Pencil("Derwent")
print(ex_2.draw())
ex_3 = Handl("TouchFive")
print(ex_3.draw())
