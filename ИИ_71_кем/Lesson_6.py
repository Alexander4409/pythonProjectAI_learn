# Многомерные массивы (списки)
# matrix = [[1,2,3],[3,4,5],[6,7,8]]
# matrix[1][1]=0
# print(matrix)
# вывод матрици
# for row in matrix:
#     for item in row:
#         print(item, end=" ")
#     print()

# генератор матрицы
rows, colms = 5,10
matrix = [["*" for _ in range(colms)] for _ in range(rows)]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

