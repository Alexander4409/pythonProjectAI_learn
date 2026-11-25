# ДЗ доделать робота пиццемейкера, добавить функцию отслеживания заказов
import time
import os
import json

CONFIG_FILE = "config.txt"
USERS_FILE = "users.txt"
ORDERS_FILE = "orders.txt"


def save_path_to_config(path):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            f.write(path)
        return True
    except Exception as e:
        print(f"не удалось сохранить конфигурацию: {e}")
        return False


def load_path_from_config():
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return f.read().strip()
    except Exception as e:
        print(f"не удалось загрузить конфигурацию: {e}")
    return ""


def clear_config():
    try:
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)
        return True
    except Exception as e:
        print(f"не удалось очистить конфигурацию: {e}")
        return False


def save_users():
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(login_users, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"не удалось сохранить пользователей: {e}")
        return False


def load_users():
    global login_users
    try:
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    login_users = json.loads(content)
    except Exception as e:
        print(f"не удалось загрузить пользователей: {e}")


def save_order(username, order, total):
    try:
        data = []
        if os.path.exists(ORDERS_FILE):
            with open(ORDERS_FILE, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    data = json.loads(content)
        data.append({
            "user": username if username else "гость",
            "items": [{"name": n, "price": p, "quanity": q} for n, p, q in order],
            "total": total,
            "time": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        with open(ORDERS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"не удалось сохранить заказ: {e}")
        return False


def load_orders():
    try:
        if os.path.exists(ORDERS_FILE):
            with open(ORDERS_FILE, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    return json.loads(content)
    except Exception as e:
        print(f"не удалось загрузить заказы: {e}")
    return []


def show_user_orders(username):
    if not username:
        print("войдите в аккаунт, чтобы посмотреть свои заказы")
        return
    orders = load_orders()
    user_orders = [o for o in orders if o.get("user") == username]
    if not user_orders:
        print("у вас пока нет заказов")
        return
    print(f"\nваши заказы ({username}):")
    for i, o in enumerate(user_orders, start=1):
        print(f"\nзаказ №{i} от {o.get('time', '?')}")
        for item in o.get("items", []):
            print(f"  {item['name']} x{item['quanity']} = {item['price'] * item['quanity']} р.")
        print(f"  итого: {o.get('total', 0)} р.")

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
    save_users()
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

load_users()
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
    print("4. Выхд")
    print("5. мои заказы")

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
            save_order(current_login, full_order, total)
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
    elif menu == "5":
        show_user_orders(current_login)
    else:
        print("Неверный пункт меню.")
