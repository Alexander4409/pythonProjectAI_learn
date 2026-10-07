# комплексные словари
# users = {"Tom":{"phone":+595534534,
#                 "email":"Super@user.com",
#                 "spin_code":2},
#          "Bob":{"phone":+595534542,
#                 "email":"Super@user1.com",
#                 "spin_code":1}}
#
# bob_spin_code = users["Bob"]["spin_code"]
# print(bob_spin_code)
#
# for person, info in users.items():
#     print(f"Пользователь: {person}")
#     for key, value in info.items():
#         print(f"  {key}: {value}")

# удалить и добавить пользователей

users_dictionary = {"tom":99090909, "bob":353545345 }
new_user = {"john":5848848}
print(users_dictionary)
users_dictionary.update(new_user)
print(users_dictionary)

#читать - https://metanit.com/python/tutorial/3.3.php
