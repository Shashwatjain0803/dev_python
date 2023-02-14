import pandas as p

l = [10,20,30,40,50]
print(p.Series(l))

l2 = [10,20,30,40,50]
print(p.Series(l2,index=["z","b","c","o","u"]))