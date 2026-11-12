import time


def time_manager(func):
    def wrapper(*args,**qwargs):
        start = time.time()
        res = func(*args, **qwargs)
        end = time.time()
        print(f"Время выполнения : {end - start}")
        return res
    return wrapper


#
# def heavy(num):
#     for num1 in range(1, num):
#         for num2 in range(1, num):
#             num1**num2
#
# @time_manager
# def sequential(num):
#     for i in range(num):
#         heavy(500)
#     print(f"{num} Циклов вычислений выполнены")
#
#
# sequential(80)


# 80 Циклов вычислений выполнены
# Время выполнения : 29.588422060012817


import threading

def heavy(num, cycle, thead):
    for i in range(1,num):
        for y in range(1,num):
            i**y
        print(f"Cycle - {cycle}, Flow - {thead}")

def sequential(calc, thead):
    print(f"launch flow - {thead}")
    for i in range(calc):
        heavy(500, i, thead)
    print(f"{calc} - количество циклов вычислений завершено")


@time_manager
def threaded(theads, calc):
    #theads - количество потоков
    #calc - кол-во операций на 1 поток

    threads = []

    for thead in range(theads):
        task = threading.Thread(target= sequential,args=(calc,thead))
        threads.append(task)
        task.start()

    for task in threads:
        task.join()



threaded(4,20)
