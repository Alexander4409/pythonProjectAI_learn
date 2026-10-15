import time

adult_menu = [
    {0: "Том Ям — 650 руб."},
    {1: "Борщ с говядиной — 450 руб."},
    {2: "Французский луковый суп — 490 руб."},
    {3: "Стейк Рибай — 2400 руб."},
    {4: "Филе-миньон — 1900 руб."},
    {5: "Лосось на гриле — 950 руб."},
    {6: "Утиная грудка су-вид — 850 руб."},
    {7: "Паста Карбонара — 550 руб."},
    {8: "Салат Капрезе — 480 руб."},
    {9: "Тартар из тунца — 690 руб."},
    {10: "Салат с козьим сыром — 580 руб."},
    {11: "Тирамису — 380 руб."},
    {12: "Фондан с матчей — 420 руб."}
]

kids_menu = [
    {0: "Суп-буквы с курицей — 250 руб."},
    {1: "Крем-суп из тыквы — 280 руб."},
    {3: "Сырный крем-суп — 310 руб."},
    {4: "Домашние наггетсы — 290 руб."},
    {5: "Mini-бургеры — 380 руб."},
    {6: "Котлетки-зайки на пару — 320 руб."},
    {7: "Рыбные треугольники — 340 руб."},
    {8: "Сырные палочки — 280 руб."},
    {9: "Макароны-бантики с сыром — 240 руб."},
    {10: "Овощные палочки — 190 руб."},
    {11: "Фруктовые шпажки — 220 руб."},
    {12: "Блинчики с нутеллой — 260 руб."},
    {13: "Творожная запеканка — 210 руб."}
]

drinks_menu = [
    {0: "Чай Матча Латте — 280 руб."},
    {1: "Лимонад Розмарин-Грейпфрут — 350 руб."},
    {2: "Какао с маршмеллоу — 230 руб."},
    {3: "Молочный коктейль — 270 руб."},
    {4: "Яблочный компот — 120 руб."},
    {5: "Детский мохито — 250 руб."},
    {6: "Банановый смузи — 290 руб."}
]


def get_price(menu_prices, item_id):
    for d in menu_prices:
        if item_id in d:
            return d[item_id]
    return 0


adult_prices = [{0: 650}, {1: 450}, {2: 490}, {3: 2400}, {4: 1900}, {5: 950}, {6: 850}, {7: 550}, {8: 480}, {9: 690},
                {10: 580}, {11: 380}, {12: 420}]
kids_prices = [{0: 250}, {1: 280}, {2: 310}, {3: 290}, {4: 380}, {5: 320}, {6: 340}, {7: 280}, {8: 240}, {9: 190},
               {10: 220}, {11: 260}, {12: 210}]
drinks_prices = [{0: 280}, {1: 350}, {2: 230}, {3: 270}, {4: 120}, {5: 250}, {6: 290}]

num_adults = int(input("Здравствуйте! Спасибо, что пришли, подскажите, сколько в вашей компании взрослых: "))
num_children = int(input("И скажите, пожалуйста, сколько у вас детей: "))
table = int(input("И еще, бронировали ли вы столик, если да, то какой, если нет, то напишите 0: "))

total_price = 0
total_items_count = 0

if num_adults == 0:
    print("Извините, мы обслуживаем людей, только если присутствуют взрослые")

elif num_children == 0:
    print()
    print("взрослое меню -", adult_menu)
    print()
    print("напитки -", drinks_menu)

    print("\nВведите через пробел или запятую ID блюд из взрослого меню, которые хотите заказать:")
    only_adult_order_input = input()
    only_adult_order = list(map(int, only_adult_order_input.replace(',', ' ').split()))

    print("\nВведите через пробел или запятую ID напитков, которые хотите заказать (если не нужно, нажмите Enter):")
    drinks_order_input = input()
    drinks_order = list(map(int, drinks_order_input.replace(',', ' ').split())) if drinks_order_input.strip() else []


    for item_id in only_adult_order:
        total_price += get_price(adult_prices, item_id)
        total_items_count += 1
    for item_id in drinks_order:
        total_price += get_price(drinks_prices, item_id)
        total_items_count += 1

elif num_children != 0 and num_adults != 0:
    print()
    print("взрослое меню -", adult_menu)
    print()
    print("детское меню -", kids_menu)
    print()
    print("напитки -", drinks_menu)

    print("Введите через пробел или запятую номер блюд из взрослого меню:")
    adult_order_input = input()
    adult_order = list(map(int, adult_order_input.replace(',', ' ').split())) if adult_order_input.strip() else []

    print("Введите через пробел или запятую номер блюд из детского меню:")
    kids_order_input = input()
    kids_order = list(map(int, kids_order_input.replace(',', ' ').split())) if kids_order_input.strip() else []

    print("Введите через пробел или запятую номер напитков:")
    drinks_order_input = input()
    drinks_order = list(map(int, drinks_order_input.replace(',', ' ').split())) if drinks_order_input.strip() else []


    for item_id in adult_order:
        total_price += get_price(adult_prices, item_id)
        total_items_count += 1
    for item_id in kids_order:
        total_price += get_price(kids_prices, item_id)
        total_items_count += 1
    for item_id in drinks_order:
        total_price += get_price(drinks_prices, item_id)
        total_items_count += 1


if num_adults > 0 and total_items_count > 0:
    print(f"Общая сумма вашего заказа: {total_price} руб.")


    waiting_minutes = total_items_count * 1
    real_delay_seconds = waiting_minutes * 5

    print(f"Время ожидания вашего заказа составит {waiting_minutes} минут.")
    print("Приступаем к готовке")
    time.sleep(real_delay_seconds)
    print("Ваш заказ готов!")


    payment_method = input("\nЧем будете оплачивать? (напишите 'наличными' или 'картой'): ").strip().lower()

    if payment_method == "наличными":
        user_money = int(input("Введите сумму денег, которую вы даете: "))
        if user_money >= total_price:
            change = user_money - total_price
            print(f"Спасибо за оплату! Ваша сдача: {change} руб.")
        else:
            print("Этих денег недостаточно для оплаты заказа.")
    else:
        print("Оплата картой прошла успешно! Спасибо, что посетили нас!")
