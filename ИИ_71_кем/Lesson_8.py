rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = []
number = 1
for r in range(rows):
    row = []
    for c in range(cols):
        row.append(number)
        number += 1
    matrix.append(row)
for row in matrix:
    for item in row:
        print(f"{item:<4}", end=" ")
    print()
max_value = matrix[0][0]
best_row = 0
best_col = 0
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] > max_value:
            max_value = matrix[r][c]
            best_row = r
            best_col = c

print(max_value)
print(best_row, best_col)
