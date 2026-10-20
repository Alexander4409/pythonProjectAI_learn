# Замыкания
# def outer():
#     num = 5
#     def inner():
#         nonlocal num
#         num += 1
#         print(f"inner result - {num}")
#
#     return inner
#
#
# fu = outer()
#
# fu()
# fu()
# fu()
# fu()
# fu()

# применение параметров
# def mult(num):
#     def inner(num_2): return num*num_2
#
#     return inner
#
#
# fu = mult(5)
#
# print(fu(1))
# print(fu(2))
# print(fu(3))
# print(fu(4))

# Оптимизация

def mult(num):return lambda num_1: num*num_1


fu = mult(5)

print(fu(1))
print(fu(2))
print(fu(3))
print(fu(4))

