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

# import asyncio
#
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
#     print(type(task1))
#     print(task1.__class__.__bases__)
#
#     await task1
#     await task2
#
# asyncio.run(main())

# <class '_asyncio.Task'>
# (<class '_asyncio.Future'>,)
# set.result(value)

## корутина - разновидность генератора дает возможность возобнавлять
# работу функции которая была приостановлена
## задача - частный случай футуры, предназначена для обертки корутины
## футура - оболочка для асинхронной сущности, может переключать выполнение задач
# которые обозначены словом await

#не работающий пример

# def fun1(num):
#     print(num ** 2)
#
#     sleep(3)
#
#     print("fun1 complete")
#
#
# def fun2(num):
#     print(num ** 0,5)
#
#     sleep(3)
#
#     print("fun2 complete")
#
# def main():
#
#     task1 = create_task(fun1(4))
#     task2 = create_task(fun2(4))
#
#     task1
#     task2
#
# main()

#неудачный пример

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
# async  def main():
#     await fun1(4)
#     await fun2(4)
#
# print(time.strftime("%X"))
# asyncio.run(main())
# print(time.strftime("%X"))



#Паралелизм - выполнение нескольких вычислений одновременно
#поток - независимая последовательность выполнения вычислений
#демонстрация не правильной работы потока данных

# num = 2
#
# def thread_1():
#     global num
#     num = num + 2
#     return num
#
# def thread_2():
#     global num
#     num = num * 3
#     return num
#
# print(thread_1())
# print(thread_2())

#исследование разных подходов к параллельному вычислению

#Однопоточный режим
import time

def heavy(num):
    for i in range(1,num):
        for y in range(1,num):
            i ** y

def sequential(num):
    for i in range(num):
        heavy(500)
    print(f'{num} - циклов вычислений закончено')


if __name__ == "__main__":
    start = time.time()
    sequential(80)
    end = time.time()
    print("Общее время работы ", end - start)

# 80 - циклов вычислений закончено
# Общее время работы  50.62856197357178



