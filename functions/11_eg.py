
# global keyword
a = 10
b = 20
def d1():
    global c
    global d
    c = 30
    d = 40
    print('Global: ', a)
    print('Global: ', b)
    print('Local: ', c)
    print('Local: ', d)

d1()
print(c,d)

