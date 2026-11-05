import time
import tracemalloc

def benchmark(f):
    def w(*a, **kw):
        tracemalloc.start()
        t = time.time()
        res = f(*a, **kw)
        print(f"\n{f.__name__}: {time.time()-t:.2f}s | {tracemalloc.get_traced_memory()/1048576:.2f}MB")
        tracemalloc.stop()
        return res
    return w

def heavy(num):
    for i in range(1, num):
        for y in range(1, num):
            i**y

@benchmark
def sequential(num):
    for i in range(num):
        heavy(500)
    print(f"{num} - количество циклов вычислений завершено")

if __name__ == '__main__':
    sequential(80)
