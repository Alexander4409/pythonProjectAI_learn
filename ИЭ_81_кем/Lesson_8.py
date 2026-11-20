#локальный и глобальный контекст
# def messages():
#     def say_hi():
#         print("Hi")
#
#     say_hi()
#
#
# messages()

#global - прикрепляет некий идентификатор к переменной и позволяет скрывать глобальные параметры и заменить из локальными

# name = "Bob"
#
# def say_hi():
#     global name
#     name = "Tom"
#     print(f"Hi {name}")
#
#
# def say_bye():
#     print(f"Bye {name}")
#
#
# print(name)
# say_hi()
# say_bye()

# nonlocal - прикрепляет идентификатор к переменной в локальном контексте какой либо функции

# def func_outer():
#     num = 5
#
#     def func_inner():
#         nonlocal num
#         num = 25
#         print(num)
#
#     func_inner()
#     print(num)
#
# func_outer()

