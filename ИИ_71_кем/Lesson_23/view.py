def decor(input_func):
    def output_func():
        print(25 * "*")
        input_func()
        print(25 * "*")
    return output_func


@decor
def show_welcome():
    print("РОБОТ ПИЦЦЕМЕЙКЕР ЗАПУЩЕН")

@decor
def show_menu():
    print(f"Выберите действие : \n"
          f"1 - Cделать новую пиццу \n"
          f"2 - Посмотреть статус и запасы \n"
          f"3 - Пополнить запасы продуктов \n"
          f"0 - Выключить робота ")

@decor
def show_status(state):
    print(f"___ТЕКУЩИЙ СТАТУС РОБОТА___\n"
          f"Состояние - {state["status"]}\n"
          f"Температура - {state["temperature"]} oC\n"
          f"Выполнено заказов - {state["orders_completed"]}\n"
          f"Остатки ингредиентов -")
    for item, count in state["ingredients"].item():
        print(f' - {item.capitalize()} : {count} ед.')


def ask_menu_choice():
    return input("Ваш выбор - ").split()


def ask_toppings(available_toppings):
    print()

