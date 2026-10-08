# def - область кода которая способна выполнять
# какое либо действие столько раз сколько её раз вызовут



#процедура - нет return
# def say_hi():
#     print("hi")
#
# say_hi()
# say_hi()
# say_hi()
# say_hi()

# def say_hi(name):
#     return f"hi {name}"
#
# print(say_hi("Tom"))

# локальные функции

# def messages():
#     def say_hi():print("hi")
#     def say_bye():print("bye")
#
#     say_hi()
#     say_bye()
#
# messages()

# def say_hi(): print("hi")
# def say_bye(): print("bye")
#
# def messages():
#     say_bye()
#     say_hi()
#
#
# messages()


# аргументы по умолчанию

# def summ(num_1 = 11, num_2 = 12):
#     return num_1+num_2
#
# print(summ(111,111))


# def car_info(color,/,engine,T_range):
#     return f"Car color - {color}, engine volume - {engine}, Total range - {T_range}"
#
#
# # print(car_info("red", 5, 3000))
# # # билиберда при не правильном порядке
# # print(car_info(3, "blue", 3000))
# # именованные параметры
# print(car_info("blue" , engine= 5, T_range= 3000))

# # именованные параметры
# def print_person(*, name, age, company):
#     print(f'Name - {name}, age - {age}, company - {company}')
#
# # print_person("Bob", 32, "microsoft")
#
# #позиционные
# def print_person_1( name, age,/, company):
#     print(f'Name - {name}, age - {age}, company - {company}')
#
# print_person_1("Bob", 32, company= "microsoft")

# args / qwargs

# def summ(*args):
#     res = 0
#     for num in args:
#         res += num
#
#     print(res)
#
# summ(1,3,3,5,2,5,7,2,6,7,1,2,3,4)
# summ(1,3,3,5,2,5,7,2)

# def print_pets_names(owner, **pets):
#     print(f"Owner name - {owner}")
#     for pet,name in pets.items():
#         print(f"{pet}:{name}")
#
# print_pets_names("john", dog = "Barkly", cat = ["Fluffy", "Larry"], perrot = ["Sheldon"])

# лямбда
# message = lambda :print("hi")
#
# message()

# Область видимости
#
# def say_hi():
#     global name
#     name = "Sam"
#     print(f'Hi {name}')
#
# def say_bye():
#     # name = "Tom"
#     print(f'bye {name}')

# say_hi()
# say_bye()

def outer():
    num = 5

    def inner():
        print(num)

    inner()
    print(num)

outer()