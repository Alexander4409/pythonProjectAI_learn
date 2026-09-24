# данные - сведенья которые хранятся в каком-либо виде
# информация - структурированные данные
# знания - структурированные и применяемая на практике информация
# типы данных -
# print(2.0 == 2)
# print(int(2) == float(2))

# def test_memory():
#     num = 11
#     num1 = num
#
#     print(id(num))
#     print(id(num1))
#
#
# test_memory()

# 140719339608792
# 140719339608792

def test_memory_mutable():
    lst = [10]
    lst1 = lst

    print(id(lst))
    print(id(lst1))

    lst.append(10000)
    print(id(lst))


test_memory_mutable()

# 2002872750464
# 2002872750464
# 2002872750464