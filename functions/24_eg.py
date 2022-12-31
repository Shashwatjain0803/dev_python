# decorators

def d1(func):
    def d2():
        return"d2 function", func()
    return d2

def d3():
    return "d3 function"
d = d1(d3)
print(d())

@d1
def d4():
    return"d4 function"
print(d4())