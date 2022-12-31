# outer function inner function (hod)
def outerFunction(a,b):
    print(a, b) # 10 20
    def innerFunction(c, d):
        print(c, d)
    return innerFunction

o = outerFunction(10,20)
print(o.__name__) # innerFunction
o(30,40)
