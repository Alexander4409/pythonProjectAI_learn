# #декораторы - модифицирую вывод функции не меняя её исходного кода
# def decor(input_func):
#     def output_func():
#         print(10 * "*")
#         input_func()
#         print(10 * "*")
#     return output_func
#
#
# @decor
# def say_hi():
#     print("hi")
#
#
# @decor
# def say_bye():
#     print("bye")
#
# say_hi()
# say_bye()

def checker_decor(input_func):
    def output_func(*args):
        name = args[0]
        age = args[1]
        if age < 0: age = "Error"
        input_func (name,age)
    return output_func


@checker_decor
def print_person(name,age):
    print(f'name - {name}, age - {age}')

print_person('Tom', 9)
print_person('Jeffry', 56)
print_person('Marta', 23)
print_person('Donald', -9999999999999)

