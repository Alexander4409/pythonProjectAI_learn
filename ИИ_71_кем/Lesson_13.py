import json

# to_do_list = ["by milk", "wash dish", "Learn python"]

# # file save
# with open('tasks.json', 'w', encoding='utf-8') as file:
#     json.dump(to_do_list,file,ensure_ascii=False, indent=4)
# print("To do list has been created !")

# file read
# with open('tasks.json', 'r', encoding="utf-8") as file:
#     load_file = json.load(file)
# print(f"Load file content - {load_file}")
#
# #file rewrite
#
# load_file.append('Learn biology')
# with open("tasks.json", "w", encoding="utf-8") as file:
#     json.dump(load_file, file ,ensure_ascii= False, indent=4)
# print(load_file)

import json
players = {
    'Froggy':{"level": 5, "score": 12, "items": ["dimond pickaxe"]},
    'Dimaaaaa':{"level": 45, "score": 2212, "items": ["dimond pickaxe"],}
}

with open("players.json", "w", encoding="utf-8") as file:
    json.dump(players, file, ensure_ascii=False, indent=4)

# Обновить словарь, создать нового игрока, изменить уровень уже существующего игрока