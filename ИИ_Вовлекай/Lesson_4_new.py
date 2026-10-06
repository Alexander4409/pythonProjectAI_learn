# Циклы - https://metanit.com/python/tutorial/2.7.php

#break - останавливает цикл
#continue - пропуск текущей итерации

# def base_user_info_5(name,age):
#     user_age = age + 5
#     return f"Привет {name}, тебе сейчас {age}, а через 5 лет станет {user_age}"
#
#
# name = input("Укажите имя")
# age = int(input("Укажите возраст"))
#
# print(base_user_info_5(name,age))

# процедура - нет return
# def say_hi():
#     print("Hi")
#
#локальные функции
# def say_bye():
#     print("Bye")
#
# def say_hi():
#     print("Hi")
#
#
# def print_messages():
#     say_hi()
#     say_bye()
#
# print_messages()

# def print_messages():
#     def say_bye():print("Bye")
#     def say_hi():print("Hi")
#
#     say_bye()
#     say_hi()
#
#
# print_messages()

#параметры функции (по умолчанию)
#!!!!!!!
# def base_user_info_5(name ,age):
#     user_age = age + 5
#     return f"Привет {name}, тебе сейчас {age}, а через 5 лет станет {user_age}"
#
#
# name = input("Укажите имя")
# age = int(input("Укажите возраст"))
#
# print(base_user_info_5(name,age))

# def print_person(name="None", age=18):
#     print(f"Name {name}, age = {age}")
#
# print_person("Bob")

# def print_person(*, name,age, company):
#     print(f"Name {name}, age = {age}, company = {company}")
#
# print_person(company = "Microsoft", age = 41, name = "Bob")
# передача именованных параметров
# def wow(*,run,mark,model,V,color):
#     print(f'пробег {run},марка {mark}, модель {model}, объем двигателя {V}, цвет {color}')
#
# print(wow(run=1000,mark='honda',model='CHR',V=50,color='белый'))

# одновременная передача позиционных и именованных параметров
# def print_person(name, / ,age = 18, *, company):
#     print(f"Name {name}, age = {age}, company = {company}")
#
# print_person("Bob", company="Google")
# print_person("Sam",37, company="JetBrains")
# print_person("Marta", company="JetBrains",age=45)

def summ(*args):
    res = 0
    for nums in args:
        res = res+nums
    print(f"sum of numbers - {res*2}")

summ(1,2)
summ(1,2,4,2,5,2,5)
summ(1,7)

# qwargs!
# - https://metanit.com/python/tutorial/2.15.php