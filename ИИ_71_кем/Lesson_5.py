try:
    year = int(input("введите год"))
except ValueError:
    print("ошибка")
try:
    mouth = int(input("введите месяц"))
except ValueError:
    print("ошибка")
try:
    day = int(input("введите день"))
except ValueError:
    print("ошибка")
if year % 4 == 0:
    leap_year = 1
else:
    leap_year = 0
if mouth % 2 and mouth <= 12 and day <= 30:
    print("это возможно")
elif mouth % 2 != 0 and mouth <= 12 and day <= 29 and leap_year == 0:
    if mouth == 2:
        print("это не возможно")
    else:
        print("это возможно")
    if mouth == 2 and leap_year == 1:
        print("Это возможно")
else:
    print("это не возможно")

