#переменные
# devochky, trmvai - так не делаем!!!
# пишем все на английском (комментарии можно на русском)
age = 18 # переменные должны называться осмысленно !

# читать - https://metanit.com/python/tutorial/2.2.php
# стиль написания переменных - low_snake_case - для переменных и названий функций,
# для классов HiCamelCase
# print(lst)
# lst.append("hi")
# print(lst)

# def test_memory():
#     num = 10
#     num_2 = num
#
#     print(f"num id: {id(num)}")
#     print(f"num_2 id: {id(num_2)}")
#
#     num += 1
#     print(f"num id: {id(num)}")
#
#
# test_memory()
# num id: 140708828551896
# num_2 id: 140708828551896
# num id: 140708828551928
# ячейка памяти не динамическая любое перезаписывание информации ведет к созданию новой ячейки

def test_memory():
    lst = [10]
    lst_2 = lst

    print(f"lst id: {id(lst)}")
    print(f"lst_2 id: {id(lst_2)}")

    lst.append(1)
    print(f"lst id: {id(lst)}")

test_memory()

# lst id: 1701852139904
# lst_2 id: 1701852139904
# lst id: 1701852139904
# ячейка памяти динамическая (изменяется её объем (оперативная память))