# user_dict = {"name":"Bob",
#              "age": 34,
#              "is_maried":True,
#              "company":"Microsoft"}
#вывод словаря
# print(user_dict)
#вывод конкретного значения по ключу
# print(user_dict["name"])
#изменение данных в словаре
# user_dict["is_maried"] = False
# print(user_dict["is_maried"])

# for key in user_dict:
#     print(f"{key}: {user_dict[key]}")

users = {"Tom":{"phone":+595534534,
                "email":"Super@user.com",
                "spin_code":2},
         "Bob":{"phone":+595534542,
                "email":"Super@user1.com",
                "spin_code":1}}

# print(users["Tom"])
#
# user1 = users.get("Bob")
# print(user1)

# del users["Bob"]
# print(users)
dict.update(users["Tom"],{"age": 26, "city": "Москва"})
print(users)