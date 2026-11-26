def decor(input_func):
    def output_func():
        print(25 * "*")
        input_func()
        print(25 * "*")
    return output_func


@decor
def show_welcome():
    print("РОБОТ ПИЦЦЕМЕЙКЕР ЗАПУЩЕН")


show_welcome()