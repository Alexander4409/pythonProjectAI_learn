import random

n, m = map(int, input("Введите n и m через пробел: ").split())
matrix = [[random.randint(1, 1000) for _ in range(m)] for _ in range(n)]
print("\nСгенерированная матрица:")
for row in matrix:
    print(*(f"{num:4}" for num in row))
max_val = matrix[0][0]
best_row, best_col = 0, 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            best_row, best_col = i, j
print(f"\nМаксимальный элемент: {max_val}")
print(f"Индексы первого вхождения (строка, столбец): {best_row} {best_col}")

n = 15
center = n // 2
for i in range (n):
    row = ["*" if i == center or j == center or i == j or i + j == n - 1 else "." for j in range(n)]
    print("".join(row))
