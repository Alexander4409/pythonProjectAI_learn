# #декораторы - модифицирую вывод функции не меняя её исходного кода
# def decor(input_func):
#     def output_func():
#         print(10 * "*")
#         input_func()
#         print(10 * "*")
#     return output_func
#
#
# @decor
# def say_hi():
#     print("hi")
#
#
# @decor
# def say_bye():
#     print("bye")
#
# say_hi()
# say_bye()

# def checker_decor(input_func):
#     def output_func(*args):
#         name = args[0]
#         age = args[1]
#         if age < 0: age = "Error"
#         input_func (name,age)
#     return output_func
#
#
# @checker_decor
# def print_person(name,age):
#     print(f'name - {name}, age - {age}')
#
# print_person('Tom', 9)
# print_person('Jeffry', 56)
# print_person('Marta', 23)
# print_person('Donald', -9999999999999)
#
#
# Генераторная функция
# yield - ключевое слово
# def lasy_couter(num):
#     count = 1
#     while count <= num:
#         yield count
#         count += 1
#
# gen = lasy_couter(3)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

#Асинхронное программирование
# Базовый случай

# import time
#
# def func1(num):
#     print(num**3)
#     time.sleep(3)
#     print("Func1 compete")
#
# def func2(num):
#     print(num**0.5)
#     time.sleep(3)
#     print("Func2 complete")
#
#
# def main():
#     func1(4)
#     func2(4)
#
# print(type(func1))
# print(type(func1(4)))
#
#
# <class 'function'>
# 64
# Func1 compete
# <class 'NoneType'>

# асинхронный код
# import time
# import asyncio
#
#
# async def func1(num):
#     print(num ** 3)
#     await asyncio.sleep(3)
#     print("Func1 compete")
#
#
# async def func2(num):
#     print(num ** 0.5)
#     await asyncio.sleep(3)
#     print("Func2 complete")
#
#
# async def main():
#     task1 = asyncio.create_task(func1(4))
#     task2 = asyncio.create_task(func2(4))
#
#     await task1
#     await task2
#
# print(type(func1))
# print(type(func1(4)))
# <class 'function'>
# <class 'coroutine'> - разновидность генератора дает возможность приостановки выполнения задачи

# print(time.strftime("%X"))
# asyncio.run(main())
# print(time.strftime("%X"))

# f - функция содержащая корутину
# f() - корутина

# Задачи task 1/2
# import asyncio
#
#
# async def func1(num):
#     print(num ** 3)
#     await asyncio.sleep(3)
#     print("Func1 compete")
#
#
# async def func2(num):
#     print(num ** 0.5)
#     await asyncio.sleep(3)
#     print("Func2 complete")
#
#
# async def main():
#     task1 = asyncio.create_task(func1(4))
#     task2 = asyncio.create_task(func2(4))
#
#     print(type(task1))
#     print(task1.__class__.__bases__)
#
#     await task1
#     await task2
#
# asyncio.run(main())

# <class '_asyncio.Task'> - частный случай футуры, пердназначен для оборачивания (декорирования ) корутины
# (<class '_asyncio.Future'>,) - оболочка (разновидность декоратора) которая позволяет
# выполнятся коду асинхронно

# не работающий код (притворяемся что асинхронности нету )
# def func1(num):
#     print(num**2)
#     sleep(3)
#     print("Func1 complete")
#
# def func2(num):
#     print(num**3)
#     sleep(3)
#     print("Func2 complete")
#
# def main():
#     task1 = create_task(func1(4))
#     task2 = create_task(func2(4))
#
#     task1
#     task2
#
#
# main()

