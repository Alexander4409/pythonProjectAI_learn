#генераторные функции

# def count_up(max):
#     count = 1
#     while count <= max:
#         yield count
#         count += 1
#
#
# gen = count_up(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


#отличия -               return                        |   yeld
# критерии           |                                 |
# жизненный цикл     |завершает работу функции навсегда| заморозка функции, ожидание следующего вызова
# память             |возвращает весь результат целиком| возвращает по одному элементу за раз
# количество вызовов |может сработать несколько раз    | может срабатывать многократно

#обычный подход с return
# def get_numbers_return(num):
#     result = []
#     for i in range(num):
#         result.append(i)
#     return result
#
#
# my_list = get_numbers_return(100000000)
# print(my_list)


# def get_numbers_yield(num1):
#     for i in range(num1):
#         yield i
#
#
# my_list = get_numbers_yield(100000000)
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))

#прием значений yield
# def echo_generator():
#
#     while True:
#         received = yield "Генератор готов принимать данные"
#         print(f"Генератор получил значение - {received}")
#
# gen = echo_generator()
# print(next(gen))
# message = input("Введите данные - ")
# # - запуск генератора
# gen.send(message)


# from inspect import isgenerator, isgeneratorfunction
# # создание генераторной функции
# def gen_func():
#     yield 10
#
# #возвращение генератора
# gen = gen_func()
#
# print(type(gen_func))
# print(type(gen))
#
# print(isgeneratorfunction(gen_func))
# print(isgenerator(gen))

# print(isgeneratorfunction(gen))
# print(isgenerator(gen_func))

#асинхронное программирование

#не асинхронный код
# import time
#
# def fun1(num):
#     print(num ** 2)
#     time.sleep(3)
#     print("Fun1 - compete")
#
# def fun2(num):
#     print(num ** 0.5)
#     time.sleep(3)
#     print("Fun2 - complete")
#
# def main():
#     fun1(4)
#     fun2(4)
#
# print(time.strftime("%X"))
#
# main()
#
# print(time.strftime("%X"))

#асинхронный
import asyncio
import time

async def fun1(num):
    print(num ** 2)
    await asyncio.sleep(3)
    print("Fun1 - compete")

async def fun2(num):
    print(num ** 0.5)
    await asyncio.sleep(3)
    print("Fun2 - compete")

async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    await task1
    await task2

print(time.strftime("%X"))

asyncio.run(main())

print(time.strftime("%X"))

# import aiohttp -
# aiofiles