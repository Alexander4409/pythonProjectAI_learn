# tumb = ["Ножницы", "книга", "карандаш"]
#
# tumb_iter = iter(tumb)
# print(tumb_iter)
# try:
#     while True:
#         next_value = next(tumb_iter)
#         print("Очередное значение", next_value)
# except StopIteration:
#     print("Иттерация завершена")


# import dis
#
#
# # Точная копия поведения оригинального list_iterator
# def имитация_list_next(it_index, my_list):
#   if it_index >= len(my_list):
#     raise StopIteration
#   value = my_list[it_index]
#   it_index += 1
#   return value, it_index
#
#
# # Смотрим байт-код этой логики
# dis.dis(имитация_list_next)
