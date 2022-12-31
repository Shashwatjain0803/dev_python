# outer function inner function (hod)
def d1(a,b):
    def d2(c,d):
        return a+b, c-d, a/c, a+d
    return d2

d = d1(10,20)
print(d(30,40))
