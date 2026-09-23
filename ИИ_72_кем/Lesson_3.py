# 1 байт = 8 битов
# 1 Килобайт (Кбайт) = 1024 байта = 𝟐^𝟏𝟎 байтов
# 1 Мегабайт (Мбайт) = 1024 Килобайта = 𝟐^𝟐𝟎 байтов
# 1 Гигабайт (Гбайт) = 1024 Мегабайта = 𝟐^𝟑𝟎 байтов
# 1 Терабайт (Тбайт) = 1024 Гигабайта = 𝟐^𝟒𝟎 байтов



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

# Количество символов на странице = 60 строк * 56 символов = 3360 символов
# По условию используется 32-х символьный алфавит (т. е. мощность алфавита = 32 символа).
# 𝟐^𝐢=𝟑𝟐 символа, отсюда i = 5 бит.
# Такое количество информации приходится на 1 символ 32-х символьного алфавита.
# Количество информации, содержащееся на странице =
# 3360 символов * 5 бит = 16800 бит
# Переводим в байты: 16800 бит : 8 бит = 2100 байт
# Переводим в Кб 2100 байт : 1024 байт = 2,05 Кб
