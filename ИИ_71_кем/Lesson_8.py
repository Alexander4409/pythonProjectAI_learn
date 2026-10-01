rows, colms = 7, 7
matrix = []

for r in range(rows):
    row = []
    for c in range(colms):
        if r == rows // 2 or c == colms // 2:
            row.append(".")
        elif c == r:
            row.append(1)
        elif c == colms - 1 - r:
            row.append(1)
        elif c == r + 1:
            row.append(2)
        elif c == r - 1:
            row.append(2)
        elif c == (colms - 1 - r) - 1:
            row.append(2)
        elif c == (colms - 1 - r) + 1:
            row.append(2)
        else:
            row.append(0)
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
