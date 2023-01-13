# without lambda functions
def d1(a=5,b=5):
    return a+b

d = d1()
print(d)

# lambda
d1 = lambda a=5,b=5: a+b
d = d1()
print(d)