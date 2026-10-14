import json
players_db = {
    "proGammer_99":{"level":5, "score":0,"items":["diamond axe", "iron sword"]},
    "SinygenPro":{"level":67,"score":1400, "items":["nige...", "big pencil"]}
}
#--Save info in dictionary
with open ('players.json','w', encoding="utf-8") as file:
    json.dump(players_db, file, ensure_ascii=False, indent= 4)

#--read info
with open ('players.json','r', encoding="utf-8") as file:
    curent_DB = json.load(file)

for player in curent_DB.items():
    print(player)

#--update info
curent_DB["proGammer_99"]["level"] = 6
curent_DB["proGammer_99"]["items"].append('new_armor')

curent_DB["misha_the_camper"]={"level":1, "score":0,"items":[]}
with open("players.json", "w", encoding="utf-8") as file:
    json.dump(curent_DB,file,ensure_ascii=False,indent=4)


with open ('players.json','r', encoding="utf-8") as file:
    curent_DB = json.load(file)

for player in curent_DB.items():
    print(player)

#задача написать робота пицемейкера
# робот должен принимать заказ от пользователя (учитывать что пользователь может придти не один)
# робот должен предоставить разное меню для разновозрастных пользователей, после идентификации
# пользователя и определения тех позиций которые пользователь хочет купить робот должен спросить,
# как будет проходить оплата (наличнкой или кртой) в случии налички
# пользователь вводит число боле суммы, а робот выдает сдачу
# Код должен сохранять заказы пользователя в файле json и история заказов должна быть доступна через
# панель аднимистратора