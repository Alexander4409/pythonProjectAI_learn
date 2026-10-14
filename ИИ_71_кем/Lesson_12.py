#замыкания
def outer():
    num = 5

    def inner ():
        nonlocal num
        num +=1
        print(num)

    return inner

fu = outer()

fu()
fu()
fu()
fu()
fu()
fu()
fu()
fu()

#задача написать робота пицемейкера
# робот должен принимать заказ от пользователя (учитывать что пользователь может придти не один)
# робот должен предоставить разное меню для разновозрастных пользователей, после идентификации
# пользователя и определения тех позиций которые пользователь хочет купить робот должен спросить,
# как будет проходить оплата (наличнкой или кртой) в случии налички
# пользователь вводит число боле суммы, а робот выдает сдачу
def robot_cash_register():
    total = 0
    def add_money(amount):
        nonlocal total
        total += amount
        print(f"[Касса] +{amount} руб. Итого: {total} руб.")
        return total
    return add_money

update_cash = robot_cash_register()

# Склад ингредиентов
stock = {
    "тесто": 10, "сыр": 30, "пепперони": 8, "томаты": 12,
    "ветчина": 10, "грибы": 15, "ананас": 6, "колбаса": 10, "нутелла": 5
}

# История заказов
orders_history = []

# Базовое меню: (название, цена, необходимые ингредиенты)
BASE_MENU = {
    "1": ("Маргарита",       400, {"тесто": 1, "сыр": 3, "томаты": 2}),
    "2": ("Пепперони",       450, {"тесто": 1, "сыр": 3, "пепперони": 3}),
    "3": ("Ветчина и грибы", 500, {"тесто": 1, "сыр": 3, "ветчина": 2, "грибы": 2}),
    "4": ("Гавайская",       480, {"тесто": 1, "сыр": 3, "ветчина": 2, "ананас": 2}),
    "5": ("Мясная",          550, {"тесто": 1, "сыр": 3, "пепперони": 2, "колбаса": 2}),
    "6": ("Сладкая",         200, {"тесто": 1, "нутелла": 2}),
}

# Размеры пиццы: (множитель цены, множитель ингредиентов)
SIZES = {"1": ("Маленькая", 1.0, 1.0), "2": ("Средняя", 1.3, 1.3), "3": ("Большая", 1.6, 1.7)}

def get_available_menu(age):
    """Возвращает меню только из тех пицц,.ingredients которых есть на складе."""
    available = {}
    for key, (name, price, ingredients) in BASE_MENU.items():
        # Проверяем, хватает ли всех ингредиентов
        if all(stock.get(ing, 0) >= need for ing, need in ingredients.items()):
            if age <= 12 and name not in ("Маргарита", "Сладкая"):
                continue  # детям — только детское меню
            available[key] = (name, price, ingredients)
    return available

def choose_size():
    print("\nВыберите размер:")
    for k, (n, pm, im) in SIZES.items():
        print(f"  {k}. {n} (цена x{pm})")
    while True:
        s = input("Размер (1/2/3): ")
        if s in SIZES: return s
        print("Нет такого размера.")

def pizza_robot():
    print("Привет! Я робот-пицмейкер.")
    while True:
        try:
            guests = int(input("Сколько вас? "))
            if guests > 0: break
        except ValueError: pass

    total_bill = 0
    for i in range(1, guests + 1):
        print(f"\n--- Гость {i} ---")
        while True:
            try:
                age = int(input("Ваш возраст: "))
                if age > 0: break
            except ValueError: pass

        menu = get_available_menu(age)
        if not menu:
            print("К сожалению, ничего нет в наличии.")
            continue

        print("\nМеню в наличии:")
        for k, (n, p, _) in menu.items():
            print(f"  {k}. {n} - {p} руб.")

        guest_order = []  # список заказов гостя
        guest_total = 0

        while True:
            c = input("\nЗаказ (номер или 0 - конец): ")
            if c == '0':
                if not guest_order: 
                    print("Выберите хотя бы одну пиццу.")
                    continue
                break
            if c not in menu:
                print("Нет такого пункта.")
                continue

            name, base_price, ingredients = menu[c]
            size = choose_size()
            size_name, price_mult, ingr_mult = SIZES[size]

            # Проверяем склад с учётом размера
            needed = {ing: round(need * ingr_mult) for ing, need in ingredients.items()}
            if not all(stock.get(ing, 0) >= need for ing, need in needed.items()):
                print(f"Не хватает ингредиентов для {name} размера '{size_name}'.")
                continue

            final_price = int(base_price * price_mult)

            # Снимаем ингредиенты со склада
            for ing, need in needed.items():
                stock[ing] -= need

            guest_order.append({"пицца": name, "размер": size_name, "ингредиенты": needed, "цена": final_price})
            guest_total += final_price
            print(f"Добавлено: {name} ({size_name}) - {final_price} руб.")

        print(f"\nИтог по гостю {i}: {guest_total} руб.")
        total_bill += guest_total

        # Сохраняем заказ в историю
        orders_history.append({"гость": i, "возраст": age, "заказ": guest_order, "сумма": guest_total})

    print(f"\nОбщий счет: {total_bill} руб.")
    while True:
        pay = input("Оплата (наличные/карта): ").strip().lower()
        if pay in ['наличные', 'нал']: is_cash = True; break
        if pay in ['карта', 'картой']: is_cash = False; break

    if is_cash:
        while True:
            try:
                given = float(input(f"Внесите сумму (не менее {total_bill}): "))
                if given >= total_bill:
                    print(f"Сдача: {given - total_bill} руб.")
                    update_cash(total_bill)
                    break
            except ValueError: pass
    else:
        print("Оплата картой принята.")
        update_cash(total_bill)

    print("Спасибо! Пицца готовится.")

    # Отчёт после заказа
    print("\n=== Остатки на складе ===")
    for ing, count in stock.items():
        print(f"  {ing}: {count}")

    print("\n=== История заказов ===")
    for order in orders_history:
        print(f"Гость {order['гость']} (возраст {order['возраст']}):")
        for item in order['заказ']:
            print(f"  - {item['пицца']} ({item['размер']}), ингредиенты: {item['ингредиенты']}, {item['цена']} руб.")
        print(f"  Сумма: {order['сумма']} руб.")

pizza_robot()
