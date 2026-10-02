import random

rows = int(input("строки введи матрицы "))
colms = int(input("столбцы введи матрицы "))
matrix = []

for r in range(rows):
    row = []
    for c in range(colms):
        row.append(random.randint(1, 1000))
    matrix.append(row)

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

max_val = matrix[0][0]
max_r = 0
max_c = 0

for r in range(rows):
    for c in range(colms):
        if matrix[r][c] > max_val:
            max_val = matrix[r][c]
            max_r = r
            max_c = c

print(f"СТроки - {max_r} / Стобцы -, {max_c}")
