#асинхронные функции
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


def func_1(num):
    print(num**2)
    time.sleep(3)
    print("Func_1 Работу завершил")


def func_2(num):
    print(num**0,5)
    time.sleep(3)
    print("Func_2 Работу завершил")

def main():
    func_1(4)
    func_2(4)



main()
