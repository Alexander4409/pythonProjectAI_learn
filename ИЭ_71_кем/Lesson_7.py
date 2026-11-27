#функции - блок кода который может
# многократно выполнять какое-либо действие
# print()
# input()
# int()
# ...
# данный пример - процедура (нет return)
# def say_hi(name):
#     print(f"hi {name}")
#
#
# say_hi()
from itertools import count


#Обычная функция
# def say_hi(name):
#     return f"hi {name}"

# локальные функции
# def messages():
#     def say_hi(name):
#         print(f"hi {name}")
#
#
#     def say_bye(name):
#         print(f"bye {name}")
#
#
#     say_bye("Bob")
#     say_hi("Bob")
#
#
#
# messages()


# def main():
#     hello()
#     good_bye()
#
#
# def hello():
#     print("Hello user")
#
#
# def good_bye():
#     print("Bye user")
#
#
#
# main()

#параметры функции
# def user_info(name, age, is_maried):
#     print(f"user info\n"
#           f"user name - {str(name)}\n"
#           f"user age - {int(age)}\n"
#           f"user family status - {bool(is_maried)}")
#
# user_info("Mary", 23, True)

#параметры по умолчанию
# def user_info(name, age = 18, is_maried = False):
#     print(f"user info\n"
#           f"user name - {str(name)}\n"
#           f"user age - {int(age)}\n"
#           f"user family status - {bool(is_maried)}")
#
#
# user_info("Mary")
# user_info("Bob", 33, True)

# именованные параметры спец символ - * после него параметры ДОЛЖНЫ быть ТОЛЬКО именованными
# def user_info( name, age, is_maried,*, company,):
#     print(f"user info\n"
#           f"user name - {str(name)}\n"
#           f"user age - {int(age)}\n"
#           f"user family status - {bool(is_maried)}\n"
#           f"user company - {str(company)}")
#
#
# user_info(age = 23, name = "Kelly", is_maried = False, company="microsoft")
# user_info("Bob", 33, True, company = "apple")




