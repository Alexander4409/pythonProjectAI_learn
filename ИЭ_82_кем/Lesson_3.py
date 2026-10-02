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
    print("Итерация завершена")