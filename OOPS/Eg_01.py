
# instance method

class product :


     # def getproductdetails(self):
     #     print("instance method")



   def getproductsdetails(self,pid,pname):
       self.pid = pid
       self.pname = pname

   def display(self):
       print(self.pid , self.pname)

p = product()
p.getproductsdetails(101 , "Mi" )
p.display()
p.getproductsdetails(102 , "vivo")
p.display()