#пишем переменные осмысленно
# devochky
# malchiky - так не делаем!!!
# используем для переменных анлгийские слова
# lst_1 = [1,3,2,"hi"]
#low_snake_case
#классы и их имена - HiCamelCase
# def test_memory():
#     num = 10
#     print(id(num))
#
# test_memory()

# читать - https://metanit.com/python/tutorial/1.1.php

# =========================================================================================================================================
# я Ярослав Борблик. как я понял, код сюда вставлять про Робота Пиццемейкера
# вот:

# import time
# import json

# def admin_panel():
#     password = input('Введите пароль администратора: ')
#     if password != 'Zhjckfd0316':
#         print('Неверный пароль!')
#         return
#     try:
#         with open('orders.json', 'r', encoding='utf-8') as file:
#             orders = json.load(file)
#     except FileNotFoundError:
#         orders = []
#     if len(orders) == 0:
#         print('Заказов пока нет.')
#     else:
#         print('История всех заказов:')
#         number = 1
#         for order in orders:
#             print(f'\n=========Заказ№{number}=========')
#             for name, price in order['products']:
#                 print(f'{name} — {price} руб.')
#             print(f"Сумма: {order['total']} руб.")
#             print(f"Оплата: {order['payment']}")
#             print(f"Внесено: {order['money']} руб.")
#             print(f"Сдача: {order['change']} руб.")
#             number += 1

# def print_dict(dict):
#     for key, value in dict.items():
#         cut = value.split(';')
#         print(f'{key}) {cut[0]} - {cut[1]} руб.')
# ingredients = {'1': 'грибы;45',
#                 '2': 'пепперони;25',
#                 '3': 'ананасы;60',
#                 '4': 'оливки;30',
#                 '5': 'сыр;10',
#                 '6': 'баклажаны;65',
#                 '7': 'болгарский перец;50',
#                 '8': 'сосиски;40',
#                 '9': 'томаты;30',
#                 '10': 'сок яблочный/апельсиновый;150',
#                 '11': 'пепперони;90',
#                 '12': 'ветчина;65',
#                 '13': 'бекон;80',
#                 '14': 'курица;70',
#                 '15': 'ананасы;55',
#                 '16': 'маслины;45',
#                 '17': 'болгарский перец;35',
#                 '18': 'помидоры черри;40',
#                 '19': 'моцарелла;75',
#                 '20': 'пармезан;85',
#                 '21': 'кукуруза;30',
#                 '22': 'маринованные огурцы;35',
#                 '23': 'красный лук;25',
#                 '24': 'охотничьи колбаски;85',
#                 '25': 'говядина;100',
#                 '26': 'шпинат;40',
#                 '27': 'халапеньо;35',
#                 '28': 'фета;70',
#                 '29': 'артишоки;65',
#                 '30': 'соус барбекю;45'
#                }
# alco_menu = {'31': 'водка 0.5;400',
#             '32': 'вино красное/белое;800',
#             '33': 'коньяк;650',
#             '34': 'джин;500',
#             '35': 'виски;550',
#             '36': 'ром;700',
#             '37': 'шампансое;375',
#             '38': 'текила;600',
#             '39': 'пиво;250',
#             '40': 'ликёр;570'}
# def make_order():
#     print('Рады видеть вас в нашем ресторане! Предлагаем вам наши ингредиенты к пицце и алко напитки: ')
#     peoples = int(input('Сколько пицц хотите заказать? '))
#     total = 0
#     user_order = []
#     for q in range(1, peoples + 1):
#         user_age = int(input('И скажите, сколько вам лет? '))
#         print('Меню ингредиентов для пиццы:')
#         print_dict(ingredients)
#         if user_age <= 0:
#             print('Неверная дата возраста.')
#             break
#         if user_age >= 18:
#             print('Вы взрослые, даём алко меню: ')
#             print_dict(alco_menu)
#         while True:
#             order = input('Ваш заказ (напишите номер игридиента через пробел): ').split()
#             if order == ['0']:
#                 break
#             all_menu = ingredients
#             if user_age >= 18:
#                 all_menu = {**ingredients, **alco_menu}
#             val = True
#             for choice in order:
#                 if choice not in all_menu:
#                     val = False
#             if val:
#                 for num in order:
#                     if num == '0':
#                         continue
#                     product_info = all_menu[num].split(';')
#                     name = product_info[0]
#                     price = int(product_info[1])
#                     total += price
#                     user_order.append((name, price))
#                 break
#             print('Ошибка. Повторите заказ.')
#             for num in order:
#                 if num == '0':
#                     continue
#                 product_info = all_menu[num].split(';')
#                 name = product_info[0]
#                 price = int(product_info[1])
#                 total += price
#                 user_order.append((name, price))
#     print('Ваш заказ: ')
#     if len(user_order) == 0:
#         print('Вы ничего не заказали.')
#     else:
#         for name, price in user_order:
#             print(f'{name} — {price} руб.')
#     print('')
#     print(f'Общая сумма: {total} руб.')
#     if total > 0:
#         print('Выберите способ оплаты:')
#         print('1 — наличными')
#         print('2 — картой')
#         payment = input('Ваш выбор: ')
#         while payment != '1' and payment != '2':
#             print('Ошибка! Выберите способ оплаты ещё раз.')
#             payment = input('Ваш выбор: ')
#         if payment == '1':
#             money = int(input('Введите сумму, которую даёте: '))
#             while money < total:
#                 print('Недостаточно денег!')
#                 print(f'Не хватает {total - money} руб.')
#                 money = int(input('Введите сумму ещё раз: '))
#             change = money - total
#             print(f'Вот ваша сдача: {change} руб.')
#             payment_method = 'Наличными'
#         else:
#             input('Приложите к карту к терминалу: (нажмите Enter, чтобы продолжить...)')
#             time.sleep(2.5)
#             print('Оплата успешно выполнена!')
#             payment_method = 'Карта'
#             money = total
#             change = 0
#         print('Спасибо за заказ! Приятного аппетита!')
#         order_data = {
#             'products': user_order,
#             'total': total,
#             'payment': payment_method,
#             'money': money,
#             'change': change
#         }
#         try:
#             with open('orders.json', 'r', encoding='utf-8') as file:
#                 orders = json.load(file)
#         except FileNotFoundError:
#             orders = []
#         orders.append(order_data)
#         with open('orders.json', 'w', encoding='utf-8') as file:
#             json.dump(orders, file, ensure_ascii=False, indent=4)
#         print('Заказ сохранён!')
#     else:
#         print('Спасибо, что заглянули к нам!')
# print('1 — Войти в панель администратора')
# print('2 — Сделать заказ')
# print('3 — Выход из программы')
# choice = input('Ваш выбор: ')
# if choice == '1':
#     admin_panel()
# elif choice == '2':
#     make_order()
# elif choice == '3':
#     print('До свидания!')
# else:
#     print('Неверный выбор.')
