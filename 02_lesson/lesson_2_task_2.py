user_year = int(input("Введите год: "))


def is_year_leap(year):
    return True if user_year % 4 == 0 else False


result = is_year_leap(user_year)

print(f"год {user_year}: {result}")
