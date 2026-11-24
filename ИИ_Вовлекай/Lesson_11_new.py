# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(f'Кличка питомца - {self.name} \n'
#               f'Возраст питомца - {self.age}')
#
#
# dog = Animal("Kelly", 2)
# dog.name = "Kairo"
# # Проблема
# dog.age = -100
# dog.print_info()
#Инкапсуляция - Скрытие доступа к атрибутам и методам

# class Animal:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def print_info(self):
#         print(f'Кличка питомца - {self.__name} \n'
#               f'Возраст питомца - {self.__age}')
#
#
# dog = Animal("Kelly", 2)
# dog._Animal__name = "Человек паук"
#
# dog.print_info()


#Шаблон название атрибута - _ClassName__atribute
# _Animal__name
# _Animal__age

#Методы доступа get set

class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    #Сеттер - установка возраста
    def set_age(self,age):
        if 0 < age < 30:
            self.__age = age
        else:
            print("Недопустимый возраст питомца ")

    #геттер - получение значения
    def get_age(self):
        return self.__age


    def get_name(self):
        return self.__name


    def print_info(self):
        print(f'Кличка питомца - {self.__name} \n'
              f'Возраст питомца - {self.__age}')


dog = Dog("Kelly", 2)
dog.print_info()
dog.set_age(-4)
dog.set_age(4)

dog.print_info()

