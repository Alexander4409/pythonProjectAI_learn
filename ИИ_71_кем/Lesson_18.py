#декораторы - модифицирую вывод функции не меняя её исходного кода
def decor(input_func):
    def output_func():
        print(10 * "*")
        input_func()
        print(10 * "*")
    return output_func()



def say_hi():
    print("hi")