import time
from idlelib.config_key import AVAILABLE_KEYS

robot_state = {
    "status": "Ожидает заказ",
    "temperature": 22,
    "ingredients": {
        "Тесто":5,
        "Соус":5,
        "Сыр":5,
        "Пеперони":4
    },
    "current_pizza":[],
    "orders_completed": 0,
}


AVAILABLE_TOPPINGS = ["Сыр", "Пеперони"]

def get_status():
    return robot_state.copy()

def check_ingredients():
    inv = robot_state["ingredients"]
    return inv["Тесто"] > 0 and inv["Соус"] > 0

def start_pizza():
    if not check_ingredients():
        return False, "Недостаточно ингридиентов"

    robot_state["ingredients"]["Тесто"] -= 1
    robot_state["ingredients"]["Соус"] -= 1
    robot_state["current_pizza"] = ["основа из теста", "Соус"]
    robot_state["status"] = "Раскатываю тесто и нанесение соуса"
    return True, "Основа для пиццы готова."

def add_topping(topping):
    if topping not in AVAILABLE_TOPPINGS:
        return False, f"Ингридиент {topping} не поддерживается"
    if robot_state["ingredients"].get(topping, 0) <= 0:
        return False, f"Закончился ингридиент: {topping}"
    robot_state["ingredients"][topping] -= 1
    robot_state["current_pizza"].append(topping)
    robot_state["status"] = f"Добавление: {topping}"
    return True, f"Добавлено: {topping}"

def bake_pizza():
    if not robot_state["current_pizza"]:
        return False, "В печи пусто, сначала собери пиццу"
    robot_state["status"] = "Разогрев печи и выпекания..."
    robot_state["temperature"] = 250
    time.sleep(2)

    finished_pizza = list(robot_state["current_pizza"])
    robot_state["current_pizza"] = []
    robot_state["temperature"] = 22
    robot_state["status"] = "Ожидает заказ"
    robot_state["orders_completed"] += 1

    return True, finished_pizza

def restock_ingredients():
    for item in robot_state["ingredients"]:
        robot_state['ingredients'][item] = 5
    robot_state["status"] = "Запасы пополнены "
    return "Все ингредиенты до 5 единиц"
