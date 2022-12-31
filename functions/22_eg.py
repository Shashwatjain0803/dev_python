# HOD
# def d1(para1):
#     return "d1 function", para1()
#
# def d2():
#     return "d2 function"
#
# print(d1(d2))

def d1(a, b):
    return "d1 function", a(), b()

def d2():
    return "d2 function"

def d3():
    return  "d3 function"

print(d1(d2, d3))

