#декораторы
# def decor(input_func):
#     def output_func():
#         print("#"*36)
#         input_func()
#         print("#"*36)
#     return output_func
#
# @decor
# def hello():
#     print("hello User")
#
#
# hello()


def check_age(input_func):
    def wrapper_check(*args):
        name = args[0]
        age = args[1]
        if age < 0:
            age = "Error"
        input_func(name,age)
    return wrapper_check


@check_age
def crete_user(name,age):
    print(f"User name - {name}, user age - {age}")


crete_user("Tom", 34)
crete_user("Kenny", -21)
