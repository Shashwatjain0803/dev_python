
# instance method
class product:


    # def __init__(self):
    #     print("special method/, constructor")
     def __init__(self,pid,pname):
         self.pid = pid
         self.pname = pname

     def display(self):
         print(self.pid, self.pname)


p = product(101,"Mi")
p.display()
p = product(102,"vivo")
p.display()