#Списки и их методы - https://metanit.com/python/tutorial/3.1.php
#иитератор
tumb = ("apple", "socks", "pen")
# tumb.append("pencil")
# print(tumb)
# перебор посредством цикла for
for obj in tumb:
    print(obj)

print(iter(tumb))
#<tuple_iterator object at 0x0000025DB11D1C00>
print(iter(range(10)))
#<range_iterator object at 0x000001F9E56D02D0>
print(iter(enumerate(tumb)))
#<enumerate object at 0x0000027DF5F2E340>
print(iter(zip(tumb)))
#<zip object at 0x000001D0FB722D40>