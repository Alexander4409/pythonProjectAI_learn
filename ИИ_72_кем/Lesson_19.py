#циклы
# while / for


# break - полностью останавливает код
# while num < 10:
#     print(f'Число - {num}')
#     if num == 3:
#         break
#     num += 1

# пропускает выбранную итерацию
# while num < 10:
#
#     num += 1
#     if num == 3:
#         continue
#     print(f'Число - {num}')


#
# lst = [1,3,2,5,6]
# for num in lst:
#     print(num)

#иттераторы - инструкции по перебору
# num = 143857083752875211111111111111111
drawer = ["Ножници", "нож", "Турели", 3]
# drawer1 = ("Ножници", "нож", "Турели", 3)
# drawer2 = {"Ножници", "нож", "Турели", 3}


# print(iter(drawer))
# print(iter(drawer1))
# print(iter(drawer2))

iterator_collection = iter(drawer)

try:
    while True:
        next_val = next(iterator_collection)
        print(f"Полученный предмет из тумбочки - {next_val}")
except StopIteration:
    print("Тумбочка пуста")
# ответственность перебора лежит на итераторе



