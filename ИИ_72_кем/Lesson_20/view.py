
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

def show_status(state):
    print('Текущий статус робота \n'
          f'Состояние - {state['status']}\n'
          f'Температура печи {state['temperature']}oC\n'
          f'Выполнено заказов {state["orders_completed"]}\n'
          f'Остатки ингредиентов :\n')
    for item, count in state["ingredients"].items():
        print(f'- {item.capitalize()}: {count} шт.')


