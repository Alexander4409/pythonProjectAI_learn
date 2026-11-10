import threading
import time
from collections import Counter

results = []


def run_experiment():
    global num
    num = 2

    def thread_1():
        global num
        curent = num
        time.sleep(0.000001)
        num = curent + 2

    def thread_2():
        global num
        curent = num
        time.sleep(0.000001)
        num = curent * 3

    t1 = threading.Thread(target=thread_1)
    t2 = threading.Thread(target=thread_2)

    t1.start()
    t2.start()

    return num


# тестовый код запуска
for i in range(500):
    final_num = run_experiment()
    results.append(final_num)

status = Counter(results)

for outcome, count in status.items():
    print(f'Результат num = {outcome}, повторился {count} раз(а) ')