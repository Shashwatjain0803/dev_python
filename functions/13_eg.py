# globals() and locals()
def d1():
    a = 10
    b = 20
    print(a, b)
    print(locals()['a'], locals()['b'])
    locals()['a'] = 100
    locals()['b'] = 200
    print(a, b)

d1()