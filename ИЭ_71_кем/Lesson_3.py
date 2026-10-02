#циклы
#for
#while

#пример работы цикла while
# break - останавливает цикл
# continue - пропускает текущую иттерацию
# lst = [1,2,3]
# num = 0
#
# while num <= 10:
#     num +=1
#     if num == 5:
#         continue
#     print(num)
#
#
# print("Работа завершена")


# for item in "123":
#     for item_1 in "321":
#         for item_2 in "231":
#             print(f"{item}{item_1}{item_2}")

#генерация матрицы

# i = 1
# j = 1
# while i <= 100:
#     while j <= 100:
#         print(i*j, end="\t")
#         j +=1
#     print("\n")
#     j = 1
#     i += 1

# итератор
lst = [2,12,31,31,2]
str = "fdewoifjefj84"
tupl = (2,4,2,5)
dct = {1:"sdfdf", 2:"sddw"}

num = 134853487345

print(iter(lst))
print(iter(str))
print(iter(tupl))
print(iter(dct))
# числа не итерируемые у них нет инструкции перебора
print(iter(num))

#Читать - https://metanit.com/python/tutorial/2.7.php