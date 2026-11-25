#блок кода который может выполнять одно и тоже действие много раз
# print()
# input()
# int()



#процедура - без return
# def say_hi():
#     print("Hi")
#

# def say_hi(name):
#     return f'Hi {name}'
#
#
# print(say_hi("Tom"))
# print(say_hi("Mary"))
# print(say_hi("Jefry"))
# print(say_hi("Toby"))

#Локальные функции
# def messages():
#     def say_hi():
#         print("Hi")
#
#     def say_bye():
#         print("Bye")
#
#     say_hi()
#     say_bye()
#
# messages()

#Локальный вызов функций
# def say_hi():
#     print("Hi")
#
# def say_bye():
#     print("Bye")
#
# def messages():
#     say_hi()
#     say_bye()
#
# messages()

#параметры функций

# def print_person(name, age = 11, status = True):
#     print(f'Name - {name}\n'
#           f'Age - {age}\n'
#           f'Family status - {status}')
#
#
# print_person("Bob", 13, True)
# print_person(name = "Pavel", status = False)

# * - именованные параметры
# def print_person(*, name, age = 11, status = True):
#     print(f'Name - {name}\n'
#           f'Age - {age}\n'
#           f'Family status - {status}')
#
#
# # print_person("Bob", 13, True)
# print_person(name = "Pavel", status = False)


# / - позиционных параметров
# def print_person(name, age = 11, status = True, /):
#     print(f'Name - {name}\n'
#           f'Age - {age}\n'
#           f'Family status - {status}')
#
#
# print_person("Bob", 13, True)
# print_person(name = "Pavel", status = False)

#*args
def summ(*args):
    res = 0
    for i in args:
        res += i
    return res

print(summ(1,2,4,2,54,6,42,6,2,6457,244,68,2))
print(summ(1,2,68,2))
