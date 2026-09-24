def i_dont_khnow_how_to_name_this():
    try:
        sim = int(input("введите количество символов в пароле"))
    except ValueError:
        print("ошибка")
        exit()
    try:
        encoding = int(input("кодировка"))
    except ValueError:
        print("ошибка")
        exit()
    try:
        num_password = int(input("количество паролей"))
    except ValueError:
        print("ошибка")
        exit()
    bits = sim * encoding * num_password
    byts = bits / 8
    print(byts)
while True:
    i_dont_khnow_how_to_name_this()
