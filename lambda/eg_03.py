# without lambda functions
def d1(a,b):
    return a+b

d = d1(10,20)
print(d)

# lambda
d1 = lambda a,b: a+b
d = d1(10,20)
print(d)