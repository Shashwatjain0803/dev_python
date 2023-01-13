employees = [
    {'firstName':"sai", 'lastname': 'kumar', 'age': 25},
    {'firstName':"pradeep", 'lastname': 'reedy', 'age': 29},
    {'firstName':"praneeth", 'lastname': 'reddy', 'age': 35},
    {'firstName':"ranjith", 'lastname': 'yadav', 'age': 30},
    {'firstName':"rohit", 'lastname': 'kumar', 'age': 32}
]
print(employees)
print('---')
print(employees[0]['firstName'] + employees[0]['lastname'])
print(employees[1]['firstName'] + employees[1]['lastname'])
print(employees[2]['firstName'] + employees[2]['lastname'])
print(employees[3]['firstName'] + employees[3]['lastname'])

print('---')

m = map(lambda x:x['firstName'] + x['lastname'], employees)
print(list(m))