# globals() and locals()
a = 10
b = 20
def d1():
    a = 100
    b = 200
    print('Locals: ', a, b)
    print('Before: ', globals()['a'], globals()['b'])
    globals()['a'] = 30
    globals()['b'] = 40
    print('After: ', globals()['a'], globals()['b'])

d1()