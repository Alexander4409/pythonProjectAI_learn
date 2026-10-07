import random
import numpy as np

input_height = int(input("Введите высоту карты"))
input_width = int(input("Введите ширину карты"))

map_height = max(30, input_height)
map_width = max(40, input_width)

num_islands = 5
density = 0.50

grid = np.zeros((map_height, map_width), dtype=int)
min_row = 3
max_row = map_height - 4
min_col = 3
max_col = map_width - 4

center_row = map_height / 2.0
center_col = map_width / 2.0
placed_islands = 0
attempts = 0

while placed_islands < num_islands and attempts < 2000:
    attempts += 1
    
    if density >= 1.0:
        sigma_row = 0.1
        sigma_col = 0.1
    else:
        sigma_row = ((max_row - min_row) / 2) * (1 - density + 0.05)
        sigma_col = ((max_col - min_col) / 2) * (1 - density + 0.05)
        
    rx = int(random.gauss(center_row, sigma_row))
    ry = int(random.gauss(center_col, sigma_col))
    
    rx = max(min_row, min(max_row, rx))
    ry = max(min_col, min(max_col, ry))
    
    island_size = random.randint(5, 12) 
    
    island_cells = set()
    queue = [(rx, ry)]
    
    while len(island_cells) < island_size and queue:
        curr = random.choice(queue)
        queue.remove(curr)
        
        if not (min_row <= curr[0] <= max_row and min_col <= curr[1] <= max_col):
            continue
            
        island_cells.add(curr)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = curr[0] + dx, curr[1] + dy
            if (nx, ny) not in island_cells and (nx, ny) not in queue:
                if min_row <= nx <= max_row and min_col <= ny <= max_col:
                    queue.append((nx, ny))
                    
    if len(island_cells) < 5:
        continue
        
    collision = False
    for cx, cy in island_cells:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < map_height and 0 <= ny < map_width:
                    if grid[nx, ny] == 1:
                        collision = True
                        break
            if collision: break
        if collision: break
        
    if not collision:
        for cx, cy in island_cells:
            grid[cx, cy] = 1
        placed_islands += 1


for row in grid:
    for item in row:
        if item == 1:
            print("*", end=" ")
        else:
            print("0", end=" ")
    print()
