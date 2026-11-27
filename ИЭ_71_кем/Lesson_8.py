# def analisis(*args):
#     res = 0
#     count = 0
#     for num in args:
#         res += num
#         count += 1
#     return (f"Сумма чисел - {res}\n"
#             f"Количество чисел - {count}\n"
#             f"Среднее значение - {res/count}")
#
#
# print(analisis(1,3,13,5,2,5,6,77,8,908,46,36,2))


# def reg_host(owner_name, **pets):
#     print(f"Owner - {owner_name}")
#     for pet,pet_name in pets.items():
#         print(f"{pet}, {pet_name}")
#
# reg_host("John", dog = "Kairo", cat = ["Bastet", "Larry"], parrot = ["Flyer","Poper"])

#лямбда выражения (анонимные функции)
square = lambda num: num ** 2
print(square(4))

def square2(num):
    return num**2

print(square2(4))

#Макар скрутить мышки