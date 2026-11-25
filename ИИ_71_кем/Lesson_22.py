import json
import hashlib
import os
from datetime import datetime

orders_file = "orders.json"
admin_file = "admin.json"
KIDS_AGE_LIMIT = 12


def check_decorator(func):
    def wrapper(*args, **kwargs):
        order = func(*args, **kwargs)
        if order is None:
            return

        items_text = "\n".join(
            f"{item['name']} x {item['count']} - {item['price'] * item['count']} руб."
            for item in order["items"]
        )

        payment_info = f"Оплата: {order['payment_method']}"
        if order["payment_method"] == "Наличные":
            payment_info += f"\nВнесено: {order['cash_given']} руб.\nСдача: {order['change']} руб."

        print(
            f"\n----------------------------\n"
            f"ЧЕК ПИЦЦЕРИИ\n"
            f"Номер заказа: {order['id']}\n"
            f"Время: {order['time']}\n"
            f"Гостей: {order['guests']}\n"
            f"----------------------------\n"
            f"{items_text}\n"
            f"----------------------------\n"
            f"ИТОГО: {order['total']} руб.\n"
            f"{payment_info}\n"
            f"----------------------------\n"
        )
        return order
    return wrapper


def make_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


def setup_admin():
    if not os.path.exists(admin_file):
        with open(admin_file, "w", encoding="utf-8") as f:
            json.dump({"pass": make_hash("1234")}, f)


def get_orders():
    if not os.path.exists(orders_file):
        return []
    with open(orders_file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_orders(orders):
    with open(orders_file, "w", encoding="utf-8") as f:
        json.dump(orders, f, ensure_ascii=False, indent=4)


def process_payment(total):
    while True:
        method = input(
            f"\nК оплате: {total} руб.\n"
            "Выберите способ оплаты:\n"
            "1 - Картой\n"
            "2 - Наличными\n"
            "0 - Отменить заказ\n"
            "Выбор: "
        )

        if method == "1":
            print("Приложите карту... Оплата прошла успешно!")
            return "Карта", total, 0

        elif method == "2":
            while True:
                cash = int(input(f"Введите сумму наличных (к оплате {total} руб.): "))
                if cash < total:
                    print(f"Недостаточно средств! Не хватает {total - cash} руб.")
                else:
                    change = cash - total
                    print(f"Оплата принята! Ваша сдача: {change} руб.")
                    return "Наличные", cash, change

        elif method == "0":
            return None, 0, 0
        else:
            print("Неверный выбор, попробуйте снова.")


menu = {
    "1": {"name": "Пепперони", "price": 450},
    "2": {"name": "Маргарита", "price": 380},
    "3": {"name": "Четыре сыра", "price": 490},
    "4": {"name": "Чесночный соус", "price": 60},
    "5": {"name": "Кола", "price": 90}
}

kids_menu = {
    "6": {"name": "Мини-пицца с ветчиной и сыром", "price": 260},
    "7": {"name": "Сладкая пицца с бананом и шоколадом", "price": 240},
    "8": {"name": "Сырные палочки", "price": 170},
    "9": {"name": "Яблочный сок", "price": 65}
}


@check_decorator
def new_order():
    guests = int(input("\nСколько будет гостей: "))
    if guests <= 0:
        print("Количество гостей должно быть больше 0")
        return None

    cart = []
    ages = []

    for i in range(1, guests + 1):
        print(f"\n--- Заказ для {i}-го гостя ---")
        age = int(input(f"Введите возраст {i}-го гостя: "))
        ages.append(age)

        is_kid = age <= KIDS_AGE_LIMIT
        available_menu = menu.copy()
        if is_kid:
            print(f"Доступно детское меню (до {KIDS_AGE_LIMIT} лет)!")
            available_menu.update(kids_menu)

        while True:
            main_lines = "\n".join(f"{k} - {v['name']} ({v['price']} руб.)" for k, v in menu.items())
            menu_text = f"\nОсновное меню:\n{main_lines}"

            if is_kid:
                kids_lines = "\n".join(f"{k} - {v['name']} ({v['price']} руб.)" for k, v in kids_menu.items())
                menu_text += f"\n\nДетское меню:\n{kids_lines}"

            print(f"{menu_text}\n0 - Закончить выбор для {i}-го гостя")

            choice = input("Выберите номер: ")
            if choice == "0":
                break

            if choice in available_menu:
                count = int(input("Сколько штук: "))
                if count > 0:
                    cart.append({
                        "name": available_menu[choice]["name"],
                        "price": available_menu[choice]["price"],
                        "count": count
                    })
                    print("Добавлено в заказ!")
                else:
                    print("Количество должно быть больше 0")
            else:
                print("Такого пункта нет или он недоступен")

    if not cart:
        print("Заказ пуст")
        return None

    total = sum(item["price"] * item["count"] for item in cart)
    payment_method, cash_given, change = process_payment(total)

    if payment_method is None:
        print("Заказ отменен.")
        return None

    orders = get_orders()
    order = {
        "id": len(orders) + 1,
        "time": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "guests": guests,
        "ages": ages,
        "items": cart,
        "total": total,
        "payment_method": payment_method,
        "cash_given": cash_given,
        "change": change
    }
    orders.append(order)
    save_orders(orders)
    return order


def admin():
    password = input("Введите пароль: ")
    with open(admin_file, "r", encoding="utf-8") as f:
        saved_pass = json.load(f)["pass"]

    if make_hash(password) != saved_pass:
        print("Неверный пароль!")
        return

    while True:
        cmd = input(
            "\nАдмин панель:\n"
            "1 - Посмотреть заказы\n"
            "2 - Добавить позицию в основное меню\n"
            "3 - Добавить позицию в детское меню\n"
            "4 - Сменить пароль\n"
            "0 - Назад\n"
            "Выбор: "
        )

        if cmd == "1":
            orders = get_orders()
            if not orders:
                print("Заказов пока нет")
            else:
                print("\n".join(
                    f"Заказ № {o['id']} | Гостей: {o.get('guests', '—')} | Сумма: {o['total']} руб. ({o.get('payment_method', '—')}) | Время: {o['time']}"
                    for o in orders
                ))
        elif cmd == "2":
            name = input("Название пиццы/напитка: ")
            price = int(input("Цена: "))
            new_num = str(len(menu) + len(kids_menu) + 1)
            menu[new_num] = {"name": name, "price": price}
            print("Позиция добавлена в основное меню!")
        elif cmd == "3":
            name = input("Название детской позиции: ")
            price = int(input("Цена: "))
            new_num = str(len(menu) + len(kids_menu) + 1)
            kids_menu[new_num] = {"name": name, "price": price}
            print("Позиция добавлена в детское меню!")
        elif cmd == "4":
            new_p = input("Новый пароль: ")
            with open(admin_file, "w", encoding="utf-8") as f:
                json.dump({"pass": make_hash(new_p)}, f)
            print("Пароль изменен!")
        elif cmd == "0":
            break


setup_admin()

while True:
    x = input(
        "\n=== ПИЦЦЕРИЯ ===\n"
        "1 - Сделать заказ\n"
        "2 - Админка\n"
        "0 - Выход\n"
        "Введите цифру: "
    )
    if x == "1":
        new_order()
    elif x == "2":
        admin()
    elif x == "0":
        break
