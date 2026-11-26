import time


robot_state = {
    "status":"Ожидает заказа",
    "temperature" : 22,
    "ingredients": {
        "тесто":5,
        "соус":5,
        "сыр":5,
        "пепперони":3,
        "грибы":3,
    },
    "current_pizza":[],
    'orders_completed':0
}

AVAILABLE_TOPPINGS = ["сыр", "пепперони","грибы"]


def get_status():
    return robot_state.copy()


def check_base_ingredients():
    inv = robot_state['ingredients']
    return inv['тесто'] > 0 and inv["соус"] > 0


def start_pizza():
    if not check_base_ingredients():
        return False, "Недостаточно теста и / или соуса "

    robot_state["ingredients"]["тесто"] -=1
    robot_state['ingredients']['соус'] -=1
    robot_state['current_pizza'] = ["основа из теста", "томатный соус"]
    robot_state["status"] = "Раскатка теста и нанесение соуса"
    return True, "Основа для пиццы готова"


def add_topping(topping):
    if topping not in AVAILABLE_TOPPINGS:
        return False, f"Ингредиент  {topping} не найден или не поддерживается"

    if robot_state["ingredients"].get(topping,0) <= 0:
        return False, f"Ингредиент - {topping} закончился"

    robot_state['ingredients'][topping] -= 1
    robot_state['current_pizza'].append(topping)
    robot_state['status'] = f'Добавление - {topping}'
    return True, f'Добавлено : {topping}'


def bake_pizza():
    if not robot_state['current_pizza']:
        return False, "В печи пусто, сначала соберите пиццу"

    robot_state["status"] = "Разогрев духовки и выпекание"
    robot_state["temperature"] = 250
    time.sleep(1.5)

    finished_pizza = list(robot_state['current_pizza'])
    robot_state['current_pizza'] = []
    robot_state['temperature'] = 22
    robot_state["status"] = "Ожидает заказ"
    robot_state["orders_completed"] += 1

    return True, finished_pizza


def restock_ingredients():
    for item in robot_state["ingredients"]:
        robot_state['ingredients'][item] = 5
    robot_state["status"] = "Запасы пополнены"
    return "Все ингредиенты пополнены до 5 единиц"

