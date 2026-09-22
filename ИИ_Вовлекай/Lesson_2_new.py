#группа телеграмм - https://t.me/vovlekay_AI
# скачать пайчарм - https://gb.ru/manualpycharmcommunity
# питон скачать - https://www.python.org/downloads/windows/

#Плохой пример
# def test_foo(listing = []) -> None:
#     listing.append(1)
#     print(listing)
#
# test_foo()
#
# test_foo()
#
# test_foo([8,9,0])
#
# test_foo()
# [1]
# [1, 1]
# [8, 9, 0, 1]
# [1, 1, 1]
# не предсказуемое поведение программы

# хороший пример
# def test_foo(listing = None) -> None:
#     if listing is None:
#         listing = []
#     listing.append(1)
#     print(listing)
#
#
# test_foo()
# test_foo()
# test_foo([8,9,0])
# test_foo()

# print(6/5)
# print(6//5)
# print(6%5)

# арифметические операци - https://metanit.com/python/tutorial/2.3.php
# num = 10
# num_2 = num + 2
# print(num_2)
#Синтаксический сахар
# +=
# *=
# /=

# round()
# num = 1.345254234523424234234
# print(round(num, 2))
# иттератор - https://habr.com/ru/companies/domclick/articles/674194/
lst_1 = []