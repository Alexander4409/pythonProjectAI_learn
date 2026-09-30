# список
# lst = [1, "pencil", True, 3.14]
# lst.append(5)
# print(lst)
# lst.pop(2)
# print(lst)

# lst_m = [[1,1,1],[2,5,2],[3,3,3]]
# print(lst_m[1][1])

rows, colms = 5, 5

matrix = [["*" if r == 2 or c == 2 else "0" for c in range(colms)]for r in range(rows)]

for row in matrix:
    for item in row:
        print(item, end = " ")
    print()

# 0 0 * 0 0
# 0 0 * 0 0
# 0 0 * 0 0
# 0 0 * 0 0
# 0 0 * 0 0

# 0 0 * 0 0
# 0 0 * 0 0
# * * * * *
# 0 0 * 0 0
# 0 0 * 0 0
