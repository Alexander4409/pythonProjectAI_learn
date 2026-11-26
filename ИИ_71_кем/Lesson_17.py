#Дописывание пиццемейкера


import time
import os
import random
from functools import wraps

DB_FILE = "users_database.txt"
MENU_FILE = "pizza_menu.txt"
RECEIPT_SUFFIX = "_receipts.txt"

default_users = {
    "Admin": {"password": "SuperAdmin123", "balance": 50000},
    "Kecha": {"password": "6767", "balance": 175},
    "Cat_May!": {"password": "kisa_may", "balance": 5839}
}

default_menu = {
    "Пепперони": 350,
    "Маргарита": 300,
    "4 сыра": 400,
    "Гавайская": 320,
    "Чай": 50,
    "Мороженое": 70
}

users_db = {}
food_main = {}
active_orders = []


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = round(end_time - start_time, 4)
        return result, duration
    return wrapper


def check_login(func):
    @wraps(func)
    def wrapper(login, *args, **kwargs):
        if login not in users_db:
            print(f"\n[СИСТЕМА] Ошибка: Пользователь '{login}' не найден или вышел из системы.")
            return None
        return func(login, *args, **kwargs)
    return wrapper


def load_database():
    global users_db
    if not os.path.exists(DB_FILE):
        users_db = {login: data.copy() for login, data in default_users.items()}
        save_database()
        return

    users_db = {}
    with open(DB_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(";")
            if len(parts) == 3:
                login, password, balance = parts
                try:
                    users_db[login] = {"password": password, "balance": int(balance)}
                except ValueError:
                    continue
    
    if not users_db:
        users_db = {login: data.copy() for login, data in default_users.items()}
        save_database()


def save_database():
    with open(DB_FILE, "w", encoding="utf-8") as file:
        for login, data in users_db.items():
            file.write(f"{login};{data['password']};{data['balance']}\n")


def load_menu():
    global food_main
    if not os.path.exists(MENU_FILE):
        food_main = default_menu.copy()
        save_menu()
        return

    food_main = {}
    with open(MENU_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(";")
            if len(parts) == 2:
                item, price = parts
                try:
                    food_main[item] = int(price)
                except ValueError:
                    continue
                    
    if not food_main:
        food_main = default_menu.copy()
        save_menu()


def save_menu():
    with open(MENU_FILE, "w", encoding="utf-8") as file:
        for item, price in food_main.items():
            file.write(f"{item};{price}\n")


def generate_receipt_id():
    return f"REC-{int(time.time())}-{random.randint(100, 999)}"


def save_receipt_to_file(login, receipt_data):
    filename = f"{login}{RECEIPT_SUFFIX}"
    with open(filename, "a", encoding="utf-8") as file:
        file.write(receipt_data + "\n---\n")


@timer
def process_kitchen_logic():
    current_time = time.time()
    completed_orders = []
    
    orders_copy = list(active_orders)
    
    for order in orders_copy:
        if current_time >= order['ready_time']:
            active_orders.remove(order)
            completed_orders.append(order)
            
    return completed_orders


def show_completed_orders(completed_list):
    if not completed_list:
        print("На кухне сейчас ничего не готовится или всё еще в процессе.")
        return
        
    print("\n=== ГОТОВО НА КУХНЕ ===")
    for order in completed_list:
        print(f"[ID: {order['id']}] {order['item']} для клиента {order['user']} готово!")
        
        receipt_text = (
            f"ЧЕК № {order['id']}\n"
            f"КЛИЕНТ: {order['user']}\n"
            f"ТОВАР: {order['item']}\n"
            f"ЦЕНА: {order['price']} руб.\n"
            f"СТАТУС: ВЫДАНО\n"
            f"ВРЕМЯ: {time.strftime('%H:%M:%S')}"
        )
        
        print("-" * 30)
        print(receipt_text)
        print("-" * 30)
        
        save_receipt_to_file(order['user'], receipt_text)


def add_user():
    print("\n--- Создание новой учетной записи ---")
    user_login = input("Введи имя пользователя: ").strip()
    
    if not user_login or ";" in user_login:
        print("Некорректное имя.")
        return
        
    if user_login in users_db:
        print("Пользователь с таким именем уже существует!")
        return

    user_password = input("Введи пароль для учетной записи: ").strip()
    
    if not user_password:
        print("Пароль не может быть пустым.")
        return

    users_db[user_login] = {"password": user_password, "balance": 0}
    save_database()
    print("Учетная запись успешно создана!")


def change_user():
    print("\n--- Изменение учетной записи ---")
    input_login = input("Введи свой логин: ").strip()
    input_password = input("Введи свой пароль: ").strip()

    if input_login not in users_db or users_db[input_login]["password"] != input_password:
        print("Неверный логин или пароль.")
        return

    print("Успешный вход!")
    new_login = input("Введи новое имя пользователя: ").strip()
    new_password = input("Введи новый пароль: ").strip()

    if not new_login or not new_password:
        print("Новые данные не могут быть пустыми.")
        return
        
    if input_login == "Admin" and new_login != "Admin":
        print("Логин администратора менять нельзя.")
        return

    if new_login != input_login and new_login in users_db:
        print("Такой логин уже занят.")
        return

    user_data = users_db.pop(input_login)
    user_data["password"] = new_password
    users_db[new_login] = user_data
    save_database()

    old_filename = f"{input_login}_orders.txt"
    new_filename = f"{new_login}_orders.txt"
    
    old_receipt = f"{input_login}{RECEIPT_SUFFIX}"
    new_receipt = f"{new_login}{RECEIPT_SUFFIX}"
    
    if os.path.exists(old_receipt):
        os.rename(old_receipt, new_receipt)
        
    if os.path.exists(old_filename):
        os.rename(old_filename, new_filename)

    print("Данные учетки изменены!")


def delete_user():
    print("\n!!! Перед удалением аккаунта авторизируйтесь в нем !!!")
    input_login = input("Введи свой логин: ").strip()
    input_password = input("Введи свой пароль: ").strip()

    if input_login not in users_db or users_db[input_login]["password"] != input_password:
        print("Неверный логин или пароль.")
        return

    if input_login == "Admin":
        print("!!! Учетную запись Admin удалить нельзя !!!")
        return

    confirmation = input("Вы действительно хотите удалить учетку? (y/n): ").strip().lower()
    if confirmation != "y":
        print("Удаление отменено.")
        return

    balance = users_db.pop(input_login)["balance"]
    save_database()

    files_to_remove = [
        f"{input_login}_orders.txt",
        f"{input_login}{RECEIPT_SUFFIX}"
    ]
    
    for fname in files_to_remove:
        if os.path.exists(fname):
            os.remove(fname)

    print(f"Заберите деньги со счета: {balance} руб.")
    time.sleep(1)
    print("Учетка удалена.")


def admin_account_menu():
    while True:
        print("\n-------- МЕНЮ АДМИНИСТРАТОРА --------")
        print("0. Выход")
        print("1. Посмотреть заказы ВСЕХ пользователей")
        print("2. Добавить / Изменить цену товара")
        print("3. Удалить товар из меню")
        print("4. Посмотреть балансы всех пользователей")
        print("5. Статус кухни (сколько заказов в работе)")

        choice = input("Выбери действие: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            print("\n--- ИСТОРИЯ ЗАКАЗОВ ---")
            for user in users_db.keys():
                filename = f"{user}{RECEIPT_SUFFIX}"
                if os.path.exists(filename):
                    with open(filename, "r", encoding="utf-8") as f:
                        lines = [l.strip() for l in f if l.strip()]
                        summary = ", ".join([l for l in lines if "ТОВАР:" in l][-5:])
                        print(f"{user}: ...{summary}")
                else:
                    print(f"{user}: Нет заказов")

        elif choice == "2":
            print("\nТекущее меню:")
            for item, price in food_main.items():
                print(f"- {item}: {price} руб.")
            
            item_name = input("\nНазвание товара: ").strip()
            if not item_name: continue
            
            try:
                new_price = int(input("Цена: "))
                if new_price >= 0:
                    food_main[item_name] = new_price
                    save_menu()
                    print("Сохранено.")
                else:
                    print("Цена отрицательная.")
            except ValueError:
                print("Ошибка ввода числа.")

        elif choice == "3":
            item_to_delete = input("\nТовар для удаления: ").strip()
            if item_to_delete in food_main:
                food_main.pop(item_to_delete)
                save_menu()
                print("Удалено.")
            else:
                print("Не найдено.")

        elif choice == "4":
            print("\n--- БАЛАНСЫ ---")
            for user, data in users_db.items():
                print(f"{user}: {data['balance']} руб.")

        elif choice == "5":
            print(f"\nАктивных заказов на кухне: {len(active_orders)}")
            for o in active_orders:
                remaining = max(0, int(o['ready_time'] - time.time()))
                print(f"ID {o['id']}: {o['item']} (осталось ждать ~{remaining} сек)")

        else:
            print("Неверный ввод.")


@check_login
def user_account_menu(login):
    while login in users_db:
        current_balance = users_db[login]["balance"]

        print(f"\n-------- КЛИЕНТ: {login} | Баланс: {current_balance} руб. --------")
        print("0. Выход")
        print("1. Посмотреть меню")
        print("2. Сделать заказ (пицца уходит на кухню)")
        print("3. Посмотреть свои чеки")
        print("4. Пополнить баланс")
        print("5. Проверить статус кухни (забрать готовые)")

        choice = input("Выбор: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            print("\nМеню пиццерии:")
            for item, price in food_main.items():
                print(f"- {item}: {price} руб.")

        elif choice == "2":
            if not food_main:
                print("Меню пусто.")
                continue
                
            print("\nДоступное меню:")
            for item, price in food_main.items():
                print(f"- {item}: {price} руб.")
                
            item_name = input("Что заказать? ").strip()
            
            if item_name not in food_main:
                print("Такого товара нет.")
                continue
                
            price = food_main[item_name]
            
            if users_db[login]["balance"] < price:
                print(f"Недостаточно средств! Нужно {price}, есть {users_db[login]['balance']}.")
                try:
                    top_up = int(input("Пополнить сейчас? (введите сумму, 0 для отказа): "))
                    if top_up > 0:
                        users_db[login]["balance"] += top_up
                        save_database()
                        print("Баланс пополнен. Заказ невозможен без повторного выбора.")
                        continue
                    else:
                        continue
                except ValueError:
                    continue

            users_db[login]["balance"] -= price
            save_database()
            
            order_id = generate_receipt_id()
            prep_time = random.randint(5, 15) 
            
            new_order = {
                'id': order_id,
                'user': login,
                'item': item_name,
                'price': price,
                'start_time': time.time(),
                'ready_time': time.time() + prep_time
            }
            
            active_orders.append(new_order)
            
            print(f"Заказ принят! ID: {order_id}")
            print(f"Пицца '{item_name}' будет готова примерно через {prep_time} секунд.")
            print("Не забудь нажать пункт 5, чтобы проверить готовность!")

        elif choice == "3":
            filename = f"{login}{RECEIPT_SUFFIX}"
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
                    if content:
                        print("\n--- ТВОИ ЧЕКИ ---")
                        print(content)
                    else:
                        print("Нет сохраненных чеков.")
            else:
                print("Файл с чеками не найден.")

        elif choice == "4":
            try:
                amount = int(input("Сумма пополнения: "))
                if amount > 0:
                    users_db[login]["balance"] += amount
                    save_database()
                    print(f"Баланс пополнен. Текущий: {users_db[login]['balance']} руб.")
                else:
                    print("Сумма должна быть положительной.")
            except ValueError:
                print("Введите число.")

        elif choice == "5":
            print("\nПРОВЕРКА КУХНИ...")
            results, duration = process_kitchen_logic()
            
            if results:
                show_completed_orders(results)
                print(f"(Проверка заняла {duration:.4f} сек.)")
            else:
                print("Пока ничего не готово. Ждите...")
                if active_orders:
                     print(f"В работе заказов: {len(active_orders)}")

        else:
            print("Неверное действие.")


def login_user():
    print("\n--- Вход в систему ---")
    input_login = input("Логин: ").strip()
    input_password = input("Пароль: ").strip()

    if input_login in users_db and users_db[input_login]["password"] == input_password:
        print("Успешный вход!")
        if input_login == "Admin":
            admin_account_menu()
        else:
            user_account_menu(input_login)
    else:
        print("Неверный логин или пароль.")


def main():
    load_database()
    load_menu()

    print("Добро пожаловать в новую умную пиццерию!")
    print("(Поддержка одновременных заказов и чеков)")

    while True:
        print("\n------- ГЛАВНОЕ МЕНЮ -------")
        print("0. Выход")
        print("1. Создать учётку")
        print("2. Изменить учётку")
        print("3. Удалить учётку")
        print("4. Войти в учетку")
        print("---------------------------")

        make = input("Выбери действие: ").strip()

        if make == "0":
            print("Программа завершена.")
            break
        elif make == "1":
            add_user()
        elif make == "2":
            change_user()
        elif make == "3":
            delete_user()
        elif make == "4":
            login_user()
        else:
            print("Повтори попытку")


if __name__ == "__main__":
    main()
