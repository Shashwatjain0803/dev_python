import re

string = "shashwat"
pattern = r'h'
j = re.findall(pattern,string)
print(j)

string = "abc--ABC--def--DEF"
pattern = r"[a-z]+"
result = re.findall(pattern, string)
print(result)

string = "abc--ABC--def--DEF"
pattern = r"[a-z]+"
flags = re.IGNORECASE
result = re.findall(pattern, string, flags)
print(result)

string = "apple, man-go, grapes_, _goa,carrot_"
pattern = r"[a-z]+"
result = re.findall(pattern, string)
print(result)

pattern = r"wel...e"
string = "welcome"
r = re.findall(pattern, string)
print(r)

pattern = r'love'
string = 'i love 5 cars and love 5 bives'
replace = "like"
r = re.sub(pattern, replace, string)
print(r)

pattern = r"\D"
string = "SaiKiran1234"
r = re.findall(pattern, string)
print(r)

pattern = r"\S"
string = "My Name is SaiKiran"
r = re.findall(pattern, string)
print(r)

pattern = r"\s"
string = "My Name is SaiKiran"
r = re.findall(pattern, string)
print(r)

pattern = r'[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|in|net)'
string = "saikiran@edu.com"
if(re.search(pattern, string)):
    print("Valid")
else:
    print("Invalid")