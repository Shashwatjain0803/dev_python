# closure

def d1(a):
    print(a)
    def d2(b):
        print(b)
    return d2

d = d1 (10)
d(20)

del d1
#d1(100)
d(20)