
# документация - изучить https://networkx.org/documentation/stable/tutorial.html#analyzing-graphs

import heapq
from os.path import pathsep


def dijkstra(graph, start, target):
    distances = {node:float('inf')for node in graph}
    distances[start] = 0

    pred_distance = {node: None for node in graph}

    priority_queue = [(0,start)]

    while priority_queue:
        curent_distance, curent_node = heapq.heappop(priority_queue)

        if curent_distance > distances[curent_node]:
            continue

        for neighbor, weight in graph[curent_node].items():
            distances = curent_distance + weight

            if distances < distances[neighbor]:
                distances[neighbor] = distances
                pred_distance[neighbor] = curent_node
                heapq.heappush(priority_queue,(distances,neighbor))

    path = []
    current = target
    while current is not None:
        path.insert(0,current)
        current = pred_distance[current]

    return path,distances[target]

road_map = {
    'home':{'shop':5,'intersection':2},
    'shop':{'home':5,'unicum':6},
    'intersection':{'home':2, 'shop':1,'unicum':7},
    'unicum':{'shop':6,'intersection':7}
}

path, time = dijkstra(road_map,"home", 'unicum')
print(f'Most short way to: {path} will take {time} minutes')