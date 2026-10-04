from random import randint

rows, colms = 50, 50
border = 3

patterns = {
    1: [
        "***",
        "***",
    ],
    2: [
        ".**.",
        "****",
        ".**.",
    ],
    3: [
        "*...",
        "***.",
        "****",
        ".***",
    ],

    4: [
        ".***.",
        "*****",
        "*****",
        ".***.",
    ],
    5: [
        "**...",
        "****.",
        ".****",
        "...**",
    ],
}

#Поворачавает острова на 90 градусов, чтобы было больше патернов
def rotate(shape):
    return ["".join(row[i] for row in reversed(shape)) for i in range(len(shape[0]))]

#Проверка на возможность поставить остров: не залезает ли он за края
def can_place(matrix, shape, top, left):
    h, w = len(shape), len(shape[0])
    if top < border or left < border or top + h > rows - border or left + w > colms - border:
        return False
    for r in range(h):
        for c in range(w):
            if shape[r][c] != "*":
                continue
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if matrix[top + r + dr][left + c + dc] == "*":
                        return False
    return True

#Функция размещения
def place(matrix, shape, top, left):
    for r in range(len(shape)):
        for c in range(len(shape[0])):
            if shape[r][c] == "*":
                matrix[top + r][left + c] = "*"

#Генерация матрицы
def generate(count, density):
    matrix = [["\033[94m0\033[0m" for _ in range(colms)] for _ in range(rows)]
    max_radius = min(rows, colms) // 2 - border
    radius = max(3, max_radius * (11 - density) // 10)
    cy, cx = rows // 2, colms // 2
    placed = 0
    attempts = 0
    while placed < count and attempts < count * 500:
        attempts += 1
        shape = patterns[randint(1, len(patterns))]
        for _ in range(randint(0, 3)):
            shape = rotate(shape)
        h, w = len(shape), len(shape[0])
        top = cy + randint(-radius, radius) - h // 2
        left = cx + randint(-radius, radius) - w // 2
        if can_place(matrix, shape, top, left):
            place(matrix, shape, top, left)
            placed += 1
            attempts = 0
        elif attempts % 200 == 0 and radius < max_radius:
            radius += 1
    return matrix, placed


count = int(input("Количество островов: "))
density = max(1, min(10, int(input("Плотность (1-10): "))))

matrix, placed = generate(count, density)

for row in matrix:
    for item in row:
        if item == "*":
            item = "\033[92m*\033[0m"
        print(item, end=" ")
    print()

if placed < count:
    print(f"Поместилось островов: {placed}")
