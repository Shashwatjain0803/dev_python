import re

string = "Mr.Shashwat"
pattern = r"M"
j = re.match(pattern,string)
print(j)
print(j.group())

string = "Myageis21"
pattern = r'\w\w'
j = re.match(pattern,string)
print(j)
print(j.group())