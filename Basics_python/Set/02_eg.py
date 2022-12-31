print(dir(set))
# 'add',
# 'clear',
# 'copy',
# 'discard',
# 'pop',
# 'remove',
# 'update'

s1 = set()
s1.add(10)
s1.add(20)
s1.add(30)
s1.add(30.5)
s1.add(20)
s1.add(30.0)
print(s1) # {10, 20, 30, 30.5}

s1 = {10,20}
s2 = {30,40}
# s1.add(s2)
# print(s1) # TypeError: unhashable type: 'set'
s1.clear()
s2.clear()
print(s1, s2)

# copy list and set
s1 = {10,20}
print(s1.copy())
print(s1)
# print(s1*2) # TypeError: unsupported operand type(s) for *: 'set' and 'int'

l1 = [10,20]
print(l1)
print(l1.copy())
print(l1*1)
print(l1[::])