

import model
import view


def handle_make_pizza():
    #осонва
    success, msg = model.start_pizza()
    if not success:
        view.show_error(msg)
        return
    view.show_message(msg)

    #топпинги
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


def handel_show_status():
    current_state = model.get_status()
    view.show_status(current_state)


def handle_restock():
    msg = model.restock_ingredients()
    view.show_message(msg)


def run_robot():
    view.show_welcome()

    while True:
        view.show_menu()
        choice = view.ask_menu_choice()

        if choice == "1":
            handle_make_pizza()

        elif choice == "2":
