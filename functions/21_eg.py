# HOD

def d1(para1):
    return "d1 function first",para1()

def d2():
    return "d2 function second"

print(d1(d2))

# with two parameter

def a1 (p1,p2):
    return "hello" , p1(),p2()
def a2 ():
    return "hy"
def a3 ():
    return "hi"
print(a1(a2,a3))