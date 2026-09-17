#Бит — это количество информации, необходимое для
# однозначного определения одного из двух равновероятных событий.
from random import choices


#В информатике принято рассматривать последовательности длиной 8 битов.
# Такая последовательность называется байтом.
# 1 байт = 8 битов
# 1 Килобайт (Кбайт) = 1024 байта = 𝟐^𝟏𝟎 байтов
# 1 Мегабайт (Мбайт) = 1024 Килобайта = 𝟐^𝟐𝟎 байтов
# 1 Гигабайт (Гбайт) = 1024 Мегабайта = 𝟐^𝟑𝟎 байтов
# 1 Терабайт (Тбайт) = 1024 Гигабайта = 𝟐^𝟒𝟎 байтов

# kb convert programm
def convert_bytes():
    try:
        bytes_count = float(input("Enter bytes"))
    except ValueError:
        print("Error enter bytes")
        return


    user_choise = int(input(f"Choose\n"
                            f"1.KB\n"
                            f"2.MB\n"
                            f"3.GB\n"
                            f"4.TB"))

    units = {1:(1024,"KB"),
             2:(1024**2,"MB"),
             3:(1024**3,"GB"),
             4:(1024**4,"TB")}

    if user_choise in units:
        divider, unit_name = units[user_choise]
        res = bytes_count / divider

        print(f"Result:{bytes_count} bytes = {round(res,4)} {unit_name}")

    else:
        print("Error")

convert_bytes()



