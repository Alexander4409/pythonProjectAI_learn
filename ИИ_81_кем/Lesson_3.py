
class TumbIterator:
    def __init__(self,some_objects):
        self.some_objects = some_objects
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.some_objects):
            result = self.some_objects[self.current]
            self.current += 1
            return result
        raise StopIteration


    def to_start(self):
        self.current = 0

    def to_current(self,val):
        if val >= len(self.some_objects) or val < 0:
            print("Cursor Error!")
        else:
            self.current = val


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
        return TumbIterator(self.boxes[1]+self.boxes[2]+self.boxes[3])




tumb_1 = Tumb()
tumb_1.add_to_box("ножницы",1 )
tumb_1.add_to_box("карандаш",2 )
tumb_1.add_to_box("яблоко",3 )
tumb_1.add_to_box("книга",1 )
#
for el in tumb_1:
    print(el)

#iter() - https://docs.python.org/3.12/library/functions.html#iter
# придумать правило итерации у тумбочки

# it = iter(tumb_1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# my_ugly_list = [[{},[]],{},"",tumb_1]
#
# for some_collection in my_ugly_list:
#     for el in some_collection:
#         print(el)

