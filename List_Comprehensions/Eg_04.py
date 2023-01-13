l = []
for x in [10,20,30]:
    for y in [100,200,300]:
        l.append(x+y)

print(l)

#{syntax}-----
#[expression for loop for loop]
l2 = [x+y for x in [10,20,30]  for y in [100,200,300]]
print(l2)

#comprehensions
#list comprehensions
#set comprehensions
#dict comprehensions
#generator comprehensions