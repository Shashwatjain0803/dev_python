import re

pattern = r'(^h)'
string = "hexagon"
j = re.search(pattern,string)
print(j.group())

pattern = r'(jain$)'
string = "shashwatjain"
j = re.search(pattern,string)
print(j.group())