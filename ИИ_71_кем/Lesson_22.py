import time



def time_manager(func):
    def wrapper(*args,**qwargs):
        start = time.time()
        res = func(*args, **qwargs)
        end = time.time()
        print(f"Время выполнения : {end - start}")
        return res
    return wrapper

x = 2
lst = [x ** 2 for x in range(1000000)]


@time_manager
def fake_for():
    iterator = iter(lst)

    try:
        while True:
            next_val = next(iterator)
    except StopIteration:
        print("Итерация завершена")

fake_for()
print("fake for complity")

@time_manager
def real_for():
    for i in lst:
        pass
fake_for()
print("fake for complity")
real_for()
print("real for complity")
#здрасвуйсте, а где посмотреть свои была по олимпиаде Всош
