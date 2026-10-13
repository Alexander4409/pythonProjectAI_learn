#qwargs
# def reg_form(owner_name, **pets):
#     print(f'Владелец - {owner_name}')
#     for pet, pet_name in pets.items():
#         print(f"Вид животного {pet}, Кличка(и) - {pet_name}")
#
# reg_form("Вася", dog = "Rex", cat = ["Fluffy", "Anfisa"], parrot = ["Kesha", "Flyer"])

# лямбда выражение - небольшая анонимная функция использует оператор - lambda(параметры):(инструкция)
# message = lambda : print("Hi")
#
# message()

#вычисления

# multiply = lambda num1, num2: print(num1*num2)
#
# multiply(2,3)

# пример использования
# - передача лямбда выражения в качестве параметра
# def do_operation(num_1,num_2,operation):
#     res = operation(num_1,num_2)
#     print(f"result = {res}")
#
# do_operation(1,2, lambda num_1, num_2: num_1 + num_2)

# возвращения лямбда выражения из функции
# def select_operation(choice):
#     if choice == 1:
#         return lambda num_1 ,num_2: num_1+num_2
#     elif choice == 2:
#         return lambda num_1, num_2: num_1-num_2
#
# operation = select_operation(1)
# print(operation(1,2))
#
# operation = select_operation(2)
# print(operation(0,2))

#Контекст
# Глобальный контекст
# name = "Tom"
#
# def say_hi():
#     #изменение идентификатора переменной
#     global name
#     name = "Mary"
#     print("hello", name)
#
# def say_by():
#     print("good bye", name)
#
#
# print(name)
#
# say_hi()
# say_by()
#
# print(name)

#nonelocal - прикрепляет идентификатор из ближайшего окружения (кроме глобального контекста)
# def outer():
#     num = 5
#     def inner():
#         nonlocal num
#         num = 25
#         print(f"inner result - {num}")
#
#     inner()
#     print(f"outer result - {num}")
#
# outer()

# 1 у переменных есть идентификаторы видимости
# 2 чтобы из вложенной функции поднять значения нужен nonlocal
# 3 чтобы изменить глобальную переменную нужен global


# Замыкания!!!



