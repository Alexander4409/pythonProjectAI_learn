import time
import tracemalloc

def decor(input_func):
    def output_func():
        tracemalloc.start()
        start_time = time.perf_counter()

        input_func()

        end_time = time.perf_counter()
        result_time = end_time - start_time
        current, peak = tracemalloc.get_traced_memory()
        print(f"Текущая память: {current / 1024:.2f} КиБ")
        print(f"Пиковая память: {peak / 1024:.2f} КиБ")
        print(f"Время: {result_time}")
    return output_func()

@decor
def hello_world():
    print("Hello World!")
