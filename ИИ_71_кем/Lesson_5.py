import datetime
def user_input():
    global year
    global mouth
    global day
    year = int(input("введите год"))
    mouth = int(input("введите месяц"))
    day = int(input("введите день"))
def date():
    try:
        datetime.date(year, mouth, day)
        print("Это возможная дата")
    except ValueError:
        print("Это не возможная дата")
while True:
    user_input()
    date()
