# outer function inner function
def outerFunction():
    print("Outer Function")
    def innerFunction():
        print("Inner Function")
    innerFunction()

outerFunction()