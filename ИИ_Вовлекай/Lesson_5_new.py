#qwargs
def reg_form(owner_name, **pets):
    print(f'Владелец - {owner_name}')
    for pet, pet_name in pets.items():
        print(f"Вид животного {pet}, Кличка(и) - {pet_name}")

reg_form("Вася", dog = "Rex", cat = ["Fluffy", "Anfisa"], parrot = ["Kesha", "Flyer"])