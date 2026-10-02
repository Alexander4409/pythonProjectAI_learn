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
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i*j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1
