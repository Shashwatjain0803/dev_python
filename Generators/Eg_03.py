def d1(a, b):
    while a<=b:
        yield a
        a=a+1

d = d1(1,5)
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
