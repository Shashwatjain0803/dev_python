# empty set
s1 = set()
print(s1)

# insertion order is not preserved/Unordered, duplicates not allowed
# data structures hashcode
s1 = {10,20,30,40,20,40,50,60,70}
print(s1) # {50, 20, 70, 40, 10, 60, 30}

# data structures index positions
l1 = [10,20,30,40,20,40,50,60,70]
print(l1)

# remove duplicate elements using list
l1 = [10,20,30,40,20,40,50,60,70,10,20]
print(set(l1))

a = 10
b = 10.0
print(type(a), type(b))
print(a == b) # content comparisonb