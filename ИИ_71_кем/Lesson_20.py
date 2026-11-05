#Паралелизм - позволяет выполнять несколько вычислений одновременно
#Asincio - запуская задачу продолжаем выполнять быстрые операции пока ждем ответа
# от сервера или пользователя.
#multiprocessing - разделяет процессы по разным ядрам процессора компьютера
#threading - позволяет нескольким потоком работать в очереди
# GIL - гарантирует что в определенный момент времени будет работать только один поток
# Потокобезопасность - работает путем создания локальных копий


#не потокобезопасная программа
# import threading
# import time
# from collections import Counter
#
#
# res = []
#
# def run_experement():
#     global num
#     num = 2
#
#     def thread1():
#         global num
#         curent = num
#         time.sleep(0.000001)
#         num = curent + 2
#
#     def thread2():
#         global num
#         curent = num
#         time.sleep(0.000001)
#         num = curent ** 3
#
#     t1 = threading.Thread(target=thread1)
#     t2 = threading.Thread(target=thread2)
#
#     t1.start()
#     t2.start()
#
#     return num
#
# for i in range(500):
#     final_num = run_experement()
#     res.append(final_num)
#
# stats = Counter(res)
#
# print("Result of experiment")
# for outcome, count in stats.items():
#     print(f"result - num = {outcome} repeat - {count}  ")

import time
from turtledemo.penrose import start


def heavy(num):
    for i in range(1,num):
        for y in range(1,num):
            i**y

def sequential(num):
    for i in range(num):
        heavy(5000)
    print(f"{num} - количество циклов вычислений завершено")

if __name__ == '__main__':
    start = time.time()
    sequential(80)
    end = time.time()
    print(f'Общее время работы - {end-start}')


