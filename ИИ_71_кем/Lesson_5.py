a = int(input("Введите количество паролей"))
b = int(input("Длина одного пароля"))
c = int(input("Информационный вес одного символ"))
bit = b * c
byts = bit / 8
ff = byts * a
user_choise = int(input(f"Choose\n"
                        f"1.KB\n"
                        f"2.MB\n"
                        f"3.GB\n"
                        f"4.TB\n"
                        f"Ваш выбор: "))
units = {1: (1024, "KB"),
         2: (1024**2, "MB"),
         3: (1024**3, "GB"),
         4: (1024**4, "TB")}
if user_choise in units:
    divider, unit_name = units[user_choise]
    res = ff / divider
    print(f"Результат в {unit_name}: {res}")
else:
    print("Error")
print(f"Количество байт: {ff}")
