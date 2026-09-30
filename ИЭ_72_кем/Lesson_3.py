# инкремент
# num = 12
# num_1 = num + 2
# # синтаксический сахар - += / -=
# print(num)

num_1 = int(input(" введите 1ое число "))
num_2 = int(input(" введите 2ое число "))

operation = int(input(f"___Выбор операции___\n"
                      f"1 - сложение\n"
                      f"2 - вычитание\n"
                      f"3 - деление"))
# дописать меню для пользователя

if operation == 1:
    print(num_1+num_2)
elif operation == 2:
    print(num_1-num_2)
elif operation == 3:
