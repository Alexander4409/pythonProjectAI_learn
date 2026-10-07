# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# root = Node("Директор")
#
# root.left = Node("Генеральный исполнительный директор")
# root.right = Node("Зам. директор")
#
# root.left.left = Node("Вайбкодер")
# root.left.right = Node("Программист")
#
# print("Главный - ", root.value)
# print("Подчиненный директора - ", root.left.left.value, "и", root.left.right.value)

#BST (Binary, Search, Tree)


class BSTNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def ins_data(self, value):
        if value < self.value:
            if self.left is None: # - what if !=
                self.left = BSTNode(value)
            else:
                self.left.ins_data(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.ins_data(value)

    def search_data(self,target):
        if self.value == target:
            return True

        if target < self.value and self.left:
            return self.left.search_data(target)

        if target > self.value and self.right:
            return self.right.search_data(target)

        return False

bst = BSTNode(50)

nums = [30,70,20,40,60,80]

for num in nums:
    bst.ins_data(num)

print(bst.search_data(40))
print(bst.search_data(99))

#обход бинарных деревьев
#удаление узла