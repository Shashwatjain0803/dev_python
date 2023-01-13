import re

string = " Most welcome in jabalpur 9479674703 and 626468033 "
pattern = r'\d+'
j = re.findall(pattern,string)
print(j)

string = " Most welcome in jabalpur 9479674703 and 626468033 "
pattern = r'\w+'
j = re.findall(pattern,string)
print(j)