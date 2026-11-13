#декораторы
# def decor(input_func):
#     def wrapper():
#         print("#"*30)
#         input_func()
#         print("#"*30)
#     return wrapper
#
#
# @decor
# def hello():
#     print("hello user")
#
#
# hello()


# def check_user_info(input_func):
#     def checker(*args):
#         name = args[0]
#         age = args[1]
#         if age <= 0:
#             age = "Error"
#         input_func(name,age)
#     return checker
#
#
# @check_user_info
# def create_user_info(name, age):
#     print(f'User name - {name}, user age - {age}')
#
# create_user_info("Tom", 34)
# create_user_info("Toby", -34)
#

# область видимости и замыкания

name = "Mary"

def say_name():
    global name
    name = "Bob"
    print(name)

def say_name1():
    print(name)
    def say_name2():
        print(name)
    return say_name2()


print(name)
say_name()
say_name1()

#существует некий идентификатор области видимости
# и параметр global делает контекст глобальным для всех функций вне и внутри их
