#циклы - участок кода способный к повторению какой либо другой части кода
# while

#Глупый счётчик
# num = 0
#
# while num <= 15:
#
#     #операторы
#     num += 1
#     if num == 7:
#         continue
#     print(num)
#     # if num == 7:
#     #     print(f"Emergency stop, num = {num}")
#     #     break - остановка иттерации
#
#
# print("End program")

# матрица
# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(i*j, end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1

# for i in "13":
#     for j in "31":
#         print(f"{i}{j}")

# str = "1786594039485675849"
# lst = [1,3,5,2]
# tup = (1,4,2,4)
# dct = {1:"84", 2:'UHGYU'}
# st = {1,3,2,4}

# #иттератор
# print(iter(lst))
# print(iter(tup))
# print(iter(dct))
# print(iter(st))
# print(iter(str))

# tumb = ["pencil", "pen", "apple"]
# # <list_iterator object at 0x0000021B9EF73AC0> - правило перебора
# # коллекции или нашей тумбочки\
# # получаем правило иитерации
# iter_rule = iter(tumb)
#
# try:
#     while True:
#         next_value = next(iter_rule)
#         print(f'Очередное значение {next_value}')
# except StopIteration:
#     print("Итерация закончена")

# Условие:
# использовать yeld
# 1. У вас есть итератор, который выдает размер детали в миллиметрах
# (например, целые числа от 90 до 110).
# 2. Эталонный размер детали — 100 мм. Допустимая погрешность — ±2 мм
# (то есть детали от 98 до 102 мм считаются хорошими, а все,
# что меньше 98 или больше 102 — браком).
# 3. Нужно написать цикл, который берет элементы из итератора и считает брак.
# 4. Как только счетчик брака достигнет 3, цикл должен прерваться,
# и программа должна вывести: «Внимание! Обнаружено 3 бракованные детали.
# Конвейер остановлен

import random

def conveyor():
    while True:
        yield random.randint(95,105)

factory = conveyor()

defective_count = 0

for detail_size in factory:
    print(f"сканирование детали - {detail_size} мм")
    # дописать код

