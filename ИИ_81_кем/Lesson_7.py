
# документация - изучить https://networkx.org/documentation/stable/tutorial.html#analyzing-graphs

import heapq

def dijkstra(graph, start, target):
    # Главный словарь для хранения цен/расстояний
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pred_distance = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            # ИСПРАВЛЕНО: используем новую переменную new_distance вместо перезаписи distances
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                pred_distance[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = pred_distance[current]

    return path, distances[target]

road_map = {
    'home': {'shop': 5, 'intersection': 2},
    'shop': {'home': 5, 'unicum': 6},
    'intersection': {'home': 2, 'shop': 1, 'unicum': 7},
    'unicum': {'shop': 6, 'intersection': 7}
}

path, time = dijkstra(road_map, "home", 'unicum')
print(f'Most short way to: {path} will take {time} minutes')
