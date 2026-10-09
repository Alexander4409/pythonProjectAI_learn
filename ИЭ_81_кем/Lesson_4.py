#функция - ограниченный участок кода который можно вызывать столько раз сколько это необходимо
# процедура - нет return
# def say_hi():
#     print("hi")
#
#
# def say_hello(user_name):
#     return f"Hello {user_name}"
#
#
# print(say_hello("Tom"))


#Локальные функции
# def messages():
#     def say_hi():print("hi")
#     def say_bye():print("bye")
#     say_hi()
#     say_bye()
#
# messages()

# локальный вызов функции
# def say_hi():print("hi")
# def say_bye():print("bye")
#
# #менеджер выполнения функцию
# def messages():
#     say_hi()
#     say_bye()
#
# messages()

#параметры функций
# аргументы по умолчанию
# def summa(num=0,num1=0):
#     return f"result - {num+num1}"
#
#
# print(summa(3,))

# def car_info(color,engine, T_range,/):
#     return f"Car color - {color}, engine volume - {engine}, Total range - {T_range}"

# print(car_info("red", 5, 3000))
# print(car_info(3, "blue", 3000))
# именованные параметры - * до параметров
#print(car_info( color = "red", 3000,33333 ))
# позиционные парметры - / после параметров
# print(car_info(None))

# def modyfi_lst(lst = None) -> None:
#     if lst is None:
#         lst = []
#     lst.append(1)
#     print(lst)
#
# modyfi_lst()
# modyfi_lst()
# modyfi_lst([6,7])
# modyfi_lst([6,7,3])
# modyfi_lst()
#Передача сколько угодно аргументов по позициям *
# def summ_of_element(*args):
#     res = 0
#     for i in args:
#         res += i
#     print(res)
#
# summ_of_element(1,3,1,3,5,2,5,63,2,4)
# summ_of_element(1,3,1,3,5,4)
# summ_of_element(1,3)

#передача параметров по имени **
# def reg_host(owner_name, **pets):
#     print(f"Owner - {owner_name}")
#     for pet,pet_name in pets.items():
#         print(f"{pet}, {pet_name}")
#
# reg_host("John", dog = "Kairo", cat = ["Bastet", "Larry"], parrot = ["Flyer","Poper"])

#  анонимные функции
# res = lambda num,num1: num+num1
#
# print(res(1,2))
name = "Tom"

def say_hi():
    name = "Bob"
    print("hi", name)

def say_bye():

    print("hi", name)

say_hi()
say_bye()
# доразобрать







