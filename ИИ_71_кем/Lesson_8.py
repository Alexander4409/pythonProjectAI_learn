rows = 11
cols = 11
matrix = []

for r in range(rows):
    row = []
    for c in range(cols):
        if r == c or r + c == 10 or r == 5 or c == 5:
            row.append("*")
        else:
            row.append(".")
    matrix.append(row)

for r in range(rows):
    for c in range(cols):
        if r == c or r + c == 10:
            for dc in [-1, 1]:
                nc = c + dc
                if 0 <= nc < cols and matrix[r][nc] == ".":
                    matrix[r][nc] = "*"

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
