# # while
# num = 0
# while num < 11:
#     print("hi")
#     num += 1
# num = 0
# while num < 15:
#
#     num += 1
#     if num == 6:
#         continue - пропуск итерации
#     if num == 6:
#         break - полное прекращение работы кода
#     print(num)

i = 1
j = 1
while i < 10:
    while j < 10:
        print(f'{i} * {j} = {i*j}', end = "\t")
        j += 1
    print("\n")
    j = 1
    i += 1




