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

# class Dog:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#
#     #Сеттер - установка возраста
#     def set_age(self,age):
#         if 0 < age < 30:
#             self.__age = age
#         else:
#             print("Недопустимый возраст питомца ")
#
#     #геттер - получение значения
#     def get_age(self):
#         return self.__age
#
#
#     def get_name(self):
#         return self.__name
#
#
#     def print_info(self):
#         print(f'Кличка питомца - {self.__name} \n'
#               f'Возраст питомца - {self.__age}')
#
#
# dog = Dog("Kelly", 2)
# dog.print_info()
# dog.set_age(-4)
# dog.set_age(4)
#
# dog.print_info()

#Аннотация свойств (декоратор @property)

# class Dog:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#
#     #геттер - получение значения
#     @property
#     def age(self):
#         return self.__age
#     #Последовательность
#     #Сеттер - установка возраста
#     @age.setter
#     def age(self,age):
#         if 0 < age < 30:
#             self.__age = age
#         else:
#             print("Недопустимый возраст питомца ")
#
#
#     @property
#     def name(self):
#         return self.__name
#
#
#     def print_info(self):
#         print(f'Кличка питомца - {self.__name} \n'
#               f'Возраст питомца - {self.__age}')
#
#
# dog = Dog("Kelly", 2)
# dog.print_info()
# dog.age=-323222
# print(dog.age)
# dog.age = 3
# dog.print_info()

#Наследование
#Супер класс(родительский класс), производный класс (Класс ребенок)
#DRYKISS

# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f"Имя - {self.__name}")
#
#
# class Employer(Person):
#
#     def work(self):
#         print(f"{self.name} works")
#
#
# class Student(Person):
#
#     def study(self):
#         print(f'{self.name} study')
#
# tom = Employer("Tom")
# print(tom.name)
# tom.display_info()
# tom.work()
#
# bob = Student("Bob")
# print(bob.name)
# bob.display_info()
# bob.study()


#Наследование от нескольких классов

# class Student:
#
#     def study(self):
#         print(f'Student - study')
#
#
# class Employer:
#
#     def work(self):
#         print(f"Employer - works")
#
#
# class WorkingStudent(Employer,Student):
#     pass
#
#
# tom = WorkingStudent()
# tom.work()
# tom.study()

# Использовать с осторожностью
# class Employer:
#
#     def do(self):
#         print(f"Employer - works")
#
#
# class Student:
#
#     def do(self):
#         print(f"Student - works")
#
#
# class WorkingStudent(Employer,Student):
#     pass
#
# tom = WorkingStudent()
# tom.do()
#
#
# print(WorkingStudent.__mro__)
# print(WorkingStudent.mro())


# Задача !
# Подсчет доходов (Инкапсуляция + Наследование)
# Возьмите за основу наш код с классами Person, Student и Employer и доработайте его так,
# чтобы можно было считать общий доход разных людей.
# 1. Базовый класс Person:
# • Оставьте приватный атрибут __name и геттер @property для него.
# 2. Класс Student (наследуется от Person):
# • При создании объекта (__init__) помимо имени принимает размер стипендии и сохраняет
# его в приватный атрибут __scholarship.
# • Сделайте метод или @property для получения размера стипендии.
# • Добавьте метод set_scholarship(amount): если передана сумма меньше 0, выведите
# предупреждение (например, "Стипендия не может быть отрицательной"), иначе обновите значение.
# 3. Класс Employer (наследуется от Person):
# • При создании объекта помимо имени принимает размер зарплаты и сохраняет его в
# приватный атрибут __salary.
# • Сделайте метод или @property для получения размера зарплаты.
# • Добавьте метод set_salary(amount): если передана сумма меньше 0, выведите
# предупреждение, иначе обновите значение.
# 4. Класс WorkingStudent (наследуется от Employer и Student):
# • Описывает человека, который и учится, и работает.
# • При создании принимает имя, зарплату и стипендию.
# • Добавьте метод get_total_income(), который возвращает сумму его
# зарплаты и стипендии.
# Проверка:
# Создайте по одному объекту каждого класса (Student, Employer, WorkingStudent),
# попробуйте задать кому-то отрицательный доход и выведите итоговый доход работающего студента.
#

# Подсказка: Чтобы внутри Student или Employer сохранить имя через родительский класс Person,
# вызовите его __init__ напрямую по имени класса, передав туда self:

# пример - Person.__init__(self, name)

# Точно так же в классе WorkingStudent можно вызвать конструкторы Employer и Student.

class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name}")


class Student(Person):
    def __init__(self, name, scholarship):
        Person.__init__(self, name)
        self.__scholarship = 0
        self.set_scholarship(scholarship)

    @property
    def scholarship(self):
        return self.__scholarship

    def set_scholarship(self, amount):
        if amount < 0:
            print("Ошибка: стипендия не может быть отрицательной!")
        else:
            self.__scholarship = amount

    def study(self):
        print(f"{self.name} учится. Стипендия: {self.__scholarship}")


class Employer(Person):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        self.__salary = 0
        self.set_salary(salary)

    @property
    def salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount < 0:
            print("Ошибка: зарплата не может быть отрицательной!")
        else:
            self.__salary = amount

    def work(self):
        print(f"{self.name} работает. Зарплата: {self.__salary}")


class WorkingStudent(Employer, Student):
    def __init__(self, name, salary, scholarship):

        Employer.__init__(self, name, salary)
        Student.__init__(self, name, scholarship)

    def get_total_income(self):
        return self.salary + self.scholarship


# --- Проверка работы ---
bob = Student("Bob", 5000)
bob.study()
bob.set_scholarship(-1000)

tom = Employer("Tom", 50000)
tom.work()

alex = WorkingStudent("Alex", 30000, 4000)
alex.display_info()
alex.work()
alex.study()
print(f"Общий доход {alex.name}: {alex.get_total_income()}")
