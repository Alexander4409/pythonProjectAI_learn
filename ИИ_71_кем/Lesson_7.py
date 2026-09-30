rows = 5
colms = 5

matrix = [["0" if r + c == 4 else "1" if r + c == 3 or r + c == 5 else "2" if r + c == 2 or r + c == 6 else "3" if r + c == 1 or r + c == 7 else "4" if r + c == 0 or r + c == 8 else "*" for c in range(colms)] for r in range(rows)]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

rows = 5
colms = 5

matrix = [["." if r % 2 == 0 and c % 2 == 0 or r == c else "*" for c in range(colms)] for r in range(rows)]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
