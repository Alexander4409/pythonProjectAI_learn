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


