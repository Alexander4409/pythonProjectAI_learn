# словари (хеш таблици)
# dictionary = {"key":"value", 1:"Tom", 2:"Bob"}
# print(dictionary)


# users_emails = {"Bob":"bobexanple@gmaol.ru", "Петя":"Русскаясуперпочта@яндекс.ру"}
# users_lst = [["+1211121","Tom"],
#              ["+323232224","Bob"],
#              ["+24342443","Mary"]]
#
# users_dict = dict(users_lst)
# print(users_dict)

# dictionary = {"key":"value", 1:"Tom", 2:"Bob"}
# print(dictionary)
# #получение значений
# print(dictionary[2])
#
# # заменить значение
# dictionary[1] = "Корзаев"
# print(dictionary[1])
#
# # get(key, default)
# print(dictionary.get(1))
# # удаление элементов del
#
# del dictionary[1]
# print(dictionary)
#
# key = 2
# pop_del_elem = dictionary.pop(key)
# print(pop_del_elem)
# print(dictionary)

# user_dict = {"+132344243":"Ваня"}
# users_dict.update(user_dict)
# print(users_dict)

#Итерация по словарю
# dictionary = {"key":"value", 1:"Tom", 2:"Bob"}
#
# for key, value in dictionary.items():
#     print(f"key - {key}, value -  {value}")

# комплексные словари
users = {"Tom":{"phone":+595534534,
                "email":"Super@user.com",
                "spin_code":2},
         "Bob":{"phone":+595534542,
                "email":"Super@user1.com",
                "spin_code":1}}

bob_spin_code = users["Bob"]["spin_code"]
print(bob_spin_code)

for person, info in users.items():
    print(f"Пользователь: {person}")
    for key, value in info.items():
        print(f"  {key}: {value}")

# удалить и добавить пользователей