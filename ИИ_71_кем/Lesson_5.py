import datetime
def user_input():
    global year
    global mouth
    global day
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
def date():
    try:
        datetime.date(year, mouth, day)
        print("Это возможная дата")
    except ValueError:
        print("Это не возможная дата")
while True:
    user_input()
    date()
