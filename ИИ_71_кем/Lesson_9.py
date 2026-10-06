#Задача на острова УЛЬТРА МЕГА СЛОЖНЫЙ УРОВЕНЬ !!!
# нужно генерировать карту островов на карте
# острова состоят из суши - * и полностю окружены водой - 0
# карта должна генерироваться рандомно
# правила генерации -
# 1 запрещается внутри острова генерить воду
# 2 остров должен быть полностью окружен водой
# 3 запрещается делать еденичный остров,  минимум 5 - *
# 4 край карты должен быть заполнен водой в 3 ряда
# пользователь выбирает количество и плотность расположение островов относительно центра карты


#программа на 85% написана ИИ
#а так всё другое я написала
#ыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыы
#ъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъъ
#ыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыы
#я специально попросил дипсик сделать некоторые части математичискими, а какие вот не знаю

import random

#скока на скока
width = 100
height = 100
#символики запрещённые на территории РФ
water = '0'
land = '*'
border = 3
min_island_size = 5

def create_empty_map():
    return [[water for _ in range(width)] for _ in range(height)]

def grow_island(seed_y, seed_x, target_size):
    cells = {(seed_y, seed_x)}
    frontier = [(seed_y, seed_x)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(cells) < target_size:
        random.shuffle(frontier)
        progressed = False
        for (cy, cx) in frontier[:]:
            random.shuffle(directions)
            for (dy, dx) in directions:
                ny, nx = cy + dy, cx + dx
                if (ny, nx) not in cells:
                    cells.add((ny, nx))
                    frontier.append((ny, nx))
                    progressed = True
                    break
            if progressed and len(cells) >= target_size:
                break
        if not progressed:
            break
    return cells

def island_fits(cells):
    for (y, x) in cells:
        if y < border or y >= height - border:
            return False
        if x < border or x >= width - border:
            return False
    for (y, x) in cells:
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                ny, nx = y + dy, x + dx
                if 0 <= ny < height and 0 <= nx < width:
                    if (ny, nx) not in cells and grid[ny][nx] == land:
                        return False
    return True

def place_island(cells):
    for (y, x) in cells:
        grid[y][x] = land


def generate_map(num_islands, density):
    global grid
    grid = create_empty_map()

    center_y = height // 2
    center_x = width // 2

    max_spread_y = (height - 2 * border) // 2
    max_spread_x = (width - 2 * border) // 2
    spread_y = max(1, int(max_spread_y * density))
    spread_x = max(1, int(max_spread_x * density))

    placed = 0
    attempts = 0
    max_attempts = num_islands * 500

    while placed < num_islands and attempts < max_attempts:
        attempts += 1

        oy = int(random.gauss(0, spread_y / 2)) if spread_y > 0 else 0
        ox = int(random.gauss(0, spread_x / 2)) if spread_x > 0 else 0
        seed_y = center_y + oy
        seed_x = center_x + ox

        target_size = random.randint(min_island_size, 20)

        cells = grow_island(seed_y, seed_x, target_size)
        if len(cells) < min_island_size:
            continue

        if island_fits(cells):
            place_island(cells)
            placed += 1

    return placed


def print_map():
    for row in grid:
        print(''.join(row))


# паехали
if __name__ == "__main__":
    try:
        n = int(input("количество островов (не больше 400. а то программа сдохнет): ") or 8)
        d = float(input("плотность у центра (0.1 кучно — 1.0 разбросано): ") or 0.5)
        input("так же тут используются запрещённые символики на территории РФ (я вам не покажу их они же запрещённые)")
        inf1 = input("перед тем как начать использовать эту матрицу прочитай статью ук рф 282.4 \n"
              "сылка - https://www.consultant.ru/document/cons_doc_LAW_10699/e81ee63e1fcbf5e90a4db1f109adf1068b06b0d0/\n"
              "прочитал?")
        input("также все совпадения островов в матрице с военными базами рф в тихим океане не моих рук дело")
        inf2 = input("напишите - отдаю свою душу ярославу беркенёву \n"
              "иначе расстрел")
    except ValueError:
        n, d = 8, 0.5

    if inf2 == "отдаю свою душу ярославу беркенёву":
        print(f"молодец что написал(-а), производится взлом жопы")
    else:
        print("вы приговариваетесь к расстрелу, но перед этим посмотрите матрицу, а то мне ноль поставят")
    grid = create_empty_map()
    placed = generate_map(n, d)
    print_map()
    print(f"\nРазмещено островов: {placed} из {n}\n"
          f"{inf1} - вот твой ответ на вопрос прочитал ли ты статью ук рф 282.4")
