# 1. Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
rows, colms = 5, 5
matrix = []
for r in range(rows):
    row = []
    for c in range(colms):
        if r == c:
            row.append(1)
        elif r < c:
            row.append(2)
        else:
            row.append(0)
    matrix.append(row)

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
