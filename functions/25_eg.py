# recursion ( direct )

i = 0
def d1():
    global i
    i = i + 1
    print("d1 function", i)
    d1()

d1()