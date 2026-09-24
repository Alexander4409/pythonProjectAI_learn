import datetime
def user_input():
    year = int(input("введите год"))
    mouth = int(input("введите месяц"))
    day = int(input("введите день"))
    try:
        datetime.date(year, mouth, day)
        print("Это возможная дата")
    except ValueError:
        print("Это не возможная дата")
while True:
    user_input()
