# frozenset
f1 = frozenset([100,200,300,400,500])
print(f1)

s1 = {10,20,30,40,50}
s1.add(f1)
print(s1) # {frozenset({100, 200, 300, 400, 500}), 50, 20, 40, 10, 30}
s1.remove(f1)
print(s1)