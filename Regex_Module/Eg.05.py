import re

pattern = r'(My home)'
string = "My home in Jabalpur madhya pradesh etc...."
r = re.search(pattern, string)
print(r.group())