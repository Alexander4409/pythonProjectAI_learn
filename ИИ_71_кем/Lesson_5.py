def clothes():
    season = input("Время года: ")
    weather = input("Погода на улице: ")

    if season == "зима":
        if weather == "снег":
            print("Надень теплую куртку, теплые штаны и ботинки")
        else:
            print("Надень куртку, шапку и теплые штаны")

    elif season == "лето":
        if weather == "тепло":
            print("Надень футболку, шорты и кепку")
        else:
            print("Надень майку и открытые брюки")

    elif season == "весна" or season == "осень":
        if weather == "дождь":
            print("Надень теплую куртку, джинсы и возьми зонт")
        else:
            print("Надень ветровку и джинсы")

    else:
        print("Ты чо, введи правильное время года")


clothes()
