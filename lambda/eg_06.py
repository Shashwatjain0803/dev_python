def d1(a=5):
    def d2(b):
        return a+b
    return d2

d = d1(10)
print(d)
print(d(5))

# lambda
d1 = lambda a=5 : lambda b : a+b
d2 = d1(10)
print(d2(5))