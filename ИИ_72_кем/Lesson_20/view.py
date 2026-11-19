def decor_func(input_func):
    def outer_func():
        print(10*"*")
        input_func()
        print(10*"*")
    return outer_func


def show_welcome():
    print(f" =  \n")