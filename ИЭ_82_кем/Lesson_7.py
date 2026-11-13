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


def check_user_info(input_func):
    def checker(*args):
        name = [0]
        age = [1]
        if age <= 0:
            age = "Error"
        input_func(name,age)
    return checker


@check_user_info
def create_user_info(name, age):
    print(f'User name - {name}, user age - {age}')

create_user_info("Tom", 34)
create_user_info("Toby", -34)
