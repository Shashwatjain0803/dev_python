class Employeesalary(Exception):

    def usersalary(self,Esalary):

        if(Esalary < 5000 ):
            raise Exception ("salary is less than 5000")
        else:
            print("your salary is ", Esalary)

Employeesalary().usersalary(6000)
Employeesalary().usersalary(4500)

