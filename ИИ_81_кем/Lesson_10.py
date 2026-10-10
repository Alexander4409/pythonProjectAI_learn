class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 1. Центрированный обход (In-order): Лево -> Корень -> Право
def traverse_in_order(node):
    if node:
        traverse_in_order(node.left)
        print(node.value, end=" ")
        traverse_in_order(node.right)

# 2. Прямой обход (Pre-order): Корень -> Лево -> Право
def traverse_pre_order(node):
    if node:
        print(node.value, end=" ")
        traverse_pre_order(node.left)
        traverse_pre_order(node.right)

# 3. Обратный обход (Post-order): Лево -> Право -> Корень
def traverse_post_order(node):
    if node:
        traverse_post_order(node.left)
        traverse_post_order(node.right)
        print(node.value, end=" ")




root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# ЗАПУСКАЕМ ОБХОДЫ

print("1. In-order (Лево-Корень-Право):")
traverse_in_order(root)


print("\n\n2. Pre-order (Корень-Лево-Право):")
traverse_pre_order(root)


print("\n\n3. Post-order (Лево-Право-Корень):")
traverse_post_order(root)

