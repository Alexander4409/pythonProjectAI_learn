# import asyncio
#
# async def func_1(num):
#     print(num**2)
#     await asyncio.sleep(3)
#     print("Func_1 Работу завершил")
#
#
# async def func_2(num):
#     print(num**0.5)
#     await asyncio.sleep(3)
#     print("Func_2 Работу завершил")
#
#
#
# async def main():
#     task1 = asyncio.create_task(func_1(4))
#     task2 = asyncio.create_task(func_2(4))
#
#     print(type(task1))
#     print(task1.__class__.__bases__)
#
#     await task1
#     await task2
#
#
# asyncio.run(main())

# <class '_asyncio.Task'> - частный случай футуры предназначен для декорирования корутины
# (<class '_asyncio.Future'>,) - декоратор для асинхронной функции который
# позволяет переключаться между асинхронными
# задачами, а точками переключения служит ключевое слово await

import time


def time_manager(func):
    def wrapper(*args,**qwargs):
        start = time.time()
        res = func(*args, **qwargs)
        end = time.time()
        print(f"Время выполнения : {end - start}")
        return res
    return wrapper

#
#
# import asyncio
#
# async def func_1(num):
#     print(num**2)
#     await asyncio.sleep(3)
#     print("Func_1 Работу завершил")
#
#
# async def func_2(num):
#     print(num**0.5)
#     await asyncio.sleep(3)
#     print("Func_2 Работу завершил")
#
#
#
# async def main():
#
#     await func_1(4)
#     await func_2(4)
#
#
#
# @time_manager
# def manager():
#     asyncio.run(main())
#
#
# manager()


#Многопоточное программирование
# однопоточная программа

# def heavy(num):
#     for i in range(1,num):
#         for j in range(1,num):
#             i**j
#
# @time_manager
# def sequential(num):
#     for i in range(num):
#         heavy(500)
#     print(f"{num} - циклов вычислений завершено ")
#
#
# sequential(80)

# 80 - циклов вычислений завершено
# Время выполнения : 29.832934856414795

#Многопоточный режим работы

import multiprocessing


def heavy(num, cycle, core):
    for i in range(1,num):
        for j in range(1,num):
            i**j
    print(f"Цикл № - {cycle}, ядро - {core}")


@time_manager
def sequential(calc, proc):
    print()
    for i in range(num):
        heavy(500)
    print(f"{num} - циклов вычислений завершено ")
#Дописать !!!