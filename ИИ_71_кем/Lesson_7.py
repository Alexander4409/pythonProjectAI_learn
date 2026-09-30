rows = 5
colms = 5

matrix = [["." if r % 2 == 0 and c % 2 == 0 or r == c or c == 3 and r == 1 or c == 1 and r == 3 else "*" for c in range(colms)] for r in range(rows)]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
