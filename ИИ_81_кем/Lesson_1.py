#Не изменяемые типы данных
# tuple - (1,"hi",True)
# int - 4
# float - 2.1
# str - "hi"
# frozenset - {1,2,"hi"}
# bool - True/False
# bytes - 1e
# None
# complex

#Изменяемые данные
#List - [1,3.3,"True",False]
#Dict - {key:value, 1:Name}
#set - {1,3,2}
#bytearray - [0,1,0,1]

#Атрибут - совокупность характеристик

# def test_memory_id() -> None:
#     num = 100
#     num_2 = num
#
#     print(f'num: id {id(num)}')
#     print(f'num2: id {id(num_2)}')
#
#     num += 1
#
#     print(f'num: id {id(num)}')
#
#
# test_memory_id()

#Переменная это ссылка на ячейку памяти
# неизменяемый тип данных создает новую ячейку памяти
# Информация не удаляется при заполнении ячейки, она выделяется, а потом перезаписывается
# num: id 140706271929880
# num2: id 140706271929880
# num: id 140706271929912

def test_memory_id() -> None:
    lst = [100]
    lst_2 = lst

    print(f'lst: id {id(lst)}')
    print(f'lst_2: id {id(lst_2)}')

    lst.append(2)

    print(f'lst: id {id(lst)}')
    print(f'lst_2: id {id(lst_2)}')


test_memory_id()

# Ячейки всегда разные
# num: id 140706271929880
# num2: id 140706271929880
# num: id 140706271929912