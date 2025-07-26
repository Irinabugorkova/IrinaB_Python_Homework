# 1

employee_list = [
    "Jonh Snow", 
    "Piter Pen", 
    "Drakula", 
    "IvanIV", 
    "Moana", 
    "Juilet"
    ]

print(employee_list[1] + ", " + employee_list[-2])

# 2 


def dev_by_three(number):
    return "Да" if (number) % 3 == 0 else "Нет"


user_number = int(input("введите число: "))

result = dev_by_three(user_number)

print(f"Делится ли на три {user_number}? - {result}")

# 3 

import math


def min_boxes(items):
    return math.ceil(items / 5)


user_items = int(input("Количество предметов: "))
print(f"минимальное количество коробок: {min_boxes(user_items)}")

# 4

n = int(input("Введите число: "))


def check_divisibility(n):
    for i in range(1, n + 1):
        if i % 2 == 0 and i % 4 != 0:
            print(f"{i}: Делится на 2, но не на 4")
        elif i % 4 == 0:
            print(f"{i}: Делится и на 2, и на 4")
        else:
            print(i) 


check_divisibility(n)

# 5


def quarter_of_year(n_month):
    if (1 <= n_month <= 3):
        return "I квартал"
    if (4 <= n_month <= 6):
        return "II квартал"
    if (7 <= n_month <= 9):
        return "III квартал"
    if (10 <= n_month <= 12):
        return "IV квартал"
    else:
        return "Неверный номер месяца"


n_month = int(input("Введите номер месяца: "))

result = quarter_of_year(n_month)

print(result)

# 6

lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

for num in lst:
    if num > 15 and num % 3 == 0:
        print(num)

# 7

my_list = list(range(25, 0, -5))

print(my_list)

# 8

var_1 = 50
var_2 = 5

temp = var_1, var_2 = var_2, var_1 

print("var_1 = ", var_1)
print("var_2 = ", var_2)