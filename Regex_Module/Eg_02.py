import re

string = "My home sweet home "
pattern = r'\w+'
j = re.match(pattern,string)
print(j)
print(j.group())


#  (\w+ only accept this)  a-z , A-Z , _ ,0-9
string = "My_home@sweet!home "
pattern = r'\w+'
j = re.match(pattern,string)
print(j)
print(j.group())

