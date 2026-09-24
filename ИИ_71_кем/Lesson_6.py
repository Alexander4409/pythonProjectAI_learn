rows, colms = (9, 25)
matrix = [["❤️" for _ in range(colms)] for _ in range(rows)]
text = "я люблю ивана николаевича"
middle_row = rows // 2
start_col = (colms - len(text)) // 2
for i, char in enumerate(text):
    current_col = start_col + i
    if 0 <= current_col < colms:
        matrix[middle_row][current_col] = char
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
