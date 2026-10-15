#замыкания
#def outer():
#    num = 5

#    def inner ():
#        nonlocal num
#        num +=1
#        print(num)

#    return inner

#fu = outer()

#fu()
#fu()
#fu()
#fu()
#fu()
#fu()
#fu()
#fu()
#фуууууууууууууууууууууууууууууу

import time

login_users = {}
drinks_menu = {
    "Добрый Кола": 75,
    "Добрый Спрайт": 75,
    "Вода Негазированная": 35,
    "Вода Газированная": 40,
    "Чай Чёрный": 35,
    "Чай Зелёный": 50,
    "Морс Брусничный": 65,
    "Морс Облепиховый": 65
}
pizza_menu = {
    "Сырная пицца": 500,
    "Пицца пепперони": 700,
    "Мясная пицца": 800,
    "Пицца Маргарита": 700,
    "Пицца с ананасами": 700,
    "Авторская пицца": 750,
    "Пицца из школы": 36,
    "Микспицца (пепперони, сырная, мясная, маргарита)": 900
}
fastfud_menu = {
    "Картошка Фри": 50,
    "Нагетсы": 50,
    "Сырные шарики": 75
}
kids_fastfud_menu = {
    "Мини-Картошка Фри": 25,
    "Мини-Нагетсы": 25,
    "Мини-Сырные шарики": 37
}
kids_menu = {
    "Мини-Сырная пицца": 300,
    "Мини-Пепперони": 400,
    "Мини-Маргарита": 400,
    "Мини-Мясная": 500
}

current_login = None


def register(login, password):
    if login in login_users:
        print("Такой логин уже занят")
        return False
    login_users[login] = password
    print(f"Вы {login} успешно зарегистрирован.")
    return True


def login():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    if login in login_users and login_users[login] == password:
        print(f"Добро пожаловать, {login}!")
        return login
    else:
        print("Неверный логин или пароль.")
        return None


def calculate_total(order):
    total = 0
    for name, price, quanity in order:
        total = total + price * quanity
    return total


def time_pizza():
    print("\nЗаказ готовится...")
    for minutes in range(5, 0, -1):
        print(f"Осталось {minutes} мин.")
        time.sleep(60)
    print("Ваш заказ готов! приятного аппетита!")


