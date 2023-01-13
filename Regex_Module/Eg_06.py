import re

pattern = r'(name.*)'
string = "My name is Batman"
j = re.search(pattern,string)
print(j)
print(j.group())