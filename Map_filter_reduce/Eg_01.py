# Multiply Iterables
l1 = [10,20,30,40,50]
print(l1*2) # [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

# for loop and lambda
lst = [10,20,30,40,50]
l = []
r = lambda n : n*2
for i in lst:
    l.append(r(i))
print(l) # [20, 40, 60, 80, 100]

# map(func, iterable)
lst = [10,20,30,40,50]
def d1(n):
    return n*2
r = map(d1, lst)
print(r) # <map object at 0x102baee30>
print(list(r)) # [20, 40, 60, 80, 100]

print(list(map(lambda n:n*2, [10,20,30,40,50]))) # [20, 40, 60, 80, 100]