# циклы
# for, while

#while - цикл работает при наличии условия

#Глупый счётчик
num = 0

while num <= 15:
    num += 1
    if num == 7:
        continue

    print(num)

    if num == 7:
        print(f"Аварийная остановка кода, число = {num}")
        break #- остановку цикла




