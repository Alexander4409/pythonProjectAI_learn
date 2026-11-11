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
    for i in range(1, num):
        for y in range(1, num):
            _ = i ** y

    if cycle in (0, 4, 9, 19):
        print(f"Cycle - {cycle}, core - {proc}")


def sequential(calc, proc):
    print(f"launch process - {proc}")
    for i in range(calc):
        heavy(500, i, proc)
    print(f"{calc} - количество циклов вычислений завершено")


def pooled(core=None):
    num_proc = multiprocessing.cpu_count() if core is None else core
    calc = int(80 / num_proc) if 80 % num_proc == 0 else int(80 // num_proc + 1)

    init = [(calc, n) for n in range(num_proc)]

    with multiprocessing.Pool(processes=num_proc) as pool:
        pool.starmap(sequential, init)

    print(f"\n[Внутри pooled] calc: {calc}, num_proc: {num_proc}, core: {core}")
    return calc, num_proc, core


if __name__ == '__main__':
    start = time.time()


    calc, num_proc, core = pooled(4)

    end = time.time()

    print(f'Общее время работы - {end - start:.2f} сек')
    print(f"На каждом ядре выполнено {calc} циклов вычислений")
    print(f'Итого {num_proc * calc} циклов за - {end - start:.2f} сек')

