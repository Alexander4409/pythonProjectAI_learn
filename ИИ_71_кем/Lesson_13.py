import json

to_do_list = ["by milk", "wash dish", "Learn python"]
# file save
with open('tasks.json', 'w', encoding='utf-8') as file:
    json.dump(to_do_list,file,ensure_ascii=False, indent=4)
print("To do list has been created !")