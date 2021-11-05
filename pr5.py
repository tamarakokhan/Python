# задача 7
import json

print("Задача 1")
with open("task_1.txt", "a", encoding="UTF-8") as f_1:
    while True:
        a = input()
        f_1.write(f"{a}\n")
        if not a:
            break

print("Задача 2")
with open("text_2.txt", "r", encoding="UTF-8") as f_2:
    count_line = 0
    for line_2 in f_2:
        count_line += 1
        words = line_2.split()
        print(f"Количество слов в {count_line} строке - {len(words)}")
    print(f"Количество срок в тексте - {count_line}")

print("Задача 3")
with open("text_3.txt", "r", encoding="UTF-8") as f_3:
    low_salary = []
    whole_salary = 0
    number_of_employees = 0
    for line_3 in f_3:
        employee_salary = line_3.split()
        if float(employee_salary[1]) < 20000:
            low_salary.append(employee_salary[0])
        whole_salary += float(employee_salary[1])
        number_of_employees += 1
    print(f"Сотрудники, имеющие ЗП меньше 20 000: {', '.join(low_salary)}")
    print(f"Средний доход сотрудников: {whole_salary / number_of_employees}")

print("Задача 4")
with open("text_4.txt", "r", encoding="UTF-8") as f_4_1:
    numbers_4 = {"one": "один", "two": "два", "three": "три", "four": "четыре"}
    for line_4 in f_4_1:
        line4 = line_4.split()
        line4[0] = numbers_4.get(line4[0].lower()).title()
        with open("task_4.txt", "a", encoding="UTF-8") as f_4_2:
            f_4_2.write(f"{' '.join(line4)}\n")

print("Задача 5")


def sum_of_numbers(num):
    the_sum = 0
    for n in num:
        the_sum = the_sum + float(n)
    return the_sum


with open("task_5.txt", "a", encoding="UTF-8") as f_5:
    f_5.write(input("Введите числа через пробел: "))
with open("task_5.txt", "r", encoding="UTF-8") as f_5:
    for line_5 in f_5:
        print(sum_of_numbers(line_5.split()))

print("Задача 6")
with open("text_6.txt", "r", encoding="UTF-8") as f_6:
    dictionary_6 = {}
    for line_6 in f_6:
        line6 = line_6.split()
        hours = []
        i = 0
        while i < len(line_6):
            line_6_int = ''
            a = line_6[i]
            while '0' <= a <= '9':
                line_6_int += a
                i += 1
                if i < len(line_6):
                    a = line_6[i]
                else:
                    break
            i += 1
            if line_6_int != '':
                hours.append(int(line_6_int))
        dictionary_6.update([(line6[0], sum(hours))])
print(dictionary_6)

print("Задача 7")
with open("text_7.txt", "r", encoding="UTF-8") as f_7_1:
    total_profit = 0
    number_of_firms = 0
    dictionary_7_1 = {}
    dictionary_7_2 = {}
    total_list = []
    for line_7 in f_7_1:
        firm = line_7.split()
        profit = float(firm[2]) - float(firm[3])
        print(f"Прибыль компании {firm[0]}: {profit}")
        total_profit += profit
        number_of_firms += 1
        if profit < 0:
            total_profit -= profit
            number_of_firms -= 1
        dictionary_7_1.update([(firm[0], profit)])
    dictionary_7_2.update([("average_profit", total_profit / number_of_firms)])
    total_list.append(dictionary_7_1)
    total_list.append(dictionary_7_2)
    print(f"Средняя прибыль компаний: {total_profit / number_of_firms}")
    print(total_list)
with open("text_77.json", "w", encoding="UTF-8") as f_7_2:
    json.dump(total_list, f_7_2, ensure_ascii=False)
