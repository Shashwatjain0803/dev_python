f = open("one.txt","r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read())
f.seek(0)
print(f.read())