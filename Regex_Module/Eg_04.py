import re

string = "shashwatjain0803@gmail.com"
pattern = r'(?P<username>\w+)@(?P<mail>\w+)\.(?P<extension>\w+)'
j = re.match(pattern,string)
print(j)
print(j.groupdict())