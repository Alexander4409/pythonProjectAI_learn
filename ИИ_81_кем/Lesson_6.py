# #графы
# social_network = {
#     "user_1":["user_2", "user_3"],
#     "user_2":["user_1", "user_4"],
#     "user_3":["user_1"],
#     "user_4":["user_2"]
# }
#
# print(f"Connections of user_1 - {social_network["user_1"]}")

# обход графа в ширину
#from collections import deque

# def bfs(graph, start, target):
#     queue = deque([[start]])
#     visited = set()
#
#     while queue:
#         path = queue.popleft()
#         node = path[-1]
#
#         if node == target:
#             return path
#
#         if node not in visited:
#             visited.add(node)
#
#             for neighbor in graph.get(node,[]):
#                 new_path = list(path)
#                 new_path.append(neighbor)
#                 queue.append(new_path)
#
#     return None
#
# social_network = {
#     "user_1":["user_2", "user_3"],
#     "user_2":["user_1", "user_4"],
#     "user_3":["user_1"],
#     "user_4":["user_2"]
# }
#
# print("Max short from user_1 to user_4", bfs(social_network, "user_1","user_4"))



