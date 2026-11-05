# Асинхронное программирование
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
# (<class '_asyncio.Future'>,) - оболочка (разновидность декоратора) которая позволяет выполнять как-бы все одновременно
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

#не удачный пример (без задач (без ракетоносителей))
import time
import asyncio

async def func1(num):
    print(num ** 3)
    await asyncio.sleep(3)
    print("Func1 compete")


async def func2(num):
    print(num ** 0.5)
    await asyncio.sleep(3)
    print("Func2 complete")

async def main():
    await func1(4)
    await func2(4)

print(time.strftime("%X"))
asyncio.run(main())
print(time.strftime("%X"))