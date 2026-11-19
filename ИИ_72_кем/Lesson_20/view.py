from operator import itemgetter


def decor_func(input_func):
    def outer_func():
        print(25*"*")
        input_func()
        print(25*"*")
    return outer_func

@decor_func
def show_welcome():
    print(f"Робот пицца-мейкер запущен")

def show_menu():
    print("Выберите действие: \n"
          "1. Сделать новую пиццу \n"
          "2. Посмотреть статус и запасы робота\n"
          "3. Пополнить запасы робота\n"
          "0. Выключить робота")

@decor_func
def show_status(state):
    print('Текущий статус робота \n'
          f'Состояние - {state['status']}\n'
          f'Температура печи {state['temperature']}oC\n'
          f'Выполнено заказов {state["orders_completed"]}\n'
          f'Остатки ингредиентов :\n')
    for item, count in state["ingredients"].items():
        print(f'- {item.capitalize()}: {count} шт.')


def ask_menu_choice():
    return input("Ваш выбор").strip()


def ask_toppings(available_toppings):
    print(f'Доступные топпинги - {', ' .join(available_toppings)}\n'
          f'Введите нужные ингредиенты через запятую или нажмите enter для пропуска')
    raw_input = input("> ").strip().lower()

    if not raw_input:
        return []
    return [item.strip() for item in raw_input.split(",")]


def show_message(message):
    print(f"[Информация] - {message}")

def show