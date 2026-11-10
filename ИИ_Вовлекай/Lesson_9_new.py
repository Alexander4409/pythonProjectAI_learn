# import threading
# import time
# from collections import Counter
#
# results = []
#
#
# def run_experiment():
#     global num
#     num = 2
#
#     def thread_1():
#         global num
#         curent = num
#         time.sleep(0.000001)
#         num = curent + 2
#
#     def thread_2():
#         global num
#         curent = num
#         time.sleep(0.000001)
#         num = curent * 3
#
#     t1 = threading.Thread(target=thread_1)
#     t2 = threading.Thread(target=thread_2)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     return num
#
#
# # тестовый код запуска
# for i in range(500):
#     final_num = run_experiment()
#     results.append(final_num)
#
# status = Counter(results)
#
# for outcome, count in status.items():
#     print(f'Результат num = {outcome}, повторился {count} раз(а) ')

#Однопоточный режим
# import time
#
# def heavy(num):
#     for i in range(1,num):
#         for y in range(1,num):
#             i ** y
#
#
# def sequential(num):
#     for i in range(num):
#         heavy(500)
#     print(f'{num} - циклов вычислений закончено')
#
#
# if __name__ == "__main__":
#     start = time.time()
#     sequential(80)
#     end = time.time()
#     print("Общее время работы ", end - start)

# 80 - циклов вычислений закончено
# Общее время работы  50.62856197357178


# import threading
# import time
#
# def heavy(num, cycle, thread):
#     for i in range(1,num):
#         for y in range(1,num):
#             i ** y
#
#     print(f'Циклы - {cycle}, поток - {thread}')
#
# def sequential(calc, thread):
#     print(f'Запускаем поток {thread}')
#     for cycle in range(calc):
#         heavy(500, cycle, thread)
#     print(f'{calc} - циклов вычислений закончено')
#
#
# def threaded(theads, calc):
#     #thread - количество потоков
#     #calc - количество операций на поток
#
#     threads = []
#
#     for thead in range(theads):
#         task = threading.Thread(target=sequential, args=(calc,thead))
#         threads.append(task)
#         task.start()
#
#     for task in threads:
#         task.join()
#
#
# if __name__ == "__main__":
#     start = time.time()
#
#     threaded(4,20)
#     end = time.time()
#     print("Общее время работы ", end - start)
#
# Общее время работы  43.818674087524414


# import threading
# import time
#
# def heavy():
#     time.sleep(2)
#
# def threaded(theads):
#     threads = []
#
#     for thead in range(theads):
#         task = threading.Thread(target=heavy)
#         threads.append(task)
#         task.start()
#
#     for task in threads:
#         task.join()
#
#     print(f"{theads} - циклов имитации операции ввода и вывода закончены.")
#
# if __name__ == "__main__":
#     start = time.time()
#
#     threaded(80)
#     end = time.time()
#     print("Общее время работы ", end - start)

# Общее время работы 2.059701442718506

#multiprocessing

import multiprocessing
import time

def heavy(num, cycle, proc):
    for i in range(1,num):
        for y in range(1,num):
            i ** y

    print(f'Циклы - {cycle}, поток - {proc}')

def sequential(calc, proc):
    print(f'Запускаем поток {proc}')
    for cycle in range(calc):
        heavy(500, cycle, proc)
    print(f'{calc} - циклов вычислений закончено. Процессор - {proc}')


def processesed(procs, calc):
    #procs - количество ядер процессора
    #calc - количество операций на ядро

    processes = []

    for proc in range(procs):
        pro = multiprocessing.Process(target=sequential, args=(calc,proc))
        processes.append(pro)
        pro.start()

    for pro in processes:
        pro.join()


if __name__ == "__main__":
    start = time.time()

    num_of_proc = multiprocessing.cpu_count()
    calc = 80 // num_of_proc + 1
    processesed(num_of_proc,calc)
    end = time.time()
    print(f" всего ядер в процессоре - {num_of_proc} ")
    print(f" на каждом ядре произведено {calc} циклов вычислений")
    print(f" итого {num_of_proc*calc} циклов за время -  {end - start}")