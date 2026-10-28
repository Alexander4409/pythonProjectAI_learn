import json
import sys
from datetime import datetime
import time
current_time = datetime.now()
try:
    import colorama
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    print(f'Модуль colorama не найден. Напишите в терминал\npip install colorama')
    sys.exit()

colorama.init()

ADMIN = False
password = '1234'

def start():
    print(Back.BLUE + Fore.WHITE + f'''           \_/             
          (* *)           
         __)#(__         
        ( )...( )(_)         
        || |_| ||//         
     >==() | | ()/     
         _(___)_         
        [-]   [-]        ''' + Style.RESET_ALL)
    print('='*10 + ' ' + 'Пиццерия робота v1' + ' ' + '='*10)

def load():
    global history_filename
    global history
    global commands
    global menu_dict
    global ADMIN
    history_filename = 'orders_history.json'
    history = {}
    try:
        with open(history_filename, 'r', encoding='utf-8') as f:
            history = json.load(f)
    except FileNotFoundError:
        with open(history_filename, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
        if ADMIN:    
            print(Fore.RED + f'[ERROR] Файл истории {history_filename} не найден. Создан новый' + Style.RESET_ALL)
    if ADMIN:
        commands = {'1': 'Сделать заказ', '2': 'Ознакомиться с меню', '3': 'Рестарт', '4': 'Сброс', '5': 'Обновить данные', '6': 'Посмотреть историю заказов', '7': 'Очистить историю заказов', '0': 'Выход'}
        print(Fore.BLUE + f'[INFO] Файл истории {history_filename} загружен' + Style.RESET_ALL)
    else:
        commands = {'1': 'Сделать заказ', '2': 'Ознакомиться с меню', '0': 'Выход'}
    menu_dict = {
        'Пепперони': {'category': 0, 'price': 350},
        'Маргарита': {'category': 0, 'price': 400},
        'Пицца 4 сыра': {'category': 0, 'price': 600},
        'Гавайская': {'category': 0, 'price': 450},
        'Мясная': {'category': 0, 'price': 500},
        'Вегетарианская': {'category': 0, 'price': 400},
        'Диабло': {'category': 0, 'price': 550},
        'Карбонара': {'category': 0, 'price': 480},
        'Вода 0.5л': {'category': 0, 'price': 70},
        'Кола 0.5л': {'category': 1, 'price': 150},
        'Фанта 0.5л': {'category': 1, 'price': 150},
        'Спрайт 0.5л': {'category': 1, 'price': 150},
        'Сок апельсиновый 0.3л': {'category': 0, 'price': 120},
        'Чай': {'category': 0, 'price': 100},
        'Кофе': {'category': 0, 'price': 150},
        'Картофель фри': {'category': 0, 'price': 150},
        'Наггетсы': {'category': 0, 'price': 200},
        'Сырные палочки': {'category': 0, 'price': 250},
        'Тирамису': {'category': 0, 'price': 300},
        'Чизкейк': {'category': 0, 'price': 280},
    }

def update_history(data={'time':'??:??', 'name':'Test', 'age':24, 'order':[], 'bill':0}):
    global order_num
    history[order_num] = data
    try:
        with open(history_filename, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
            with open(history_filename, 'w', encoding='utf-8') as f:
                json.dump(history, f, ensure_ascii=False, indent=4)
            if ADMIN:    
                print(Fore.RED + f'[ERROR] Файл истории {history_filename} не найден. Создан новый' + Style.RESET_ALL)
    if ADMIN:
            print(Fore.BLUE + f'[INFO] Файл истории {history_filename} обновлен' + Style.RESET_ALL)

load()

def init():
    global history_filename
    global history
    global commands
    global menu_dict
    global ADMIN
    global password
    commands = commands = {'1': 'Сделать заказ', '2': 'Ознакомиться с меню', '0': 'Выход'}
    menu_dict = {
            'Пепперони': {'category': 0, 'price': 350},
            'Маргарита': {'category': 0, 'price': 400},
            'Пицца 4 сыра': {'category': 0, 'price': 600},
            'Гавайская': {'category': 0, 'price': 450},
            'Мясная': {'category': 0, 'price': 500},
            'Вегетарианская': {'category': 0, 'price': 400},
            'Диабло': {'category': 0, 'price': 550},
            'Карбонара': {'category': 0, 'price': 480},
            'Вода 0.5л': {'category': 0, 'price': 70},
            'Кола 0.5л': {'category': 1, 'price': 150},
            'Фанта 0.5л': {'category': 1, 'price': 150},
            'Спрайт 0.5л': {'category': 1, 'price': 150},
            'Сок апельсиновый 0.3л': {'category': 0, 'price': 120},
            'Чай': {'category': 0, 'price': 100},
            'Кофе': {'category': 0, 'price': 150},
            'Картофель фри': {'category': 0, 'price': 150},
            'Наггетсы': {'category': 0, 'price': 200},
            'Сырные палочки': {'category': 0, 'price': 250},
            'Тирамису': {'category': 0, 'price': 300},
            'Чизкейк': {'category': 0, 'price': 280},
        }
    password = '1234'
    history = {}
    name = ''
    age = 0
    people = 0
    ADMIN = False
    try:
        with open(history_filename, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
    except Exception as e:
        if ADMIN:
            print(Fore.RED + f'[ERROR] Ошибка при создании файла: {history_filename}\n{e}' + Style.RESET_ALL)
    if ADMIN:
        print(Fore.BLUE + f'[INFO] Файл {history_filename} создан' + Style.RESET_ALL)

def menu():
    print(Back.BLUE + Fore.WHITE + f'\nМеню:' + Style.RESET_ALL)
    c = 0
    for item in menu_dict.items():
        c += 1
        if item[1]["category"] == 0:
            print(Back.CYAN + Fore.BLACK + f'{c} - {item[0]} ........ {item[1]["price"]}₽' + Style.RESET_ALL)
        else:
            print(Back.CYAN + Fore.BLACK + f'{c} - {item[0]} ........ {item[1]["price"]}₽' + Style.RESET_ALL + ' ' + Back.BLACK + Fore.RED + '18+' + Style.RESET_ALL)
    print()   

def interface():
    global history_filename
    global history
    global commands
    global ADMIN
    global password
    global name
    global age
    global people
    global order
    global order_num
    global bill
    print('Выберите действие из перечисленных (напишите соответсвующее число):')
    for c in range(len(commands.items())):
        print(f'{c} - {commands[str(c)]}')
    try:
        inp = str(input('>>> '))
    except KeyboardInterrupt:
        inp = '0'
    if inp == '1':
        print('Пожалуйста, представьтесь')
        name = input('>>> ')
        print(f'Приятно познакомиться, {name}. Какой ваш возраст?')
        while True:
            try:
                age = int(input('>>> '))
                break
            except:
                if ADMIN:
                    print(Fore.RED + '[ERROR] Введите целое число!' + Style.RESET_ALL)
                else:
                    print('Введите целое число!')
        if age < 6:
            print('Извините, но вы еще не можете совершать покупки в силу своего возраста')
            return
        if age > 150:
            print('Извините, но ваш возраст не соответствует нашим условиям')
            return
        print('Вы заказываете только для себя? (Y/n)')
        try:
            alone_inp = input('>>> ').strip().lower()
        except KeyboardInterrupt:
            alone_inp = 'y'
        if alone_inp.lower() in ('y', 'yes', 'да', ''):
            people = 1
            print('Отлично, заказ для одного человека.')
        else:
            print('На сколько человек вы заказываете?')
            while True:
                try:
                    people = int(input('>>> '))
                    if people < 1:
                        raise ValueError
                    break
                except:
                    if ADMIN:
                        print(Fore.RED + '[ERROR] Введите целое число больше 0!' + Style.RESET_ALL)
                    else:
                        print('Введите целое число больше 0!')

        order = []
        bill = 0
        menu_items = list(menu_dict.items())
        menu()
        print(f'{len(menu_items) + 1} - Завершить выбор и перейти к оплате')
        while True:
            print(Fore.YELLOW + f'Текущая сумма: {bill}₽' + Style.RESET_ALL)
            try:
                choice = input('Выберите номер позиции: ').strip()
                if menu_items[int(choice)-1][1]["category"] == 1 and age < 18:
                    print('Так как вы несовершеннолетний, вы не можете заказать эту позицию.')
                    continue
            except:
                choice = str(len(menu_items) + 1)
            if choice == str(len(menu_items) + 1):
                break
            try:
                idx = int(choice) - 1
                if idx < 0 or idx >= len(menu_items):
                    raise ValueError
            except:
                if ADMIN:
                    print(Fore.RED + '[ERROR] Неверный номер позиции' + Style.RESET_ALL)
                else:
                    print('Неверный номер позиции')
                continue
            item_name = menu_items[idx][0]
            item_price = menu_items[idx][1]['price']
            print(f'Сколько порций "{item_name}" добавить?')
            while True:
                try:
                    qty = int(input('>>> '))
                    if qty < 1:
                        raise ValueError
                    break
                except:
                    if ADMIN:
                        print(Fore.RED + '[ERROR] Введите целое число больше 0!' + Style.RESET_ALL)
                    else:
                        print('Введите целое число больше 0!')
            found = False
            for o in order:
                if o['name'] == item_name:
                    o['quantity'] += qty
                    found = True
                    break
            if not found:
                order.append({'name': item_name, 'price': item_price, 'quantity': qty})
            bill += item_price * qty
            print(Fore.GREEN + f'Добавлено: {item_name} x{qty}. Сумма: {bill}₽' + Style.RESET_ALL)

        if not order:
            if ADMIN:
                print(Fore.YELLOW + '[WARN] Вы не выбрали ни одной позиции. Заказ отменён' + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + 'Вы не выбрали ни одной позиции. Заказ отменён' + Style.RESET_ALL)
            return

        print(f'\nСумма к оплате: {bill}₽')
        print('Выберите способ оплаты: 1 - наличные, 2 - банковская карта')
        while True:
            try:
                pay_inp = input('>>> ').strip()
            except KeyboardInterrupt:
                pay_inp = '1'
            if pay_inp == '1':
                while True:
                    print('Заплатите сумму чека:')
                    try:
                        payed = int(input('>>> '))
                        if payed == bill:
                            print(Fore.GREEN + 'Оплата наличными принята. Спасибо!' + Style.RESET_ALL)
                            break
                        elif payed > bill:
                            print(Fore.GREEN + f'Оплата наличными принята. Спасибо! Ваша сдача: {payed - bill}₽' + Style.RESET_ALL)
                            break
                        else:
                            print('Недостаточно средств!')
                    except:
                        if ADMIN:
                            print(Fore.RED + '[ERROR] Введите целое число!' + Style.RESET_ALL)
                        else:
                            print('Введите целое число!')
                break
            elif pay_inp == '2':
                print(Fore.GREEN + 'Оплата банковской картой принята. Спасибо!' + Style.RESET_ALL)
                break
            else:
                if ADMIN:
                    print(Fore.RED + '[ERROR] Введите 1 или 2' + Style.RESET_ALL)
                else:
                    print('Введите 1 или 2')

        try:
            if int(list(history.keys())[-1])+1 < 9999:
                order_num = int(list(history.keys())[-1])+1
            else:
                order_num = 1
        except:
            order_num = 1

        order_time = str(datetime.now())
        update_history({'time': order_time, 'name': name, 'age': age, 'order': order, 'bill': bill})
        if ADMIN:
            print(Fore.GREEN + f'[ORDER] Заказ на имя {name} ({age} лет, на {people} чел.) оформлен. Сумма чека: {bill}₽, номер заказа - {order_num}' + Style.RESET_ALL)
        else:
            print(Fore.GREEN + f'Заказ на имя {name} ({age} лет, на {people} чел.) оформлен. Сумма чека: {bill}₽, номер заказа - {order_num}' + Style.RESET_ALL)

        print('Ожидайте, ваш заказ готовится...')
        try:
            time.sleep(10)
        except KeyboardInterrupt:
            pass
        print(Fore.GREEN + f'\nЗаказ №{order_num} готов! Ваши позиции:' + Style.RESET_ALL)
        for o in order:
            print(Fore.GREEN + f'  {o["name"]} x{o["quantity"]} — {o["price"] * o["quantity"]}₽' + Style.RESET_ALL)
        print(Fore.GREEN + f'Итого: {bill}₽. Приятного аппетита, {name}!' + Style.RESET_ALL)
    elif inp == '2':
            menu()
    elif inp == '3' and ADMIN:
        print(Fore.BLUE + '[INFO] Перезапуск...' + Style.RESET_ALL)
        load()
        start()
    elif inp == '4' and ADMIN:
            print(Fore.YELLOW + '[WARN] Вы точно хотите сбросить всё? (Y/n)' + Style.RESET_ALL)
            inp2 = input('>>> ')
            if inp2.lower() in ('y', 'yes', 'да'):
                print(Fore.BLUE + '[INFO] Сброс данных...' + Style.RESET_ALL)
                init()
    elif inp == '5' and ADMIN:
            print(Fore.BLUE + '[INFO] Обновление данных...' + Style.RESET_ALL)
            load()
    elif inp == '6' and ADMIN:
            if history == {}:
                print(Fore.BLUE + '[INFO] История заказов пуста' + Style.RESET_ALL)
            else:
                print(Back.BLUE + Fore.WHITE + f'\nИстория заказов:' + Style.RESET_ALL)
                lines = []
                for num, data in history.items():
                    lines.append(f'Заказ №{num}')
                    lines.append(f'  Время: {data.get("time", "??")}')
                    lines.append(f'  Имя: {data.get("name", "??")}, возраст: {data.get("age", "??")}')
                    lines.append(f'  Позиции:')
                    for item in data.get('order', []):
                        lines.append(f'    - {item.get("name", "??")} x{item.get("quantity", 1)} — {item.get("price", 0) * item.get("quantity", 1)}₽')
                    lines.append(f'  Сумма чека: {data.get("bill", 0)}₽')
                    lines.append('')
                history_str = '\n'.join(lines)
                if len(history_str) < 500:
                    print(history_str)
                else:
                    print(Fore.YELLOW + '[WARN] История заказов слишком большая. Будут показаны первые 500 символов (Y/n)' + Style.RESET_ALL)
                    print(history_str[:500])
                print()
    elif inp == '7' and ADMIN:
            print(Fore.YELLOW + '[WARN] Вы точно хотите очистить историю заказов? (Y/n)' + Style.RESET_ALL)
            try:
                inp2 = input('>>> ')
            except KeyboardInterrupt:
                pass
            if inp2.lower() in ('y', 'yes', 'да'):
                history = {}
                print(Fore.BLUE + f'[INFO] Переменная истории очищена' + Style.RESET_ALL)
                try:
                    with open(history_filename, 'w', encoding='utf-8') as f:
                        json.dump(history, f, ensure_ascii=False, indent=4)
                except Exception as e:
                    print(Fore.RED + f'[ERROR] Ошибка при очистке файла: {history_filename}\n{e}' + Style.RESET_ALL)
                print(Fore.BLUE + f'[INFO] Файл {history_filename} очищен' + Style.RESET_ALL)
    elif inp == '0':
        if ADMIN:
            print(Fore.YELLOW + '[WARN] Вы точно хотите выйти? (Y/n)' + Style.RESET_ALL)
            try:
                inp2 = input('>>> ')
            except KeyboardInterrupt:
                print(Fore.BLUE + '[INFO] Завершение работы файла...' + Style.RESET_ALL)
                sys.exit()
            if inp2.lower() in ('y', 'yes', 'да'):
                print(Fore.BLUE + '[INFO] Завершение работы файла...' + Style.RESET_ALL)
                sys.exit()
        else:
            print('Вы точно хотите выйти? (Y/n)')
            try:
                inp2 = input('>>> ')
            except KeyboardInterrupt:
                print('До свидания!')
                sys.exit()
            if inp2.lower() in ('y', 'yes', 'да'):
                print('До свидания!')
                sys.exit()
    elif inp == '/admin' or inp == '/adm':
        if ADMIN:
            print(Fore.BLUE + '[INFO] Выход из режима администратора...' + Style.RESET_ALL)
            commands = {'1': 'Сделать заказ', '0': 'Выход'}
            ADMIN = False
        else:
            inp2 = str(input('Введите пароль: '))
            if inp2 == password:
                ADMIN = True
                print(Fore.BLUE + '[INFO] Права администратора получены' + Style.RESET_ALL)
                commands = {'1': 'Сделать заказ', '2': 'Ознакомиться с меню', '3': 'Рестарт', '4': 'Сброс', '5': 'Обновить данные', '6': 'Посмотреть историю заказов', '7': 'Очистить историю заказов', '0': 'Выход'}
            else:
                print('Неверный пароль')
    elif inp == '':
        pass
    else:
        if ADMIN:
            print(Fore.RED + '[ERROR] Неизвестная команда' + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Неизвестная команда' + Style.RESET_ALL)

start()
while True:
    try:
        interface()
    except Exception as e:
        if ADMIN:
            print(Fore.RED + f'[ERROR] Произошла неизвестная ошибка: {e}' + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Произошла неизвестная ошибка.' + Style.RESET_ALL)
