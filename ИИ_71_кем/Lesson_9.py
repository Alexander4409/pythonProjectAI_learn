import random
import os

os.system('')


def generate_island_shape(min_size=5):
    size = random.randint(min_size, min_size + int(min_size * 0.5))
    island = set([(0, 0)])
    while len(island) < size:
        x, y = random.choice(list(island))
        nx, ny = random.choice([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
        island.add((nx, ny))
    return island


def can_place_island(grid, island_cells, start_r, start_c, rows, cols):
    for dr, dc in island_cells:
        r, c = start_r + dr, start_c + dc
        if r < 3 or r >= rows - 3 or c < 3 or c >= cols - 3:
            return False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if grid[r + i][c + j] == '*':
                    return False
    return True


def generate_map(rows=22, cols=40, density=10):
    grid = [['0' for _ in range(cols)] for _ in range(rows)]

    available_rows = max(0, rows - 6)
    available_cols = max(0, cols - 6)
    max_available_cells = available_rows * available_cols

    target_land_cells = int(max_available_cells * (density / 100))

    if density <= 15:
        min_island_size = 5
    elif density <= 40:
        min_island_size = 12
    else:
        min_island_size = 30

    attempts = 0
    current_land_cells = 0
    max_attempts = 2000

    while current_land_cells < target_land_cells and attempts < max_attempts:
        attempts += 1
        island_shape = generate_island_shape(min_size=min_island_size)

        if current_land_cells + len(island_shape) > target_land_cells + int(min_island_size * 0.5):
            continue

        start_r = random.randint(3, rows - 4)
        start_c = random.randint(3, cols - 4)

        if can_place_island(grid, island_shape, start_r, start_c, rows, cols):
            for dr, dc in island_shape:
                grid[start_r + dr][start_c + dc] = '*'
            current_land_cells += len(island_shape)
            attempts = 0

    return grid


def print_colored_map(grid):
    for row in grid:
        line = []
        for cell in row:
            if cell == '0':
                line.append('\033[94m0\033[0m')
            elif cell == '*':
                line.append('\033[92m*\033[0m')
        print(" ".join(line))


print("Введите плотность островов от 1 до 100%:")
try:
    user_density = float(input())
    if user_density < 1: user_density = 1
    if user_density > 100: user_density = 100
except ValueError:
    user_density = 10

island_map = generate_map(rows=25, cols=50, density=user_density)
print_colored_map(island_map)
