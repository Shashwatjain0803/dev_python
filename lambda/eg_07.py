def d1(a,b):
    if a>b:
        return a
    else:
        return b

d = d1(10,20)
print(d)

d1 = lambda a, b : a if a>b else b
d = d1(10,20)
print(d)