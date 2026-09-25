#Переменные
# читать - https://metanit.com/python/tutorial/2.2.php
# переменные должны называться осмысленно, стиль написания - low_snake_case
# user_age = 10
# user_age_lst = [1,31,32]
# print()
# age = 18
#
# print(age)
# типы данных - атрибуты, которые задают способы считывания и записи данных

# не изменяемые типы данных
# tuple (1,3,1,4,6,3,6)
# int - 4
# float - 3.13
# str - "dffwe3423d3e33dddfet34565erfgfdsdfGHG"
# bool - True/False
# None - гуглим про "ничего"

# изменяемые типы данных
# list - [1,3,1,3]
# dict - {key:valu, "Bob":13}
# set - {1,3,1,3,4}

# def test_memory():
#     num = 10
#     num_2 = num
#
#     print(f"num id = {id(num)}")
#     print(f"num_2 id = {id(num_2)}")
#
#     num += 1
#     print(f"num id = {id(num)}")
#
#
# test_memory()

# num id = 140708822784728
# num_2 id = 140708822784728
# num id = 140708822784760


def test_memory():
    lst = [10]
    lst_2 = lst

    print(f"lst id = {id(lst)}")
    print(f"lst_2 id = {id(lst_2)}")

    lst.append(3)
    print(f"lst id = {id(lst)}")


test_memory()

# lst id = 2415773077888
# lst_2 id = 2415773077888