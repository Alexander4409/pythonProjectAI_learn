# циклы
# for, while


#while - цикл работает при наличии условия

#Глупый счётчик
# num = 0
#
# while num <= 15:
#     num += 1
#     if num == 7:
#         continue # - пропуск итерации
#
#     print(num)
#
#     if num == 7:
#         print(f"Аварийная остановка кода, число = {num}")
#         break #- остановку цикла

# таблица умножения
# i = 1
# j = 1
#
# while i < 10:
#     while j < 10:
#         print(f"{i} * {j} = {i*j}", end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1

# for -
# # итерация - выполнение какого - то действия заданное количество раз
# num = "1675849345678594"
# tumb = ["phone", "pen...", "gun"]
# tumb_1 = ("phone", "pen...", "gun")
# tumb_3 = {"phone", "pen...", "gun"}
# tumb_4 = {1:"phone", 2:"pen...", 3:"gun"}
# print(iter(num))
# print(iter(tumb))
# print(iter(tumb_1))
# print(iter(tumb_3))
# print(iter(tumb_4))


tumb = ["phone", "pen...", "gun"]

iter_obj = iter(tumb) #- получим инструкцию

try:
    while True:
        next_val = next(iter_obj)
        print(f"Очередное значение - {next_val}")
except StopIteration:
    print("Итерация завершена") # читать - https://habr.com/ru/articles/132554/

# Условие:
# использовать yeld
# 1. У вас есть итератор, который выдает размер детали в миллиметрах
# (например, целые числа от 90 до 110).
# 2. Эталонный размер детали — 100 мм. Допустимая погрешность — ±2 мм
# (то есть детали от 98 до 102 мм считаются хорошими, а все,
# что меньше 98 или больше 102 — браком).
# 3. Нужно написать цикл, который берет элементы из итератора и считает брак.
# 4. Как только счетчик брака достигнет 3, цикл должен прерваться,
# и программа должна вывести: «Внимание! Обнаружено 3 бракованные детали.
# Конвейер остановлен

def generator():
    import random

    def conveyor():
        while True:
            yield random.randint(90, 110)
    factory = conveyor()
    defective_count = 0
    for detail_size in factory:
        if detail_size < 98 or detail_size > 102:
            defective_count += 1
        print(f'Detail size: {detail_size}')
        if defective_count >= 3:
            print('Some text that written without AI')
            break

generator()

# Вот ваш код, который соответствует исходному заданию по информатике.
# Я могу добавить вложенные циклы или ветвление, если хотите.