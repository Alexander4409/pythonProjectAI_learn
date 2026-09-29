#циклы
# позволяют повторять что-либо столько раз сколько это необходимо.

# for i in range(1,1000):
#     print(i)

# Итератор - объект который в себе хранит инструкцию перебора чего либо

# ошибка типа данных
# num = 10000000
# for n in num:
#     print(n)

# tumb_list = ["ножницы", "книга", "pencil"]
# tumb_tuple = (1,32,52)
# tumb_set = {321,54,72,5}
# tumb_dict = {"Marta":123123123, "Bob":12312313}
# tumb_str = "gtwregewrilldt4523984235o986ytnfc90452"
# добавление объекта при помощи метода append
# tumb.append("яблоко")
# print(tumb)
# for obj in tumb:
#     print(obj)

# инкапсулированное правило итерации или просто ссылка на
# ячейку в памяти компьютера, где храниться правило перебора итерируемого объекта

# print(iter(tumb_list))
# print(iter(tumb_set))
# print(iter(tumb_str))
# print(iter(tumb_dict))
# print(iter(tumb_tuple))


# аналог цикла for БЕЗ цикла for
tumb_list = ["ножницы", "книга", "pencil"]

it = iter(tumb_list)

try:
    while True:
        # next() - представляет из себя "кнопку" которая получает следующее значение коллекции
        next_value = next(it)
        print(f"Очередное значение - {next_value}")
except StopIteration:
    print("Итерация закончена!")
print("Программа завершила работу ")



# ссылка на скачивание питона - https://www.python.org/ftp/python/3.14.7/Python-3.14.7.tar.xz
# Инструкция по установке питона - https://metanit.com/python/tutorial/1.2.php
# ссылка на пайчарм - https://gb.ru/manualpycharmcommunity
# Общая инструкция по работе с пайчарм и питон - https://habr.com/ru/articles/720480/
# инстркуция по связыванию питона и пайчарма -https://inf.tgl.net.ru/wp-content/uploads/2023/04/%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F-Python-PyCharm.pdf