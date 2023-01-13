# def d1():
#     return 10
#     return 20
#     return 30
#
# d = d1()
# print(d)
# print(type(d))

# def d2():
#     return 10,20,30
#
# d = d2()
# print(d)
# print(type(d))

# def d1():
#     yield 10
#     yield 20
#     yield 30
#
# d = d1()
# print(type(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d)) # StopIteration

def d1():
    yield 10
    return 20
    yield 30

d = d1()
print(d)
print(next(d))
print(next(d))

def d1(n):
    for i in range(n):
        yield i

d = d1(5)
print(d)
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d)) # StopIteration