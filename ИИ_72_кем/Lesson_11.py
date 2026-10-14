import json

from ИИ_71_кем.Lesson_13 import players

# to_do_list = ["learn python", "food", "sleep", "learn english"]

# __file save__
# with open("tasks.json", "w", encoding="utf-8") as file:
#     json.dump(to_do_list,file,ensure_ascii=False, indent = 4)
# print(f"File was created")

# __file read__
# with open("tasks.json", "r", encoding="utf-8") as file:
#     load_list = json.load(file)
#
# print(load_list)

# __update file__
# print()
# to_do_list.append("go to shop")
#
# with open("tasks.json", "w", encoding="utf-8") as file:
#     json.dump(to_do_list, file, ensure_ascii=False, indent=4)
# print(to_do_list)

players_db = {
    "proGammer_99":{"level":5, "score":0,"items":["diamond axe", "iron sword"]},
    "SinygenPro":{"level":67,"score":1400, "items":["nige...", "big pencil"]}
}

with open ('players.json','w', encoding="utf-8") as file:
    json.dump(players_db, file, ensure_ascii=False, indent= 4)