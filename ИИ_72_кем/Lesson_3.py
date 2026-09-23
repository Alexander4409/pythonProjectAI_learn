# 1 байт = 8 битов
# 1 Килобайт (Кбайт) = 1024 байта = 𝟐^𝟏𝟎 байтов
# 1 Мегабайт (Мбайт) = 1024 Килобайта = 𝟐^𝟐𝟎 байтов
# 1 Гигабайт (Гбайт) = 1024 Мегабайта = 𝟐^𝟑𝟎 байтов
# 1 Терабайт (Тбайт) = 1024 Гигабайта = 𝟐^𝟒𝟎 байтов
from random import choice


def convert_bytes():
    try:
        bytes_count = float(input("enter bytes count: "))
    except ValueError:
        print("Error enter correct valid")
        return

    user_choice = input(f'please enter chosen value: \n'
                            f'1 - Kb\n'
                            f'2 - mb\n'
                            f'3 - GB\n'
                            f'4 - TB')

    units = {
        "1": (1024,"kb"),
        "2": (1024**2,"mb"),
        "3": (1024**3,"gb"),
        "4": (1024**4,"tb"),
    }

    if user_choice in units:
        divider , unit_name = units[user_choice]
        res = bytes_count / divider
        print(f'result - {bytes_count}, bytes - {round(res, 4)}, {unit_name}')
    else:
        print("Error, check your data")

convert_bytes()