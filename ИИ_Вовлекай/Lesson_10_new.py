#ООП
# int, str, Bool
# class Human:
#     pass
#
#
# tom = Human()
# bob = Human()
from tkinter.font import names


#конструктор класса

# class Person:
#     #конструктор
#     def __init__(self,name,age,FMML):
#         #атрибуты (они позволяют задавать определенное состояние вашим объектам)
#         self.name = name
#         self.age = age
#         self.FMML = FMML
#
#
#
# #Определение сущностей
# tom = Person("Tom", 22, "ML")
#
# # #определение атрибута вне класса!!!
# # print(tom.company)
# # tom.company = "Microsoft"
# # AttributeError: 'Person' object has no attribute 'company'
#
# bob = Person("Bob", 24,"ML")
# mary = Person("Mary",25,"FM")
#
#
# print(tom.FMML)
# print(mary.age)
# print(tom.name)

#Методы классов
# class Person:
#     # методы - функции объекта
#     def say_hi(self):
#         print("Hi")
#
#     def say(self,message):
#         print(message)
#
#     def work(self):
#         print("Working")
#
#
# tom = Person()
# tom.say_hi()
# tom.work()
# tom.say("Привет моё имя Том")


# class Car:
#     def __init__(self,model,brend,color):
#         self.model = model
#         self.brend = brend
#         self.color = color
#
#     def dispay_info(self):
#         print(f"Модель - {self.model}, Марка автомобиля - {self.brend}, Цвет кузова - {self.color}")
#
# car_1 = Car("CRV", "Toyota", "Белый")
#
# car_1.dispay_info()
import time

class Dish:
    def __init__(self,dish_name):
        self.dish_name = dish_name
        print(f"Повар приготовил - {self.dish_name}")


    # деструктор

    def __del__(self):
        time.sleep(3)
        print(f'Еда под названием {self.dish_name} выдана посетителю ресторана')


def create_dish():
    shrimps = Dish('Креветки')

create_dish()
print("ресторан закрылся работа программы завершена")