import math


def square(side):
    area = side * side
    return math.ceil(area)


user_side = float(input("Введите сторону квадрата: "))

result = square(user_side)

print(f"Площадь квадрата со стороной {user_side}: {result}")
