# iterables
# l1 = []
# print(dir(l1))

l2 = [10,20,30,40,50]
print(l2)
print(type(l2))
print(l2.__iter__()) # <list_iterator object at 0x00000152ADDC6D10>
l = l2.__iter__()
print(l.__next__())
print(l.__next__())
print(l.__next__())
print(l.__next__())
print(l.__next__())
# print(l.__next__()) # stop iteration


