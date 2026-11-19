def decor_func(input_func):
    def outer_func():
        print(25*"*")
        input_func()
        print(25*"*")
    return outer_func

@decor_func
def show_welcome():
    print(f"Робот пиццемейкер запущен")

def show_menu():
    print("Выберите действие: \n"
          "1. Сделать новую пиццу"
          "2. Посмотреть статус и запасы робота"
          "3. пополнить запасы робота"
          "0. Выключить робота")

