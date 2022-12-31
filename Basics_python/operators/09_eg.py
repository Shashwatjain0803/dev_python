# Identity Operators
l1 = [10,20,30,40,50]
l2 = [10,20,30,40,50]
print(l1 is l2) # False # ref
print(l1 == l2) # True # content

l3 = [10,20,40,40,50]
l4 = [100,200]
print(l3 == l4)
print(l3 is l4)