#Базовый уровень, решение в лоб
import asyncio
import time




def time_manager(func):
    def wrapper(*args,**qwargs):
        start = time.time()
        res = func(*args, **qwargs)
        end = time.time()
        print(f"Время выполнения : {end - start}")
        return res
    return wrapper


# def func1(num):
#     print(num**2)
#     time.sleep(3)
#     print("func1 завершил работу")
#
#
# def func2(num):
#     print(num**0.2)
#     time.sleep(3)
#     print("func2 завершил работу")
#
#
#
# @time_manager
# def main():
#     func1(3)
#     func2(3)
#
#
# main()
# 16
# Func_1 Работу завершил
# 1 5
# Func_2 Работу завершил
# Время выполнения : 6.00136137008667



# async def func1(num):
#     print(num**2)
#     await asyncio.sleep(3)
#     print("Func1 завершил работу")
#
#
# async def func2(num):
#     print(num**0.2)
#     await asyncio.sleep(3)
#     print("Func2 завершил работу")
#
#
# async def main():
#     task1 = asyncio.create_task(func1(4))
#     task2 = asyncio.create_task(func2(4))
#
#     await task1
#     await task2
#
#
#
# @time_manager
# def manager():
#     asyncio.run(main())
#
#
# manager()

# 16
# 1.3195079107728942
# Func1 завершил работу
# Func2 завершил работу
# Время выполнения : 3.0182418823242188

# разбор типов данных
# def func1(num):
#     print(num**2)
#     time.sleep(3)
#     print("func1 завершил работу")
#
#
# def func2(num):
#     print(num**0.2)
#     time.sleep(3)
#     print("func2 завершил работу")
#
#
#
# @time_manager
# def main():
#     func1(3)
#     func2(3)
#
# print(type(func1))
# print(type(func1(4)))

# <class 'function'>
# 16
# func1 завершил работу
# <class 'NoneType'>


async def func1(num):
    print(num**2)
    await asyncio.sleep(3)
    print("Func1 завершил работу")


async def func2(num):
    print(num**0.2)
    await asyncio.sleep(3)
    print("Func2 завершил работу")


async def main():
    task1 = asyncio.create_task(func1(4))
    task2 = asyncio.create_task(func2(4))

    await task1
    await task2

print(type(func1))
print(type(func1(4)))

# <class 'function'>
# <class 'coroutine'> - разновидность генератора