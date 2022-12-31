# outer function inner function
def outerFunction(a,b):
    print("Outer Function", a, b)
    def innerFunction(c, d):
        print("Inner Function", c, d)
    innerFunction(30,40)

outerFunction(10,20)