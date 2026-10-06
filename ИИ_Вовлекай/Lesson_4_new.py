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

#параметры функции
def base_user_info_5(name,age):
    user_age = age + 5
    return f"Привет {name}, тебе сейчас {age}, а через 5 лет станет {user_age}"


name = input("Укажите имя")
age = int(input("Укажите возраст"))

print(base_user_info_5(name,age))