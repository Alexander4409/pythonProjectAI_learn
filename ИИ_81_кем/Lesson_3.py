
class TumbIterator:
    def __next__(self):
        pass

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
        return TumbIterator







tumb_1 = Tumb()
print(iter(tumb_1))
tumb_1.add_to_box("ножницы",1 )
tumb_1.add_to_box("карандаш",2 )
tumb_1.add_to_box("яблоко",3 )
tumb_1.add_to_box("книга",1 )
#


# придумать правило итерации у тумбочки

# my_ugly_list = [[{},[]],{},"",tumb_1]
#
# for some_collection in my_ugly_list:
#     for el in some_collection:
#         print(el)

