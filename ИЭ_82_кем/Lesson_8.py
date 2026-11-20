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


# def func_1(num):
#     print(num**2)
#     time.sleep(3)
#     print("Func_1 Работу завершил")
#
#
# def func_2(num):
#     print(num**0.5)
#     time.sleep(3)
#     print("Func_2 Работу завершил")
#
#
# @time_manager
# def main():
#     func_1(4)
#     func_2(4)



# main()
# 16
# Func_1 Работу завершил
# 1 5
# Func_2 Работу завершил
# Время выполнения : 6.00136137008667

async def func_1(num):
    print(num**2)
    await asyncio.sleep(3)
    print("Func_1 Работу завершил")


async def func_2(num):
    print(num**0.5)
    await asyncio.sleep(3)
    print("Func_2 Работу завершил")


@time_manager
async def main():
    task1 = asyncio.create_task(func_1(4))
    task2 = asyncio.create_task(func_2(4))

    await task1
    await task2


asyncio.run(main())