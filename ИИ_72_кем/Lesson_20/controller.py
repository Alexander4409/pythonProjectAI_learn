from random import choice

import model
import view

def handle_make_pizza():
    # готовим основу
    success, msg = model.start_pizza()
    if not success:
        view.show_error(msg)
        return
    view.show_message(msg)
    # выбираем и добавляем начинки
    chosen_toppings = view.ask_toppings(model.AVAILABLE_TOPPINGS)
    for topping in chosen_toppings:
        if topping:
            ok, top_msg = model.add_topping(topping)
            if ok:
                view.show_message(top_msg)
            else:
                view.show_error(top_msg)

    # выпекание
    view.show_message("Отправляем пиццу в печь ... ")
    baked, res = model.bake_pizza()
    if baked:
        view.show_finished_pizza(res)
    else:
        view.show_error(res)

#дианов +

def handle_show_status():
    current_state = model.get_status()
    view.show_status(current_state)


def handle_restock():
    mgs = model.restock_ingredients()
    view.show_message(mgs)

def run_robot():
    view.show_welcome()
    choice = view.ask_menu_choice()

    while True:
        if choice == "1":
            handle_make_pizza()
        elif choice == "2":
            handle_show_status()
        elif choice == "3":
            handle_restock()
        elif choice == "0":
            view.show_message("Выключение системы")
            break

        else:
            view.show_error("Неизвестная команда")


