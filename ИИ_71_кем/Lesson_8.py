# 4. Дано нечетное число n. Создайте двумерный массив из n×n элементов,
# заполнив его символами "." (каждый элемент массива является строкой из одного символа).
# Затем заполните символами "*" среднюю строку массива, средний столбец массива,
# главную диагональ и побочную диагональ. В результате единицы в массиве должны
# образовывать изображение звездочки. Выведите полученный массив на экран,
# разделяя элементы массива пробелами.

# 5. Найдите индексы первого вхождения максимального элемента. 
# Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
# Если таких элементов несколько, то выводится тот, у которого меньше номер строки,
# а если номера строк равны то тот, у которого меньше номер столбца.
# Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.

rows, colms = 9, 9
mid_rows = rows // 2
mid_colms = colms // 2

matrix = [["." for _ in range(colms)] for _ in range(rows)]

for r in range(rows):
    for c in range(colms):
        if (abs(r - c) <= 1 or abs(r + c - (rows - 1)) <= 1 or r == mid_rows or c == mid_colms):
            matrix[r][c] = '*'

for row in matrix:
    print(' '.join(row))

# я ненавижу отступы







# второй код 

import random


def random_matrix(rows, colms):
    matrix = []
    for _ in range(rows):

        row = [random.randint(1, 100) for _ in range(colms)]  
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:

        print(*(f'{num:4}' for num in row))
    print()


def max_matrix(matrix, rows, colms):

    max_vals = matrix[0][0]

    for r in range(rows):
        for c in range(colms):
            if matrix[r][c] > max_vals:
                max_vals = matrix[r][c]

    return max_vals


def main():
    print("Введите количество строк и столбцов через пробел (например: 3 4):")
    
    rows, colms = map(int, input().split())
    matrix = random_matrix(rows, colms)

    print("\nСгенерированная матрица:")
    print_matrix(matrix)

    max_value = max_matrix(matrix, rows, colms)
    print(f'Максимальный элемент: {max_value}')


if __name__ == '__main__':
    main()
