# discard and remove
s1 = {10,20,30,40,50}
s1.remove(30)
print(s1) # KeyError: 60

s2 = {10,20,30,40,50}
s2.discard(60)
print(s2)

# pop
s3 = {10,20,30,40,50}
print(s3.pop()) # 59
print(s3)
print(s3.pop()) # 30
print(s3.pop()) # 40
print(s3.pop()) # 10
print(s3.pop()) # 30
print(s3)