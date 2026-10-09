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
def car_info(color = "White",engine = 3, T_range = 300,/):
    return f"Car color - {color}, engine volume - {engine}, Total range - {T_range}"

# print(car_info("red", 5, 3000))
# print(car_info(color="blue", engine= 5, T_range= 3000))
# print(car_info(color= "red", engine= 5, T_range= 3000))
# именованные параметры - * до параметров
print(car_info( color = "red", 4, 33333 ))
# позиционные парметры - / после параметров
# print(car_info(None))