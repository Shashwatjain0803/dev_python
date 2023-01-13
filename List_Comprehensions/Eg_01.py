# find the range using list constructor

l1 = list(range(1,10))
print(l1)

# find the square root using list constructor
for i in list(range(1,10)):
    print(i**2)

# find the square root using list constructor and comprehensions

# {syntax}-----
#[expression for item in iterabale]

l1 = [i**2 for i in list(range(1,10))]
print(l1)

# find the square root and  even numbers
#{syntax}----
#[expresion for item in iterable if condition]
s=[i**2 for i in list(range(1,10)) if i%2==0]
print(s)
