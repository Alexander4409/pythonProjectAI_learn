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


#лямбда функции
# message = lambda num_1, num_2:print(num_1+num_2)
#
# message(5,2)

#Области видимости

# name = "john"
#
# def say_hi():
#     global name
#     name = "Bob"
#     print(f'Hi {name}')
#
# def say_bye():
#
#     print(f'Bye {name}')
#
# say_hi()
# say_bye()
#
# def outer():
#     num = 5
#     def inner():
#         nonlocal num
#         num = 25
#         print(num)
#     inner()
#     print(num)
# outer()
#замыкание
def outer():
    num = 0
    def inner():
        nonlocal num
        num += 1
        print(num)
    return inner

fu = outer()

fu()
fu()
fu()
fu()
fu()
fu()
fu()
fu()
fu()
fu()
fu()
fu()

#задача написать робота пицемейкера
# робот должен принимать заказ от пользователя (учитывать что пользователь может придти не один)
# робот должен предоставить разное меню для разновозрастных пользователей, после идентификации
# пользователя и определения тех позиций которые пользователь хочет купить робот должен спросить,
# как будет проходить оплата (наличнкой или кртой) в случии налички
# пользователь вводит число боле суммы, а робот выдает сдачу

