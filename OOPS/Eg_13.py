# polymorphism
# Methodoverloading , constructor overloading , operator overloading

from multipledispatch import dispatch
class product:

    @dispatch(int,str)
    def getproductdetails(self,pid , pname):
        self.pid = pid
        self.pname = pname
        print(self.pid ,self.pname)

    @dispatch(float,str)
    def getproductdetails(self,pid , pname):
        self.pid = pid
        self.pname = pname
        print(self.pid ,self.pname)

    @dispatch(str)
    def __init__(self ,job):
        self.job = job
        print(self.job)

    @dispatch(int)
    def __init__(self ,contact):
        self.contact = contact
        print(self.contact)


p = product("sales jobs")
p.getproductdetails(101,"apple")
p.getproductdetails(101.10 , "lg")

p = product(554554586)