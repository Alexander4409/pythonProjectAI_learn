# # циклы while/for
#
# num = 0
# while num <= 100:
#
#
#     num += 1
#     if num == 5:
#         continue
#
#     print(f"Число - {num}")
#
#     if num == 10:
#         print("Аварийная остановка цикла")
#         break
#


# проверяет истинность утверждения и выполняет инструкцию в
# своём теле до тех пор пока выражение истинно

# break полностью останавливает цикл
# continue

lst = [1,3,1,23,4,23,432,2]
lst1 = '1213243131312cjhfghdjskl3'
lst2 = (1,32,3,1,42,4,6)

# иттератор - инструкция которая содержит информацию о том как
# выполнять перебор какой либо коллекции
# print(iter(lst))
# print(iter(lst1))
# print(iter(lst2))

iterator = iter(lst)

try:
    while True:
        next_val = next(iterator)
        print(next_val)
except StopIteration:
    print("Итерация завершена")