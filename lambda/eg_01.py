# without lambada function
def d1():
    return print("d1 function")

d1()

# lambda args : expression
d = lambda d1 : print("d1 function")
print(d)
print(type(d))
d(d1)