#многопоточный код
import threading
import time

from ИИ_81_кем.Lesson_14 import target


def heavy(num, cycle, thead):
    for i in range(1,num):
        for y in range(1,num):
            i**y
        print(f"Cycle - {cycle}, Flow - {thead}")

def sequential(calc, thead):
    print(f"launch flow - {thead}")
    for i in range(calc):
        heavy(500, cycle, thead)
    print(f"{calc} - количество циклов вычислений завершено")

def threaded(theads, calac):
    #theads - количество потоков
    #calc - кол-во операций на 1 поток

    threads = []

    for thead in range(theads):
        task = threading.Thread(target= sequential,args=(calac,thead))
        threads.append(task)
        task.start()

    for task in threads:
        task.join()


if __name__ == '__main__':
    start = time.time()
    threaded(4,20)
    end = time.time()
    print(f'Общее время работы - {end-start}')