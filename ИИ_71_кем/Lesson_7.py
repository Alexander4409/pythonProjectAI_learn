rows = 5
colms = 5

matrix = [["1" if r + c == 4 else "0" if r + c == 3 or r + c == 2 or r + c == 1 or r + c == 0 else "2" if r + c == 5 or r + c == 6 or r + c == 7 or r + c == 8 else "*" for c in range(colms)] for r in range(rows)]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
