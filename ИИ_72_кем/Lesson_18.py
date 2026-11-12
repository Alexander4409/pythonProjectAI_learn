import time


def time_manager(func):
    def wrapper(*args,**qwargs):
        start = time.time()
        res = func(*args, **qwargs)
        end = time.time()
        print(f"Время выполнения : {end - start}")
        return res
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


# 80 Циклов вычислений выполнены
# Время выполнения : 29.588422060012817