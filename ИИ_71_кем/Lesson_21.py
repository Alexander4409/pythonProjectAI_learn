#многопоточный код
# import threading
# import time
#
#
#
# def heavy(num, cycle, thead):
#     for i in range(1,num):
#         for y in range(1,num):
#             i**y
#         print(f"Cycle - {cycle}, Flow - {thead}")
#
# def sequential(calc, thead):
#     print(f"launch flow - {thead}")
#     for i in range(calc):
#         heavy(500, i, thead)
#     print(f"{calc} - количество циклов вычислений завершено")
#
# def threaded(theads, calac):
#     #theads - количество потоков
#     #calc - кол-во операций на 1 поток
#
#     threads = []
#
#     for thead in range(theads):
#         task = threading.Thread(target= sequential,args=(calac,thead))
#         threads.append(task)
#         task.start()
#
#     for task in threads:
#         task.join()
#
#
# if __name__ == '__main__':
#     start = time.time()
#     threaded(4,20)
#     end = time.time()
#     print(f'Общее время работы - {end-start}')
#
# Общее время работы - 40.66031861305237

# import threading
# import time
#
# def heavy():
#     time.sleep(2)
#
# def threaded(theads):
#     #theads - количество потоков
#
#     threads = []
#
#     for thead in range(theads):
#         task = threading.Thread(target=heavy)
#         threads.append(task)
#         task.start()
#
#     for task in threads:
#         task.join()
#     print(f"{threads} циклов имитации ввода вывода ")
#
# if __name__ == '__main__':
#     start = time.time()
#     threaded(80)
#     end = time.time()
#     print(f'Общее время работы - {end-start}')

# Общее время работы - 2.0209929943084717

import multiprocessing
import time




def heavy(num, cycle, proc):
    for i in range(1,num):
        for y in range(1,num):
            i**y
        print(f"Cycle - {cycle}, core - {proc}")

def sequential(calc, proc):
    print(f"launch flow - {proc}")
    for i in range(calc):
        heavy(500, i, proc)
    print(f"{calc} - количество циклов вычислений завершено")

def pocessesed(procs, calc):
    # procs - количество ядер
    # calc - количество операций на ядре

    proceses = []
    for proc in range(procs):
        pro = multiprocessing.Process(target = sequential, args=(calc, proc))
        proceses.append(pro)
        pro.start()

        for pro in proceses:
            pro.join()


if __name__ == '__main__':
    start = time.time()
    num_proc = multiprocessing.cpu_count()
    calc = 80 // num_proc + 1
    pocessesed(num_proc,calc)
    end = time.time()
    print(f'Общее время работы - {end-start}')
    print(f"На каждом ядре выполнено {calc} циклов вычислений ")
    print(f'Итого {num_proc*calc} циклов за - {end-start}')
