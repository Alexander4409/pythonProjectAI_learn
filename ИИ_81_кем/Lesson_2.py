#Списки и их методы - https://metanit.com/python/tutorial/3.1.php
#иитератор
# tumb = ("apple", "socks", "pen")
# tumb.append("pencil")
# print(tumb)
# перебор посредством цикла for
# for obj in tumb:
#     print(obj)
#
# print(iter(tumb))
#инкапсулированнная инструкция перебора объекта  - <tuple_iterator object at 0x0000025DB11D1C00>

# tumb = ["apple", "socks", "pen"]
#
# it = iter(tumb)
#
# try:
#     while True:
#         next_value = next(it)
#         print(f"value {next_value}")
# except StopIteration:
#     print("Iteration stop")
# print("program complete")

#класс тумбочка с ящиками
class Tumb:
    "класс тумбочка"
    def __init__(self):
        self.boxes = {
            1:[],
            2:[],
            3:[]
        }

    def add_to_box(self,obj,box_num):
        if box_num not in {1,2,3}:
            print("Enter a valid value!")
        else:
            self.boxes[box_num].append(obj)

    def remove_from_box(self,box_num):
        if box_num not in {1, 2, 3}:
            print("Enter a valid value!")
        else:
            return self.boxes[box_num].pop()

    def __str__(self):
        boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        return ", ".join(boxes_items)

    def __iter__(self):
        # получить сумму всех ящиков
        # boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        # # получение итератора
        # for el in boxes_items:
        #     yield el, id(el)
        return TumbIterator


class TumbIterator:
    pass




tumb_1 = Tumb()
tumb_1.add_to_box("ножницы",1 )
tumb_1.add_to_box("карандаш",2 )
tumb_1.add_to_box("яблоко",3 )
tumb_1.add_to_box("книга",1 )
#
# print(tumb_1)

# придумать правило итерации у тумбочки

# так не делаем !
my_ugly_list = [[{},[]],{},"",tumb_1]

for some_collection in my_ugly_list:
    for el in some_collection:
        print(el)

