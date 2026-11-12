import time


def time_manager(func):
    def wrapper():
        time.time()
        func()
        time.time()
    return wrapper



def heavy(num):
    for num1 in range(1, num):
        for num2 in range(1, num):
            num1**num2

@time_manager
def sequential(num):
    for i in range(num):
        heavy(500)
    print(f"{num} Циклов вычислений выполнены")


sequential(80)
