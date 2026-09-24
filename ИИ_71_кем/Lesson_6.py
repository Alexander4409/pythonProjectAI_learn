

# 3 сгенерировать марицу по типу
#          0 * 0 * 0
#          * 0 0 0 *
#          0 0 * 0 0
#          * 0 0 0 *
#          0 * 0 * 0
# Задаем два вида строк
row_even = ["0", "*", "0", "*", "0"]
row_odd  = ["*", "0", "0", "0", "*"]
matrix = [
    row_even,
    row_odd,
    row_even,
    row_odd,
    row_even]
for row in matrix:
    print(*row)
