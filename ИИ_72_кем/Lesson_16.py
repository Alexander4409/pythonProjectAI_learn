# декораторы
def decor_func(input_func):
    def outer_func():
        print(10*"*")
        input_func()
        print(10*"*")
    return outer_func

@decor_func
def say_hi():
    print("Hi")

@decor_func
def say_bye():
    print("bye")


say_hi()
say_bye()