while True:
    print("\nЭто ресторан с названием - ДТВТДатоцаоржыфколпжло")
    print("---------------------------------------------------")
    if current_login is None:
        print("Вы не авторизованы")
    else:
        print(f"Вы вошли как: {current_login}")
    print("1. Заказать пиццу")
    print("2. Меню")
    print("3. Логин / Регистрация")
    print("4. Выход")

    menu = input("Выберите: ")

    if menu == "1":
        print("\nКто будет заказывать?")
        print("1. Взрослый")
        print("2. Ребёнок (детское меню)")
        who = input("выбор: ")

        full_order = []

        if who == "1":
            order = []
            while True:
                print("\nПиццы")
                for i, (name, price) in enumerate(pizza_menu.items(), start=1):
                    print(f"{i}. {name} - {price} р.")
                print("0. Вернуться назад")

                choice = input("Введите номер позиции (0 - закончить): ")
                if choice == "0":
                    break
                if not choice.isdigit():
                    print("Введите число!")
                    continue
                idx = int(choice) - 1
                keys = list(pizza_menu.keys())
                if 0 <= idx < len(keys):
                    name = keys[idx]
                    quanity = input(f"Сколько порций '{name}'? ")
                    if not quanity.isdigit():
                        print("Введите число!")
                        continue
                    order.append((name, pizza_menu[name], int(quanity)))
                    print(f"Добавлено: {name} x{quanity}")
                else:
                    print("Нет такой позиции.")
            full_order += order

            order = []
            while True:
                print("\nФастфуд")
                for i, (name, price) in enumerate(fastfud_menu.items(), start=1):
                    print(f"{i}. {name} - {price} р.")
                print("0. Вернуться назад")

                choice = input("Введите номер позиции (0 - закончить): ")
                if choice == "0":
                    break
                if not choice.isdigit():
                    print("Введите число!")
                    continue
                idx = int(choice) - 1
                keys = list(fastfud_menu.keys())
                if 0 <= idx < len(keys):
                    name = keys[idx]
                    quanity = input(f"Сколько порций '{name}'? ")
                    if not quanity.isdigit():
                        print("Введите число!")
                        continue
                    order.append((name, fastfud_menu[name], int(quanity)))
                    print(f"Добавлено: {name} x{quanity}")
                else:
                    print("Нет такой позиции.")
            full_order += order

            order = []
            while True:
                print("\nНапитки")
                for i, (name, price) in enumerate(drinks_menu.items(), start=1):
                    print(f"{i}. {name} - {price} р.")
                print("0. Вернуться назад")

                choice = input("Введите номер позиции (0 - закончить): ")
                if choice == "0":
                    break
                if not choice.isdigit():
                    print("Введите число!")
                    continue
                idx = int(choice) - 1
                keys = list(drinks_menu.keys())
                if 0 <= idx < len(keys):
                    name = keys[idx]
                    quanity = input(f"Сколько порций '{name}'? ")
                    if not quanity.isdigit():
                        print("Введите число!")
                        continue
                    order.append((name, drinks_menu[name], int(quanity)))
                    print(f"Добавлено: {name} x{quanity}")
                else:
                    print("Нет такой позиции.")
            full_order += order

        elif who == "2":
            order = []
            while True:
                print("\nДетское меню")
                for i, (name, price) in enumerate(kids_menu.items(), start=1):
                    print(f"{i}. {name} - {price} р.")
                print("0. Вернуться назад")

                choice = input("Введите номер позиции (0 - закончить): ")
                if choice == "0":
                    break
                if not choice.isdigit():
                    print("Введите число!")
                    continue
                idx = int(choice) - 1
                keys = list(kids_menu.keys())
                if 0 <= idx < len(keys):
                    name = keys[idx]
                    quanity = input(f"Сколько порций '{name}'? ")
                    if not quanity.isdigit():
                        print("Введите число!")
                        continue
                    order.append((name, kids_menu[name], int(quanity)))
                    print(f"Добавлено: {name} x{quanity}")
                else:
                    print("Нет такой позиции.")
            full_order += order

            order = []
            while True:
                print("\nДетский фастфуд")
                for i, (name, price) in enumerate(kids_fastfud_menu.items(), start=1):
                    print(f"{i}. {name} - {price} р.")
                print("0. Вернуться назад")

                choice = input("Введите номер позиции (0 - закончить): ")
                if choice == "0":
                    break
                if not choice.isdigit():
                    print("Введите число!")
                    continue
                idx = int(choice) - 1
                keys = list(kids_fastfud_menu.keys())
                if 0 <= idx < len(keys):
                    name = keys[idx]
                    quanity = input(f"Сколько порций '{name}'? ")
                    if not quanity.isdigit():
                        print("Введите число!")
                        continue
                    order.append((name, kids_fastfud_menu[name], int(quanity)))
                    print(f"Добавлено: {name} x{quanity}")
                else:
                    print("Нет такой позиции.")
            full_order += order

            order = []
            while True:
                print("\nНапитки")
                for i, (name, price) in enumerate(drinks_menu.items(), start=1):
                    print(f"{i}. {name} - {price} р.")
                print("0. Вернуться назад")

                choice = input("Введите номер позиции (0 - закончить): ")
                if choice == "0":
                    break
                if not choice.isdigit():
                    print("Введите число!")
                    continue
                idx = int(choice) - 1
                keys = list(drinks_menu.keys())
                if 0 <= idx < len(keys):
                    name = keys[idx]
                    quanity = input(f"Сколько порций '{name}'? ")
                    if not quanity.isdigit():
                        print("Введите число!")
                        continue
                    order.append((name, drinks_menu[name], int(quanity)))
                    print(f"Добавлено: {name} x{quanity}")
                else:
                    print("Нет такой позиции.")
            full_order += order

        else:
            print("Неверный выбор.")
            continue

        if not full_order:
            print("Заказ пуст.")
            continue

        total = calculate_total(full_order)

        print("\nВаш заказ")
        if current_login is None:
            print("Гость")
        else:
            print(f"Клиент: {current_login}")
        for name, price, quanity in full_order:
            print(f"{name} x{quanity} = {price * quanity} р.")
        print(f"Итого: {total} р.")

        print(f"\nСумма к оплате: {total} р.")
        method_pay = input("Способ оплаты (1 - наличные, 2 - карта): ")

        pay_true = False
        if method_pay == "1":
            while True:
                try:
                    cash = int(input("Введите сумму наличными: "))
                except ValueError:
                    print("Введите число!")
                    continue
                if cash < total:
                    print("Недостаточно средств. Попробуйте снова.")
                else:
                    change = cash - total
                    print(f"Сдача: {change} р.")
                    pay_true = True
                    break
        elif method_pay == "2":
            print("Оплата картой прошла успешно.")
            pay_true = True
        else:
            print("Неверный способ оплаты.")

        if pay_true:
            print("Заказ принят! Робот приступает к работе.")
            time_pizza()
        else:
            print("Оплата не прошла. Заказ отменён.")

    elif menu == "2":
        print("\nПиццы")
        for i, (name, price) in enumerate(pizza_menu.items(), start=1):
            print(f"{i}. {name} - {price} р.")
        print("0. Вернуться назад")

        print("\nФастфуд")
        for i, (name, price) in enumerate(fastfud_menu.items(), start=1):
            print(f"{i}. {name} - {price} р.")
        print("0. Вернуться назад")

        print("\nДетское меню")
        for i, (name, price) in enumerate(kids_menu.items(), start=1):
            print(f"{i}. {name} - {price} р.")
        print("0. Вернуться назад")

        print("\nДетский фастфуд")
        for i, (name, price) in enumerate(kids_fastfud_menu.items(), start=1):
            print(f"{i}. {name} - {price} р.")
        print("0. Вернуться назад")

        print("\nНапитки")
        for i, (name, price) in enumerate(drinks_menu.items(), start=1):
            print(f"{i}. {name} - {price} р.")
        print("0. Вернуться назад")

    elif menu == "3":
        print("1. Войти")
        print("2. Зарегистрироваться")
        sub = input("Выбор: ")
        if sub == "1":
            result = login()
            if result is not None:
                current_login = result
        elif sub == "2":
            login_name = input("Придумайте логин: ")
            password = input("Придумайте пароль: ")
            register(login_name, password)
        else:
            print("Неверный выбор.")

    elif menu == "4":
        print("приходи ещё!!!!!! до свидания! втфоврытшфыовлжафалырпыопрыволпордпллплвалпларвпррдаыпрлыдпывпрлдыволаыаолпдлыррлыалаыполп")
        break
    else:
        print("Неверный пункт меню.")
