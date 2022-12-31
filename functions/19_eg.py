# outer function inner function (hod)
def d1(a):
    def d2(b):
        return a+b
    return d2

d = d1(10)
print(d(20))
