# ДЗ доделать робота пиццемейкера, добавить функцию отслеживания заказов

import json, os
from datetime import datetime

ORDERS_FILE, CASH_FILE, PWD = "orders.json", "cash.json", "admin"
KIDS_MENU = {"1": ("Мини-пицца", 150), "2": ("Сладкая", 200)}
ADULT_MENU = {"1": ("Пепперони", 450), "2": ("Маргарита", 400), "3": ("Мясная", 550)}

def cash_register():
    total = 0
    def add(amount):
        nonlocal total
        total += amount
        with open(CASH_FILE, 'w') as f: json.dump(total, f)
        return total
    def get(): return total
    def set_val(v): 
        nonlocal total; total = v
    return add, get, set_val

add_cash, get_cash, set_cash = cash_register()

def load_json(file, default):
    try:
        with open(file, 'r', encoding='utf-8') as f: return json.load(f)
    except: return default

def save_json(file, data):
    with open(file, 'w', encoding='utf-8') as f: json.dump(data, f, ensure_ascii=False)

def make_order():
    guests = int(input("Сколько гостей? ") or 1)
    total_bill, session_orders = 0, []
    
    for i in range(1, guests + 1):
        age = int(input(f"Возраст гостя {i}: "))
        menu = KIDS_MENU if age <= 12 else ADULT_MENU
        print("Меню:", ", ".join(f"{k}. {v[0]} ({v[1]}р)" for k, v in menu.items()))
        
        items, guest_total = [], 0
        while True:
            c = input("Выбор (номер или 0 для завершения): ").strip()
            if c == '0' and items: break
            if c in menu:
                name, price = menu[c]
                items.append({"name": name, "price": price})
                guest_total += price
                print(f"Добавлено: {name} ({price}р)")
                
        total_bill += guest_total
        session_orders.append({"guest": i, "age": age, "items": items, "total": guest_total, "time": datetime.now().strftime("%H:%M")})

    print(f"\nИТОГО: {total_bill} руб.")
    pay = input("Оплата (нал/карта): ").strip().lower()
    
    if 'нал' in pay:
        while True:
            try:
                given = float(input(f"Внесите сумму (мин. {total_bill}): ").replace(',', '.'))
                if given >= total_bill:
                    change = given - total_bill
                    print(f"Принято: {given:g} руб. Сдача: {change:g} руб.")
                    break
                else:
                    print(f"Недостаточно! Нужно ещё {total_bill - given:g} руб.")
            except ValueError:
                print("Ошибка: введите корректное число.")
    else:
        print("Оплата картой прошла успешно.")

    add_cash(total_bill)
    orders = load_json(ORDERS_FILE, [])
    orders.extend(session_orders)
    save_json(ORDERS_FILE, orders)
    print("Заказ сохранён!")

def admin_panel():
    if input("Введите пароль: ") != PWD:
        return print("Доступ запрещён.")
    
    while True:
        print("\n--- АДМИН-ПАНЕЛЬ ---")
        print("1. История заказов\n2. Общая выручка\n3. Выход")
        c = input("Выбор: ").strip()
        
        if c == '1':
            orders = load_json(ORDERS_FILE, [])
            if not orders: print("История пуста.")
            for o in orders:
                items_str = ", ".join(f"{i['name']} ({i['price']}р)" for i in o['items'])
                print(f"[{o['time']}] Гость {o['guest']} ({o['age']} лет): {items_str} | Итого: {o['total']}р")
        elif c == '2':
            print(f"Текущая выручка: {get_cash()} руб.")
        elif c == '3':
            break

def main():
    set_cash(load_json(CASH_FILE, 0))
    while True:
        print("\n=== РОБОТ-ПИЦМЕЙКЕР ===")
        print("1. Сделать заказ\n2. Панель администратора\n3. Выход")
        choice = input("Ваш выбор: ").strip()
        
        if choice == '1': make_order()
        elif choice == '2': admin_panel()
        elif choice == '3': break

if __name__ == "__main__":
    main()

Ивашко
