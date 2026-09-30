rows, colms = 5, 5
matrix = [["1" if i == j else "0" if i < j else "2" for j in range(colms)] for i in range(rows)]

for row in matrix:
    print(*(row))
