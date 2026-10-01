n = int(input())

rows = n
colms = n

matrix = []


for i in range(rows):
    matrix.append(["."] * colms)

for i in range(rows):
    for j in range(colms):

        if i == rows // 2:
            matrix[i][j] = "*"

        elif j == colms // 2:
            matrix[i][j] = "*"

        elif i == j:
            matrix[i][j] = "*"

        elif i + j == rows - 1:
            matrix[i][j] = "*"
for i in range(rows):
    print(*matrix[i])
