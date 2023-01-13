#{syntax}-----
# expression(element) for element in iterable if condition if condition
l = [i for i in range(50) if i%2==0 if i%5==0]
print(l)

#{syntax}-----
# [expression(element) if condition else condition for i in iterable]
names = ["joy","joy","joys","joys","joy"]
l2 = [i if i == "joy" else "not joy" for i in names]
print(l2)