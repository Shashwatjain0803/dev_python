print("before")
try:
    l1 = [10,20,30,40]
    print(l1[8])
except IndexError:
    print("IndexError")
print("after")
