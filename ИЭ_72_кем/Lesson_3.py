# инкремент
# num = 12
# num_1 = num + 2
# # синтаксический сахар - += / -=
# print(num)
while True:
    try:


        operation = int(input(f"___Меню для пользователя___\n"
                              f"1 - сложение\n"
                              f"2 - вычитание\n"
                              f"3 - деление\n"
                              f"4 - остановка программы"))

        num_1 = int(input(" введите 1ое число "))
        num_2 = int(input(" введите 2ое число "))

        # дописать меню для пользователя

        if operation == 1:
            print(num_1 + num_2)
        elif operation == 2:
            print(num_1 - num_2)
        elif operation == 3:
            try:
                res = num_1 / num_2
                print(res)
            except ZeroDivisionError:
                print("Error2")
        elif operation == 4:
            break

    except ValueError:
        print("Error1")




