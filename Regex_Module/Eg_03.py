import re

string = 'shahswatjain0803@gmail.com'
pattern = r'(\w+)@(\w+).(\w+)'
j = re.match(pattern,string)
print(j)
print(j.group(0))
print(j.group(1))
print(j.group(2))
print(j.group(3))
print(j.group(1,2,3))
print(j.groups())