# читать - https://metanit.com/python/tutorial/2.2.php
# Переменные писать осмысленно т.е на английском языке
# devochky, knopka, poezd - так не делать !!!
age = 17
# стиль написания переменных и названий функций - low_snake_case
# класс пишем в стиле HiCamelCase
# типы данных

# Не изменяемые
# bool - True/False
# str - "hi"
# float - 3.14
# int - 3
# tuple (1,3,"hi")

# Изменяемые типы данных
# list - [1,3,2,'Hi']
# dict - {key:value, 67:Mem}
# set - {3,2,True}

# тип данных - это атрибуты которые имеют некие уникальные характеристики

# def test_memory():
#     num = 10
#     num_2 = num
#
#     print(f"num id = {id(num)}")
#     print(f"num_2 id = {id(num_2)}")
#
# test_memory()

# num id = 140707748911832
# num_2 id = 140707748911832
#Сформулировать вывод

def test_memory():
    lst = [10]
    lst_2 = lst

    print(f"lst id = {id(lst)}")
    print(f"lst_2 id = {id(lst_2)}")
    lst.append(1)
    print(f"lst id = {id(lst)}")


test_memory()
