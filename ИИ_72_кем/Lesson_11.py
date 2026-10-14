import json

to_do_list = ["learn python", "food", "sleep", "learn english"]

# __file save__
# with open("tasks.json", "w", encoding="utf-8") as file:
#     json.dump(to_do_list,file,ensure_ascii=False, indent = 4)
# print(f"File was created")

# __file read__
with open("tasks.json", "r", encoding="utf-8") as file:
    load_list = json.load(file)

print(load_list)