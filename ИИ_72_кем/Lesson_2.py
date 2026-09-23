# def test_memory():
#     num = 10
#     num_1 = num
#
#     print(f'num - {id(num)}')
#     print(f'num_1 - {id(num_1)}')
#
#     num += 1
#     print(id(num))
#     num -= 1
#     print(id(num))
#
# test_memory()


# num -  140703710583512
# num_1 -  140703710583512
# 140703710583544
# 140703710583512

def test_memory():
    lst = [10]
    lst_1 = lst

    print(f'num - {id(lst)}')
    print(f'num_1 - {id(lst_1)}')

    lst.append(200)
    print(id(lst))

test_memory()
# для динамической коллекции с изменяемыми типами данных
# выделяется закрытая область в оперативной памяти

# тип данных - атрибут определяющий какого рода данные могут храниться в объекте.
# num - 2524585251200
# num_1 - 2524585251200
# 2524585251200