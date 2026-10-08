# локальные функции
# def messages():
#     def say_hi():
#         print("hi")
#     def say_bye():
#         print("bye")
#
#
#     say_bye()
#     say_hi()
#
#
# messages()

# Локальный вызов функции
# def say_hi():
#     print("hi")
#
# def say_bye():
#     print("bye")
#
# def messages():
#     say_hi()
#     say_bye()
#
# messages()

# def car_info(color = "white",engine = 3,T_range = 300):
#     return f"Car color - {color}, engine volume - {engine}, Total range - {T_range}"
#
# # print(car_info("red", 5, 3000))
# # print(car_info(3, "blue", 3000))
# # именованные параметры - * до параметров
# # print(car_info(color = "blue" , engine= 5, T_range= 3000))
# # позиционные парметры - / после параметров
# print(car_info(None))

# def summ(*args):
#     res = 0
#     for num in args:
#         res +=num
#     print(res)
#
# summ(1,2,4,2,5,24,7,3,7,35,2)
# summ(1,2,4,2,5)

# def reg_host(owner_name, **pets):
#     print(f"Owner - {owner_name}")
#     for pet,pet_name in pets.items():
#         print(f"{pet}, {pet_name}")
#
# reg_host("John", dog = "Kairo", cat = ["Bastet", "Larry"], parrot = ["Flyer","Poper"])


