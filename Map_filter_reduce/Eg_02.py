# Multiply Iterables
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
# print(l1*l2) # TypeError: can't multiply sequence by non-int of type 'list'

def d1(a, b):
    return a*b
result = map(d1, l1,l2)
print(result)
print(list(result))

print(list(map(lambda a,b:a*b,l1,l2)))