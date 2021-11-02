# задача 1
from sys import argv
# задача 2, 4
from random import randint
# задача 5
from functools import reduce
# задача 6
from itertools import count, cycle
# задача 7
from math import factorial

print("Задача 1")
name, a_1, a_2 = argv


def salary(hours, rate_per_hour):
    try:
        return (float(hours) * float(rate_per_hour)) + 0.1 * (float(hours) * float(rate_per_hour))
    except ValueError:
        return "Введите 2 числа."


print(f"Зарплата - {salary(a_1, a_2)}")

print("Задача 2")
list_2 = [randint(0, 300) for _ in range(15)]
new_list = []
for i in range(1, len(list_2)):
    if list_2[i] > list_2[i - 1]:
        new_list.append(list_2[i])
print(list_2)
print(new_list)

print("Задача 3")
list_3 = [n for n in range(20, 241) if n % 20 == 0 or n % 21 == 0]
print(list_3)

print("Задача 4")
list_4 = [randint(0, 20) for _ in range(15)]
new_list4 = [val for val in list_4 if list_4.count(val) == 1]
print(list_4)
print(new_list4)

print("Задача 5")


def pr(val_1, val_2):
    return val_1 * val_2


print(reduce(pr, [b for b in range(100, 1001) if b % 2 == 0]))

print("Задача 6")
for c_1 in count(3):
    if c_1 > 10:
        break
    print(c_1)

c_2 = 0
for val in cycle([1, 'a', 2, 'b', 3, 'c']):
    if c_2 > 10:
        break
    print(val)
    c_2 += 1

print("Задача 7")


def fact(num):
    for j in range(num + 1):
        yield f"{j}! = {factorial(j)}"


for el in fact(int(input("Введите число: "))):
    print(el)
