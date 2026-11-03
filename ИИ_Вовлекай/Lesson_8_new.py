# асинхронное програмирование исследование

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
# print(type(fun1))
# print(type(fun1(4)))

# <class 'function'>
# 16
# Fun1 - compete
# <class 'NoneType'>

# print(time.strftime("%X"))
#
# main()
#
# print(time.strftime("%X"))

#асинхронный
# import asyncio
# import time
#
# async def fun1(num):
#     print(num ** 2)
#     await asyncio.sleep(3)
#     print("Fun1 - compete")
#
# async def fun2(num):
#     print(num ** 0.5)
#     await asyncio.sleep(3)
#     print("Fun2 - compete")
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#
#     await task1
#     await task2
#
# print(type(fun1))
# print(type(fun1(4)))

# <class 'coroutine'>

# print(time.strftime("%X"))
#
# asyncio.run(main())
#
# print(time.strftime("%X"))

# f - функция
# f() - корутина, генератор, число ...

# футуры и задачи

import asyncio


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

    print(type(task1))
    print(task1.__class__.__bases__)

    await task1
    await task2

asyncio.run(main())

# <class '_asyncio.Task'>
# (<class '_asyncio.Future'>,)
# set.result(value)

## корутина - разновидность генератора дает возможность возобнавлять
# работу функции которая была приостановлена
## задача - частный случай футуры, предназначена для обертки корутины
## футура - оболочка для асинхронной сущности, может переключать выполнение задач
# которые обозначены словом await