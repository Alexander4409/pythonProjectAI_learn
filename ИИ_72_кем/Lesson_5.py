# список
# lst = [1, "pencil", True, 3.14]
# lst.append(5)
# print(lst)
# lst.pop(2)
# print(lst)

# lst_m = [[1,1,1],[2,5,2],[3,3,3]]
# print(lst_m[1][1])

rows, colms = 5, 5

matrix = [["*" for _ in range (rows)] for _ in range (colms)]

for row in matrix:
    for item in row:
        print(item, end = " ")
    print()


