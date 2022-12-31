a,b ,c  = 50,80,90

def S1():
    return globals()
print(S1())
def S2():
    l,m,n = 66,77,88
    return locals()
print(S2())
