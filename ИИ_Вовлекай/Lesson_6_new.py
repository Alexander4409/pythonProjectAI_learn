# Замыкания
# def outer():
#     num = 5
#     def inner():
#         nonlocal num
#         num += 1
#         print(f"inner result - {num}")
#
#     return inner
#
#
# fu = outer()
#
# fu()
# fu()
# fu()
# fu()
# fu()

# применение параметров
# def mult(num):
#     def inner(num_2): return num*num_2
#
#     return inner
#
#
# fu = mult(5)
#
# print(fu(1))
# print(fu(2))
# print(fu(3))
# print(fu(4))

# Оптимизация

# def mult(num):return lambda num_1: num*num_1
#
#
# fu = mult(5)
#
# print(fu(1))
# print(fu(2))
# print(fu(3))
# print(fu(4))

#декораторы
# def select(input_func):
#     def output_func():
#         print("*"*10)
#         input_func()
#         print("*"*10)
#     return output_func
#
#
# @select
# def hi():
#     print("Hello user")
#
#
# @select
# def bye():
#     print("Good bye user")
#
#
# hi()
# bye()

# перехват параметров декоратором
# def check(input_func):
#     def output_func(*args):
#         name = args[0]
#         age = args[1]
#         if age <= 0 :
#             age = "Error !"
#         input_func(name,age)
#
#     return output_func
#
#
# @check
# def print_person(name,age):
#     print(f"user name - {name}, user age - {age}")
#
# print_person("Tom", 23)

#дз проверка объема двигателя и пробега автомобиля!!!

# получение результата функции
# def check(input_func):
#     def output_func(*args):
#         res = input_func(*args)
#         if res < 0:
#             res = "result is below 0 "
#         return res
#     return output_func
#
#
# @check
# def summ(num1, num2):
#     return num1+num2
#
#
# res_1 = summ(10,20)
# print(res_1)
#
# res_2 = summ(10, -20)
# print(res_2)

# встроенные декораторы

# from pydantic import validate_call
#
#
# @validate_call
# def process_data(num:int, name:str):
#     return f"{name}: {num*2}"
#
# print(process_data(5,"Test"))
# print(process_data("5","Test"))