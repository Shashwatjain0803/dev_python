try:
    a = 10
    b = 20
    c = 0

    print(a/b)
    print(a/c)

    l1 = [10,20,300]
    print(l1[8])
except ZeroDivisionError:
    print("ZeroDivisionError")
except IndexError:
    print("indexerror")
finally:
    print("Finally block")
