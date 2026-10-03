rows, colms = 30,30

matrix = []

for r in range(rows):
    row = []

    for c in range(colms):
        colms_middle = colms / 2 - 1
        rows_middle = rows / 2 - 1

        if c == colms_middle:
            row.append("*")
        elif r == c:
            row.append("*")
        elif r == rows_middle:
            row.append("*")
        elif r + c == colms - 1:
            row.append("*")
        else:
            row.append(".")

    matrix.append(row)

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# 5. Найдите индексы первого вхождения максимального элемента. Выведите два числа:
# номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
# Если таких элементов несколько, то выводится тот, у которого меньше номер строки,
# а если номера строк равны то тот, у которого меньше номер столбца.
# Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
