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
# вложенные циклы
# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(f'{i} * {j} = {i*j}', end = "\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1

#for - пробегается по набору значений
# nums = [1,2,3,5,3,2]
# nums_1 = (1,2,3,5,3,2)
# nums_2 = "100000000000000000000"
#
# print(iter(nums))
# print(iter(nums_1))
# print(iter(nums_2))
tumb = ["pen...", "apple", "pencil"]

tumb_iterator = iter(tumb)

try:
    while True:
        nex_item = next(tumb_iterator)
        print("Очередное значение ", nex_item)
except StopIteration:
    print("Итерация завершена")



#Читать - https://metanit.com/python/tutorial/2.7.php
