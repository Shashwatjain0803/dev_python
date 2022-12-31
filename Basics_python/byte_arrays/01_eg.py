b1 = bytes()
print(b1)

b2 = bytes([10,20,30,40,50])
print(b2)

b3 = bytearray()
print(b3)

b4 = bytearray([10,20,30,40,50])
print(b4) # b'\n\x14\x1e(2'

# b5 = bytes([10])
# b5[0] = 100
# print(b5) # TypeError: 'bytes' object does not support item assignment

b6 = bytearray([10])
b6[0] = 100
print(b6)