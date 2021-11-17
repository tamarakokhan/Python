# задача 4, 5, 6
from abc import ABC, abstractmethod
import sys

print("Задача 1")


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_int(cls, data):
        date_x = data.split("-")
        date = [int(num) for num in date_x]
        return cls(date)

    @staticmethod
    def validation(obj):
        if 1 <= obj.date[0] <= 31 and 1 <= obj.date[1] <= 12 and 1900 <= obj.date[2] <= 2100:
            day = obj.date[0]
            month = obj.date[1]
            year = obj.date[2]
            return f"Дата введена верно.\nДень - {day}\nМесяц - {month}\nГод - {year}"
        else:
            return f"Дата введена не верно, проверьте данные."


date_1 = Date.date_int("20-1-1995")
print(Date.validation(date_1))

print("Задача 2")


class MyError2(Exception):
    def __init__(self, text):
        self.text = text


num_1, num_2 = input("Введите первое число: "), input("Введите второе число: ")

try:
    num_1, num_2 = int(num_1), int(num_2)
    if num_2 == 0:
        raise MyError2("На ноль делить нельзя!")
except (ValueError, MyError2) as error:
    print(error)
else:
    print(f"{num_1} / {num_2} = {num_1 / num_2}")

print("Задача 3")


class MyError3(Exception):
    def __init__(self, text):
        self.text = text


list_of_nums = []
while True:
    try:
        a = input("Введите число, если хотите завершить работу введите 'stop': ")
        if a == "stop":
            print(*list_of_nums)
            break
        if not a.isdigit():
            raise MyError3("Введите число!")
        a = int(a)
        list_of_nums.append(a)
    except (ValueError, MyError3) as error:
        print(error)

print("Задача 4, 5, 6")


class Warehouse:

    def __init__(self, size):
        self.size = size
        self.equipment = []

    def acceptance(self, equipment):
        self.equipment.append(equipment.arrival())
        return self.equipment

    def to_send(self, equipment, subdivision):
        self.equipment.remove(equipment.arrival())
        return f"{equipment.arrival()} передан в {subdivision}"


class OfficeEquipment(ABC):
    def __init__(self, name, price, num):
        self.info = {"name": name, "price": price, "num": num}
        self.validation()

    def validation(self):
        if not self.info.get("price").isdigit() or not self.info.get("num").isdigit():
            print(f"Проверьте данные, 'цена' и 'количество' должны быть числами.")
            sys.exit()

    def __str__(self):
        return f"Наименование: {self.info.get('name')}, цена: {self.info.get('price')}, " \
               f"количество: {self.info.get('num')} "

    @abstractmethod
    def arrival(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, name, price, num, num_of_pages):
        super().__init__(name, price, num)
        self.num_of_pages = num_of_pages

    def arrival(self):
        return self.info


class Scanner(OfficeEquipment):
    def __init__(self, name, price, num, picture_format):
        super().__init__(name, price, num)
        self.picture_format = picture_format

    def arrival(self):
        return self.info


class Xerox(OfficeEquipment):
    def __init__(self, name, price, num, num_of_copies):
        super().__init__(name, price, num)
        self.num_of_copies = num_of_copies

    def arrival(self):
        return self.info


warehouse = Warehouse(1000)
printer_1 = Printer(input("Введите наименование: "), input("Введите цену: "),
                    input("Введите количество: "), input("Введите количество страниц: "))
scanner_1 = Scanner(input("Введите наименование: "), input("Введите цену: "),
                    input("Введите количество: "), input("Введите формат изображения: "))
xerox_1 = Xerox(input("Введите наименование: "), input("Введите цену: "),
                input("Введите количество: "), input("Введите количество копий: "))
print(printer_1)
print(scanner_1)
print(xerox_1)
warehouse.acceptance(printer_1)
warehouse.acceptance(scanner_1)
warehouse.acceptance(xerox_1)
print(warehouse.equipment)
print(warehouse.to_send(printer_1, "personnel department"))
print(warehouse.equipment)

print("Задача 7")


class ComplexNum:
    def __init__(self, n, m):
        self.num1 = n
        self.num2 = m

    def __str__(self):
        return f"{self.num1:.2f} + {self.num2:.2f}i"

    def __add__(self, other):
        self.sum_num1 = self.num1 + other.num1
        self.sum_num2 = self.num2 + other.num2
        return f"Сумма = {ComplexNum(self.sum_num1, self.sum_num2)}"

    def __mul__(self, other):
        self.mul_num1 = self.num1 * other.num1 - self.num2 * other.num2
        self.mul_num2 = self.num2 * other.num1 + self.num1 * other.num2
        return f"Произведение = {ComplexNum(self.mul_num1, self.mul_num2)}"


num1 = float(input("Введите вещественное число: "))
num2 = float(input("Введите вещественное число: "))
a = ComplexNum(num1, num2)
num1 = float(input("Введите вещественное число: "))
num2 = float(input("Введите вещественное число: "))
b = ComplexNum(num1, num2)
print(f"a = {a}, b = {b}")
print(a + b)
print(a * b)
