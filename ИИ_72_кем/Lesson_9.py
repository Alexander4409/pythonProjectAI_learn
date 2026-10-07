# def - определение функции
# процедура - не содержит return
# def say_hi():
#     print("hi")
#
# say_hi()
# say_hi()
# say_hi()
# say_hi()

# def say_name(name):
#     return f"hi {name}"
#
#
# print(say_name("Tom"))

def car_info(color,engine,T_range):
    return f"Car color - {color}, engine volume - {engine}, Total range - {T_range}"

print(car_info("red", 5, 3000))
print(car_info(3, "blue", 3000))
# именованные параметры
print(car_info(color = "blue" , engine= 5, T_range= 3000))

