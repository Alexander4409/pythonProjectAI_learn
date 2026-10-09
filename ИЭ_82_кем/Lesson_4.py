#функция - ограниченный блок кода

# процедура не имеет return
# def say_hi():
#     print("hi")
#
# say_hi()

# Функция (пример)
# def say_hi(name):
#     return f"hi {name}"
#
# print(say_hi("Tom"))

#локальные функции
# def manager():
#     def say_bye():
#         print("Bye")
#
#     def say_hi():
#         print("hi")
#
#
#     say_hi()
#     say_bye()
#
# manager()

#локальные вызовы функций
# def say_bye():
#     print("Bye")
#
# def say_hi():
#     print("hi")
#
# #управляющая конструкция
# def manager():
#     say_hi()
#     say_bye()
#
# manager()

#аргументы функций
# def car_info(color = "White",engine = 3, T_range = 300,/):
#     return f"Car color - {color}, engine volume - {engine}, Total range - {T_range}"
#
# # print(car_info("red", 5, 3000))
# # print(car_info(color="blue", engine= 5, T_range= 3000))
# # print(car_info(color= "red", engine= 5, T_range= 3000))
# # именованные параметры - * до параметров
# print(car_info( color = "red", 4, 33333 ))
# # позиционные парметры - / после параметров
# # print(car_info(None))

# def test(lst = None) -> None:
#     if lst is None:
#         lst = []
#         lst.append(1)
#     print(lst)
#
# test()
# test()
# test([4,5,6])
# test()

# def summ(*args):
#     res = 0
#     for i in args:
#         res += i
#     print(res)
#
# summ(1,3,1,4,2,46,25,1,46,54)
# summ(1,3)

# def vet_reg_form(owner_name, **pets):
#     print(f"Owner - {owner_name}")
#     for pet,pet_name in pets.items():
#         print(f"{pet}, {pet_name}")
#
# vet_reg_form("john", dog = "Kairo", cat = ["Bastet", "Lusy"], hamster = ["Turbo", "Tron", "KFS"])\
#
# анонимные функции
suum = lambda num, num2:print(num+num2)

suum(1,2)
