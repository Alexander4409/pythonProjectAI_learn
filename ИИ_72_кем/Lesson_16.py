# декораторы
# def decor_func(input_func):
#     def outer_func():
#         print(10*"*")
#         input_func()
#         print(10*"*")
#     return outer_func
#
# @decor_func
# def say_hi():
#     print("Hi")
#
# @decor_func
# def say_bye():
#     print("bye")
#
#
# say_hi()
# say_bye()

# def check_age(input_func):
#     def output_func(*args):
#         name = args[0]
#         age = args[1]
#         if age < 0: age = "Error"
#         input_func(name,age)
#     return output_func
#
#
# @check_age
# def print_person(name, age):
#     print(f"Name - {name}, Age - {age}")
#
#
# print_person("Bob", 12)
# print_person("Jeffry", 45)
# print_person("Marry", 23)
# print_person("Dory", -9999)


# генераторы и генераторные функции
#yield вместо return

# def lazy_counter(max):
#     count = 0
#     while count <= max:
#         yield count
#         count += 1
#
# gen = lazy_counter(3)
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def get_nums_return(num):
#     res = []
#     for i in range(num):
#         res.append(i)
#     return res
#
# first_list = get_nums_return(10000000)
#
# print(first_list)

# def get_nums_yield(num):
#     for i in range(num):
#         yield i
#
# first_list = get_nums_yield(1000000)
#
# print(next(first_list))
# print(next(first_list))
# print(next(first_list))
# print(next(first_list))
# print(next(first_list))
# print(next(first_list))
# print(next(first_list))

#Ассинхронное программирование

# import time
#
# def func1(num):
#     print(num**2)
#     time.sleep(3)
#     print("Func1 - complete")
#
#
# def func2(num):
#     print(num**0.9)
#     time.sleep(3)
#     print("Func2 - complete")
#
#
# def main():
#     func1(4)
#     func2(4)
#
# print(time.strftime("%X"))
# main()
# print(time.strftime("%X"))


import time
import asyncio


async def func1(num):
    print(num**2)
    await asyncio.sleep(3)
    print("func1 - complete")


async def func2(num):
    print(num**0.9)
    await asyncio.sleep(3)
    print("func2 - complete")

async def main():
    task1 = asyncio.create_task(func1(4))
    task2 = asyncio.create_task(func2(4))

    await task1
    await task2

print(time.strftime("%X"))
asyncio.run(main())
print(time.strftime("%X"))

# 18:17:46
# 16
# Func1 - complete
# 3.4822022531844965
# Func2 - complete
# 18:17:52
