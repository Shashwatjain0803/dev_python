s = "Hello learners like the code"
#    0123............
print(s.find('l'))
print(s.find('l'))
print(s.rfind('l'))

print(s.find('l',5,8))

print(s.find('m'))

s = "HelloWorld"
print(list(reversed(s)))

for x in reversed(s):
    print(x, end = " ")