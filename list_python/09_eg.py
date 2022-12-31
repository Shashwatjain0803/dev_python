# slicing [start : end (-1) : step over ]

L1 = [ 10,20,30,40,50,60,70,80,90]

print(len(L1))
print(L1[0:6:1])
print(L1[2:8:1])
print(L1[2:12:2])

print(L1[::])
print(L1[::2])
print(L1[:6:])
print(L1[4::])


#magics
print(L1[::-1])
#print(L1[-10])
print(L1[2:9:1])
print(L1[-2:-6:-1])
